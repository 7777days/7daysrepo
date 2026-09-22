# -*- coding: utf-8 -*-
"""
OTT Sync v1.00 - Backup/Restore and Settings
"""

import os
import sys
import socket
import datetime
import subprocess
import platform
import xbmc
import xbmcgui
import xbmcvfs
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')

SMB_HOST_CANDIDATES = ["192.168.50.195", "100.85.97.35"]
SMB_PORT_CHECK_TIMEOUT = 1.0
SMB_SHARE = "WD/kodi_sync"

ITEMS = {
    "favourites": {
        "label": "Favourites",
        "local": ["special://profile/favourites.xml"],
        "filenames": ["favourites.xml"]
    },
    "carlinkit": {
        "label": "CarLinkKit Settings",
        "local": [
            "special://profile/guisettings.xml",
            "special://profile/addon_data/skin.estuary/settings.xml"
        ],
        "filenames": [
            "guisettings.xml",
            "settings.xml"
        ]
    }
}


def log(msg):
    xbmc.log("[{}] {}".format(ADDON_NAME, msg), level=xbmc.LOGINFO)


def notify(msg, error=False):
    icon = xbmcgui.NOTIFICATION_ERROR if error else xbmcgui.NOTIFICATION_INFO
    xbmcgui.Dialog().notification(ADDON_NAME, msg, icon, 4000)


def resolve_smb_host():
    for host in SMB_HOST_CANDIDATES:
        try:
            s = socket.create_connection((host, 445), timeout=SMB_PORT_CHECK_TIMEOUT)
            s.close()
            return host
        except Exception:
            continue
    return SMB_HOST_CANDIDATES[0]


def get_smb_credentials():
    try:
        user = ADDON.getSettingString('smb_user')
        pw = ADDON.getSettingString('smb_pass')
        return user, pw
    except Exception as e:
        log("설정값 로드 실패: {}".format(e))
        return "7777days", ""


def remote_root():
    host = resolve_smb_host()
    user, pw = get_smb_credentials()
    if user:
        return "smb://{}:{}@{}/{}/".format(user, pw, host, SMB_SHARE)
    return "smb://{}/{}/".format(host, SMB_SHARE)


def read_text(path):
    try:
        if not xbmcvfs.exists(path):
            return None
        f = xbmcvfs.File(path)
        raw = f.readBytes()
        f.close()
        return raw.decode('utf-8', errors='ignore') if isinstance(raw, (bytes, bytearray)) else raw
    except Exception as e:
        log("읽기 실패 {}: {}".format(path, e))
        return None


def write_text(path, text):
    try:
        f = xbmcvfs.File(path, 'w')
        f.write(text.encode('utf-8'))
        f.close()
        return True
    except Exception as e:
        log("쓰기 실패 {}: {}".format(path, e))
        return False


def force_kill_kodi():
    """OS 상관없이 Kodi 메모리가 덮어씌워지지 않도록 강제 종료"""
    system_name = platform.system()
    try:
        if "android" in sys.platform.lower() or os.path.exists("/system/bin"):
            os.system("killall -9 org.xbmc.kodi")
            os.system("am force-stop org.xbmc.kodi")
        elif system_name == "Windows":
            subprocess.Popen("taskkill /F /IM Kodi.exe /T", shell=True)
        elif system_name == "Darwin":
            os.system("killall -9 Kodi")
        elif system_name == "Linux":
            os.system("killall -9 kodi.bin")
    except Exception as e:
        log("강제종료 실패: {}".format(e))
    os._exit(0)


def get_formatted_mtime(path):
    try:
        if xbmcvfs.exists(path):
            stat = xbmcvfs.Stat(path)
            mtime = stat.st_mtime()
            if mtime > 0:
                dt = datetime.datetime.fromtimestamp(mtime)
                return dt.strftime('%Y-%m-%d %H:%M')
    except Exception as e:
        log("날짜 조회 실패 {}: {}".format(path, e))
    return None


def format_bytes(n):
    try:
        n = float(n)
    except Exception:
        return ""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if n < 1024.0:
            if unit == 'B':
                return "{:.0f}{}".format(n, unit)
            return "{:.1f}{}".format(n, unit)
        n /= 1024.0
    return "{:.1f}TB".format(n)


def get_formatted_size(path):
    try:
        if xbmcvfs.exists(path):
            stat = xbmcvfs.Stat(path)
            return format_bytes(stat.st_size())
    except Exception as e:
        log("크기 조회 실패 {}: {}".format(path, e))
    return ""


def is_cancelled(selected, default_path):
    """
    빈 값일 때만 취소로 간주한다.

    참고: Kodi Dialog().browse()는 취소해도 defaultt로 넘긴 경로를 그대로
    반환하는 경우가 있어(공식 문서에 명시된 동작), 예전엔 '반환값==기본경로'도
    취소로 처리했다. 하지만 이 애드온에서는 SMB 공유 최상위 폴더 자체가
    실제로 유효한 선택지라서, 그 판단 때문에 정상적인 선택까지 취소로
    오인하는 문제가 생겼다. 그래서 빈 값 여부만 확인하고, 대신 다음 단계의
    확인창(예/아니오)에서 실수로 인한 진행을 막는다.
    """
    return not selected or not str(selected).strip()


def pick_folder_native(dialog_type, heading, default_path=None):
    """
    Kodi 기본(네이티브) 폴더 전용 브라우저를 사용한다.
    dialog_type=3 (ShowAndGetWriteableDirectory): 백업 등 쓰기 대상 폴더 선택.
        '새 폴더 만들기' 버튼이 함께 제공된다.
    dialog_type=0 (ShowAndGetDirectory): 불러오기 등 읽기 대상 폴더 선택.

    이 타입들은 파일은 보여주지 않지만, 폴더 자체를 고르면 바로 '확인'이
    폴더 선택으로 동작한다(파일을 따로 찍을 필요가 없다).
    """
    default_path = default_path or remote_root()
    selected = xbmcgui.Dialog().browse(dialog_type, heading, 'files', defaultt=default_path)

    if is_cancelled(selected, default_path):
        return None

    if not selected.endswith('/'):
        selected = selected + '/'
    return selected


def do_export(key):
    item = ITEMS[key]

    folder = pick_folder_native(3, "Select backup location - {}".format(item["label"]))
    if not folder:
        return

    confirm_msg = "[{}] Proceed with export?\n\n".format(item["label"])
    will_overwrite = False
    for fn in item["filenames"]:
        target_path = folder + fn
        mtime_str = get_formatted_mtime(target_path)
        if mtime_str:
            confirm_msg += "- Existing {}: modified [{}] (will be overwritten)\n".format(fn, mtime_str)
            will_overwrite = True
        else:
            confirm_msg += "- New {}: (no existing file)\n".format(fn)

    if not xbmcgui.Dialog().yesno(ADDON_NAME, confirm_msg):
        return

    if will_overwrite:
        warn_msg = (
            "WARNING\n\n"
            "One or more existing files on the server will be overwritten.\n"
            "This action CANNOT be undone.\n\n"
            "Are you absolutely sure you want to continue?"
        )
        if not xbmcgui.Dialog().yesno(ADDON_NAME, warn_msg):
            return

    success_all = True
    for local_path, fn in zip(item["local"], item["filenames"]):
        local_text = read_text(local_path)
        if local_text is None:
            notify("Failed to read local file: {}".format(fn), error=True)
            success_all = False
            continue

        dest_path = folder + fn

        # 기존 파일이 있으면 덮어쓰기 전에 백업 (최신 백업 1개만 유지)
        if xbmcvfs.exists(dest_path):
            backup_path = dest_path + ".bak"
            if xbmcvfs.exists(backup_path):
                xbmcvfs.delete(backup_path)
            old_text = read_text(dest_path)
            if old_text is not None:
                if not write_text(backup_path, old_text):
                    log("백업 생성 실패: {}".format(backup_path))

        if not write_text(dest_path, local_text):
            notify("Export failed: {}".format(fn), error=True)
            success_all = False

    if success_all:
        notify("{} export complete".format(item["label"]))


def do_import(key):
    """
    폴더 하나만 선택하면 그 안에서 필요한 파일(들)을 자동으로 찾아
    한꺼번에 불러온다. (즐겨찾기 1개 파일, 카링킷 2개 파일 모두 동일)
    """
    item = ITEMS[key]

    folder = pick_folder_native(0, "Select folder to import - {}".format(item["label"]))
    if not folder:
        return

    found = []
    missing = []
    for fn in item["filenames"]:
        full = folder + fn
        if xbmcvfs.exists(full):
            mtime_str = get_formatted_mtime(full) or "-"
            found.append((fn, full, mtime_str))
        else:
            missing.append(fn)

    if missing:
        notify("Required file(s) missing in this folder: {}".format(", ".join(missing)), error=True)
        return

    confirm_msg = "[{}] Import the following file(s)?\n\n".format(item["label"])
    for fn, _full, mtime_str in found:
        confirm_msg += "- {} (modified {})\n".format(fn, mtime_str)

    if not xbmcgui.Dialog().yesno(ADDON_NAME, confirm_msg):
        return

    success_all = True
    for local_path, (fn, full, _mtime_str) in zip(item["local"], found):
        remote_text = read_text(full)
        if remote_text is None:
            notify("Failed to read {}".format(fn), error=True)
            success_all = False
            continue
        if not write_text(local_path, remote_text):
            notify("Failed to apply {}".format(fn), error=True)
            success_all = False

    if success_all:
        if key == "carlinkit":
            xbmcgui.Dialog().ok(ADDON_NAME, "CarLinkKit settings import complete.\nKodi will now force-close to apply the changes.")
            force_kill_kodi()
        else:
            notify("{} import complete".format(item["label"]))


def show_sub_menu(key):
    item = ITEMS[key]
    while True:
        options = [
            "[COLOR FF2ECC71]Export to Server[/COLOR]",
            "[COLOR FFE74C3C]Import from Server[/COLOR]"
        ]
        idx = xbmcgui.Dialog().select(item["label"], options)

        if idx < 0:
            break
        elif idx == 0:
            do_export(key)
        elif idx == 1:
            do_import(key)


def main_menu():
    while True:
        menu_items = [
            "1. Favourites Sync",
            "2. CarLinkKit Settings"
        ]

        idx = xbmcgui.Dialog().select(ADDON_NAME, menu_items)

        if idx < 0:
            break
        elif idx == 0:
            show_sub_menu("favourites")
        elif idx == 1:
            show_sub_menu("carlinkit")


if __name__ == '__main__':
    main_menu()
