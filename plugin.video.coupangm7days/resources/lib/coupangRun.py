_B1='PASS_VOD_LIST'
_B0='SPORTS_SEASON_VODLIST'
_A_='running_time'
_Az='SPORTS_SEASON_GROUP'
_Ay='SPORTS_FEED_VOD'
_Ax='SPORTS_LEAGUE_FEEDLIST'
_Aw='SPORTS_MULT_HERO'
_Av='Container.Refresh'
_Au='delete.png'
_At='RunPlugin(plugin://plugin.video.coupangm/?%s)'
_As='Dialog.Close(all,true)'
_Ar='(통합) 찜 영상에 추가'
_Aq='RunPlugin(plugin://plugin.video.coupangm/?mode=SET_BOOKMARK&bm_param=%s)'
_Ap='vsubtitle'
_Ao='Year : %s\nSeason : %s'
_An='EVENT_LIST'
_Am='EVENT_GAMELIST'
_Al='coupang_orderby'
_Ak='search_history.png'
_Aj='search.png'
_Ai='SPORTS_MAINLIST_LEAGUE'
_Ah='obj_id'
_Ag='SPORTS_SEASON_GAMELIST'
_Af='gameID'
_Ae='subMode'
_Ad='league_name'
_Ac='subType'
_Ab='startDate'
_Aa='MYVIEW_REMOVE'
_AZ='WATCH_ONE'
_AY='WATCH_ALL'
_AX='SEARCH_ALL'
_AW='SEARCH_ONE'
_AV='SEARCH_REMOVE'
_AU='orderby'
_AT='EPISODE_LIST'
_AS='movies'
_AR='vtitle'
_AQ='vidtype'
_AP='videoid'
_AO=' (%s)'
_AN='TVSHOW'
_AM='genreList'
_AL='badge'
_AK='pre_title'
_AJ='historyyn'
_AI='SEARCH_HISTORY'
_AH='THEME_GROUPLIST'
_AG='PASS_GROUPLIST'
_AF='MOVIES'
_AE='TVSHOWS'
_AD='preText'
_AC='search_key'
_AB='next.png'
_AA='다음 페이지'
_A9='[B]%s >>[/B]'
_A8='tvshows'
_A7='MENU_BOOKMARK'
_A6='TOTAL_HISTORY'
_A5='WATCH'
_A4='CATEGORY_GROUPLIST'
_A3='seasonID'
_A2='leagueID'
_A1='skey'
_A0='delType'
_z='watchedlist_%s.txt'
_y='search'
_x='SEASON_LIST'
_w='list'
_v='int'
_u='stype'
_t='TOTAL_SEARCH'
_s='CATEGORY_LIST'
_r='image'
_q='code'
_p='programimg'
_o='programnm'
_n='programid'
_m='genre'
_l='LOCAL_SEARCH'
_k='w'
_j='seasonList'
_i='1'
_h='true'
_g='season'
_f='episode'
_e='league_id'
_d='path'
_c='string'
_b='icon'
_a='HIGHLIGHT'
_Z='MOVIE'
_Y='LIVE'
_X='img'
_W='utf-8'
_V='mpaa'
_U='movie'
_T='thumbnail'
_S='duration'
_R='tvshow'
_Q='year'
_P='utf8'
_O='collectionId'
_N='page'
_M='type'
_L='episodes'
_K='func'
_J='vType'
_I='asis'
_H='id'
_G='mediatype'
_F='plot'
_E=None
_D=True
_C='title'
_B=False
_A='mode'
__author__='NightRain'
import os,xbmcplugin,xbmcgui,xbmcaddon,xbmc,xbmcvfs,inputstreamhelper,sys,datetime,urllib,json
__addon__=xbmcaddon.Addon()
__language__=__addon__.getLocalizedString
__profile__=xbmcvfs.translatePath(__addon__.getAddonInfo('profile'))
__version__=__addon__.getAddonInfo('version')
__addonid__=__addon__.getAddonInfo(_H)
__addonname__=__addon__.getAddonInfo('name')
MAIN_GROUP=[{_C:'오직 쿠팡플레이에서',_A:_s,_J:'ORIGINAL',_O:'525c9e79-aa9c-448f-a22d-431db00780bd'},{_C:'홈   (장르별)',_A:_A4,_J:'ALL'},{_C:'TV   (장르별)',_A:_A4,_J:_AE},{_C:'영화 (장르별)',_A:_A4,_J:_AF},{_C:'(패스) 스포츠',_A:_Ai},{_C:'(패스) Paramount+',_A:_AG,_O:'1afeaf87-0b7a-4a49-a971-fa5be7aedf4e'},{_C:'(패스) Sony Pictures',_A:_AG,_O:'5b37af01-01fb-4361-ba5b-0f23f307d557'},{_C:'TV   (테마별)',_A:_AH,_J:_AE},{_C:'영화 (테마별)',_A:_AH,_J:_AF},{_C:'-----------------',_A:'XXX'},{_C:'Watched (시청목록)',_A:_A5,_b:'history.png'},{_C:'(쿠팡) 검색',_A:_l,_b:_Aj},{_C:'(쿠팡) 검색기록',_A:_AI,_b:_Ak},{_C:'통합검색(웨이브,티빙,왓챠,쿠팡,넷플)',_A:_t,_b:_Aj},{_C:'통합검색(웨이브,티빙,왓챠,쿠팡,넷플) 기록',_A:_A6,_b:_Ak},{_C:'통합 찜 목록 (bookmark mini)',_A:_A7,_b:'bookmark.png'}]
WATCH_GROUP=[{_C:'시리즈 시청내역',_A:_A5,_u:_R},{_C:'영화 시청내역',_A:_A5,_u:_U}]
INFO_CONVERT_KEY={_C:{_K:'setTitle',_M:_c},_F:{_K:'setPlot',_M:_c},_V:{_K:'setMpaa',_M:_c},_G:{_K:'setMediaType',_M:_c},'tvshowtitle':{_K:'setTvShowTitle',_M:_c},'premiered':{_K:'setPremiered',_M:_c},'aired':{_K:'setFirstAired',_M:_c},_Q:{_K:'setYear',_M:_v},_S:{_K:'setDuration',_M:_v},_f:{_K:'setEpisode',_M:_v},_g:{_K:'setSeason',_M:_v},'studio':{_K:'setStudios',_M:_w},_m:{_K:'setGenres',_M:_w},'country':{_K:'setCountries',_M:_w},'cast':{_K:'setCast',_M:'actor'},'director':{_K:'setDirectors',_M:_w}}
SEARCHED_FILE_NAME=xbmcvfs.translatePath(os.path.join(__profile__,'coupang_searched.txt'))
from coupangCore import*
class CoupangRun:
	def __init__(self,in_addonurl,in_handle,in_params):self._addon_url=in_addonurl;self._addon_handle=in_handle;self.main_params=in_params;self.CoupangObj=Coupang();self.CoupangObj.CP_COOKIE_FILENAME=xbmcvfs.translatePath(os.path.join(__profile__,'cp_cookies.json'));self.CoupangObj.CP_DEVICE_FILENAME=xbmcvfs.translatePath(os.path.join(__profile__,'cp_device.json'))
	def addon_noti(self,sting):
		try:dialog=xbmcgui.Dialog();dialog.notification(__addonname__,sting)
		except:_E
	def addon_log(self,string):
		try:log_message=string.encode(_W,'ignore')
		except:log_message='addonException: addon_log'
		level=xbmc.LOGINFO;xbmc.log('[%s-%s]: %s'%(__addonid__,__version__,log_message),level=level)
	def get_keyboard_input(self,title):
		input_text=_E;kb=xbmc.Keyboard();kb.setHeading(title);xbmc.sleep(1000);kb.doModal()
		if kb.isConfirmed():input_text=kb.getText()
		return input_text
	def get_settings_account(self):cpid=__addon__.getSetting(_H);cppw=__addon__.getSetting('pw');cppf=__addon__.getSetting('profile');return cpid,cppw,cppf
	def get_settings_exclusion21(self):
		exclusion21=__addon__.getSetting('exclusion21')
		if exclusion21=='false':return _B
		else:return _D
	def get_settings_totalsearch(self):local_search=_D if __addon__.getSetting('local_search')==_h else _B;local_history=_D if __addon__.getSetting('local_history')==_h else _B;total_search=_D if __addon__.getSetting('total_search')==_h else _B;total_history=_D if __addon__.getSetting('total_history')==_h else _B;menu_bookmark=_D if __addon__.getSetting('menu_bookmark')==_h else _B;return local_search,local_history,total_search,total_history,menu_bookmark
	def get_settings_makebookmark(self):return _D if __addon__.getSetting('make_bookmark')==_h else _B
	def set_winEpisodeOrderby(self,orderby):__addon__.setSetting(_Al,orderby)
	def get_winEpisodeOrderby(self):
		orderby=__addon__.getSetting(_Al)
		if orderby in['',_E]:orderby='asc'
		return orderby
	def add_dir(self,label,sublabel='',img='',infoLabels=_E,isFolder=_D,params='',isLink=_B,ContextMenu=_E):
		url='%s?%s'%(self._addon_url,urllib.parse.urlencode(params))
		if sublabel:title='%s < %s >'%(label,sublabel)
		else:title=label
		if not img:img='DefaultFolder.png'
		listitem=xbmcgui.ListItem(title)
		if type(img)==dict:listitem.setArt(img)
		else:listitem.setArt({'thumb':img,'poster':img})
		if self.CoupangObj.KodiVersion>=20:
			if infoLabels:self.Set_InfoTag(listitem.getVideoInfoTag(),infoLabels)
		elif infoLabels:listitem.setInfo('Video',infoLabels)
		if not isFolder and not isLink:listitem.setProperty('IsPlayable',_h)
		if ContextMenu:listitem.addContextMenuItems(ContextMenu)
		xbmcplugin.addDirectoryItem(self._addon_handle,url,listitem,isFolder)
	def Set_InfoTag(self,video_InfoTag,infoLabels):
		for(key,value)in infoLabels.items():
			if INFO_CONVERT_KEY[key][_M]==_c:getattr(video_InfoTag,INFO_CONVERT_KEY[key][_K])(value)
			elif INFO_CONVERT_KEY[key][_M]==_v:
				if type(value)==int:intValue=int(value)
				else:intValue=0
				getattr(video_InfoTag,INFO_CONVERT_KEY[key][_K])(intValue)
			elif INFO_CONVERT_KEY[key][_M]=='actor':
				if value!=[]:getattr(video_InfoTag,INFO_CONVERT_KEY[key][_K])([xbmc.Actor(name)for name in value])
			elif INFO_CONVERT_KEY[key][_M]==_w:
				if type(value)==list:getattr(video_InfoTag,INFO_CONVERT_KEY[key][_K])(value)
				else:getattr(video_InfoTag,INFO_CONVERT_KEY[key][_K])([value])
	def dp_Main_List(self,args):
		local_search,local_history,total_search,total_history,menu_bookmark=self.get_settings_totalsearch()
		for main_group in MAIN_GROUP:
			title=main_group.get(_C);icon_img=''
			if main_group.get(_A)==_l and local_search==_B:continue
			elif main_group.get(_A)==_AI and local_history==_B:continue
			elif main_group.get(_A)==_t and total_search==_B:continue
			elif main_group.get(_A)==_A6 and total_history==_B:continue
			elif main_group.get(_A)==_A7 and menu_bookmark==_B:continue
			params={_A:main_group.get(_A),_J:main_group.get(_J),_O:main_group.get(_O),_N:_i}
			if main_group.get(_A)==_l:params[_AJ]='Y'
			if main_group.get(_A)in['XXX',_t,_A6,_A7]:isFolder=_B;isLink=_D
			else:isFolder=_D;isLink=_B
			infoLabels={_C:title,_F:title}
			if main_group.get(_A)=='XXX':infoLabels=_E
			if _b in main_group:icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,main_group.get(_b))
			self.add_dir(title,sublabel='',img=icon_img,infoLabels=infoLabels,isFolder=isFolder,params=params,isLink=isLink)
		xbmcplugin.endOfDirectory(self._addon_handle)
	def dp_Test(self,args):self.addon_noti('test')
	def CP_logout(self):
		dialog=xbmcgui.Dialog();ret=dialog.yesno(__language__(30905).encode(_P),__language__(30906).encode(_P))
		if ret==_B:return
		if os.path.isfile(self.CoupangObj.CP_COOKIE_FILENAME):os.remove(self.CoupangObj.CP_COOKIE_FILENAME)
		self.addon_noti(__language__(30904).encode(_W))
	def option_check(self):
		if self.cookiefile_check()==_D:
			if self.CoupangObj.CP['SESSION']['bm_sv_ex']<int(time.time()):
				if self.CoupangObj.Get_CP_profile()==_B:self.addon_noti(__language__(30909).encode(_P));sys.exit()
			return
		dialog=xbmcgui.Dialog();wc_file=dialog.browse(1,__language__(30917).encode(_P),'','.twc',_B,_B,'',_B)
		if wc_file!='':
			tempFile=xbmcvfs.translatePath(os.path.join(__profile__,'coupanginfo-temp.twc'));xbmcvfs.copy(wc_file,tempFile);loginResult=self.CoupangObj.WebCookies_Load(tempFile);xbmcvfs.delete(tempFile)
			if loginResult:
				self.CoupangObj.dic_To_jsonfile(self.CoupangObj.CP_COOKIE_FILENAME,self.CoupangObj.CP)
				if self.CoupangObj.Get_CP_profile():self.addon_noti(__language__(30910).encode(_P));return
				else:self.addon_noti(__language__(30903).encode(_P));sys.exit()
		else:self.addon_noti(__language__(30903).encode(_P));sys.exit()
	def cookiefile_check(self):
		json_data={}
		try:fp=open(self.CoupangObj.CP_COOKIE_FILENAME,'r',-1,_W);json_data=json.load(fp);fp.close()
		except Exception as exception:return _B
		self.CoupangObj.CP=json_data
		try:
			if self.CoupangObj.CP['ACCOUNT']['cpid']!='eHh4eHg=':self.CoupangObj.Init_CP();return _B
		except:self.CoupangObj.Init_CP();return _B
		return _D
	def CP_login(self,cpid,cppw,cppf):
		self.CoupangObj.Init_CP()
		if self.CoupangObj.Get_CP_Login(cpid,cppw,cppf)==_B:return _B
		if self.CoupangObj.Get_CP_profile(cppf,limit_days=int(__addon__.getSetting('cache_ttl')),re_check=_B)==_B:return _B
		return _D
	def dp_Category_GroupList(self,args):
		vType=args.get(_J);self.addon_log('Category_Group : {}'.format(vType));GN_LIST=self.CoupangObj.Get_Category_GroupList(vType)
		for gn_list in GN_LIST:
			title=gn_list.get(_C);pre_title=gn_list.get(_AK)
			if self.get_settings_exclusion21()==_D and title=='성인':continue
			info={_G:_R,_F:pre_title};params={_A:_s,_O:gn_list.get(_O),_J:gn_list.get('category'),_N:_i};self.add_dir(title,sublabel='',img='',infoLabels=info,isFolder=_D,params=params)
		xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Theme_GroupList(self,args):
		vType=args.get(_J);self.addon_log('Theme_Group : {}'.format(vType));GN_LIST=self.CoupangObj.Get_Theme_GroupList(vType)
		for gn_list in GN_LIST:title=gn_list.get(_C);pre_title=gn_list.get(_AK);info={_G:_R,_F:pre_title};params={_A:_s,_O:gn_list.get(_O),_J:gn_list.get('category'),_N:_i};self.add_dir(title,sublabel='',img='',infoLabels=info,isFolder=_D,params=params)
		xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Event_GroupList(self,args):
		GN_LIST=self.CoupangObj.Get_Event_GroupList()
		for gn_list in GN_LIST:title=gn_list.get(_C);pre_title=gn_list.get(_AK);info={_G:_R,_F:pre_title};params={_A:_Am,_O:gn_list.get(_O),_J:_Y};self.add_dir(title,sublabel='',img='',infoLabels=info,isFolder=_D,params=params)
		xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Event_GameList(self,args):
		vType=args.get(_J);collectionId=args.get(_O);GN_LIST=self.CoupangObj.Get_Event_GameList(collectionId)
		for gn_list in GN_LIST:title=gn_list.get(_C);id=gn_list.get(_H);thumbnail=gn_list.get(_T);asis=gn_list.get(_I);addInfo=gn_list.get('addInfo');starttm=gn_list.get('starttm');info={_G:_R,_C:title,_F:addInfo};params={_A:_An,_H:id,_I:asis,_C:title};self.add_dir(title,sublabel=starttm,img=thumbnail,infoLabels=info,isFolder=_D,params=params,ContextMenu=_E)
		xbmcplugin.setContent(self._addon_handle,_A8);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Event_List(self,args):
		gameId=args.get(_H);GN_LIST=self.CoupangObj.Get_Event_List(gameId)
		for gn_list in GN_LIST:title=gn_list.get(_C);id=gn_list.get(_H);thumbnail=gn_list.get(_T);asis=gn_list.get(_I);duration=gn_list.get(_S);starttm=gn_list.get('starttm');info={_G:_f,_C:title,_F:asis,_S:duration};params={_A:asis,_H:id,_I:asis,_C:title};self.add_dir(title,sublabel=starttm,img=thumbnail,infoLabels=info,isFolder=_B,params=params,ContextMenu=_E)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Category_List(self,args):
		vType=args.get(_J);collectionId=args.get(_O);page_int=int(args.get(_N));self.addon_log('Category_List : {} - {}'.format(vType,collectionId));GN_LIST,more_page=self.CoupangObj.Get_Category_List(vType,collectionId,page_int)
		for gn_list in GN_LIST:
			title=gn_list.get(_C);id=gn_list.get(_H);thumbnail=gn_list.get(_T);mpaa=gn_list.get(_V);duration=gn_list.get(_S);asis=gn_list.get(_I);badge=gn_list.get(_AL);year=gn_list.get(_Q);seasonList=gn_list.get(_j);genreList=gn_list.get(_AM)
			if asis in[_AN]:mode=_x;info={_G:_R,_C:title,_V:mpaa,_m:genreList,_Q:year,_F:_Ao%(year,seasonList)};isFolder=_D
			else:mode=_Z;info={_G:_U,_C:title,_V:mpaa,_m:genreList,_S:duration,_Q:year,_F:'(%s)'%mpaa};isFolder=_B;title+=_AO%str(year)
			params={_A:mode,_H:id,_I:asis,_j:seasonList,_C:title,_T:thumbnail,_Q:year}
			if self.get_settings_makebookmark():bm_param={_AP:id,_AQ:_U if vType==_AF else _R,_AR:title,_Ap:''};bm_param_str=json.dumps(bm_param);bm_param_str=urllib.parse.quote(bm_param_str);bookmark_url=_Aq%bm_param_str;ContextMenu=[(_Ar,bookmark_url)]
			else:ContextMenu=_E
			self.add_dir(title,sublabel=badge,img=thumbnail,infoLabels=info,isFolder=isFolder,params=params,ContextMenu=ContextMenu)
		if more_page:params[_A]=_s;params[_O]=collectionId;params[_J]=vType;params[_N]=str(page_int+1);title=_A9%_AA;subtitle=str(page_int+1);icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,_AB);self.add_dir(title,sublabel=subtitle,img=icon_img,infoLabels=_E,isFolder=_D,params=params)
		if vType==_AE:xbmcplugin.setContent(self._addon_handle,_A8)
		else:xbmcplugin.setContent(self._addon_handle,_AS)
		xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Season_List(self,args):
		programnm=args.get(_C);programid=args.get(_H);asis=args.get(_I);seasonList=args.get(_j);thumbnail=args.get(_T);year=args.get(_Q)
		if seasonList in['',_E]:self.addon_log('programid  = {}'.format(programid));seasonList=self.CoupangObj.Get_vInfo(programid).get(_j)
		if len(seasonList.split(','))>1:
			self.addon_log('seasonList = {}'.format(seasonList))
			for i_season in seasonList.split(','):title='시즌 '+i_season;info={_G:_R,_F:'%s (%s)'%(programnm,year)};params={_A:_AT,_n:programid,_o:programnm,_g:i_season,_I:asis,_p:thumbnail,_N:_i};tmp_thumbnail=thumbnail.replace("'",'"');tmp_thumbnail=json.loads(tmp_thumbnail);self.add_dir(title,sublabel='',img=tmp_thumbnail,infoLabels=info,isFolder=_D,params=params)
			xbmcplugin.setContent(self._addon_handle,_A8);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
		else:self.addon_log('programid xx = {}'.format(programid));sendArgs={_n:programid,_o:programnm,_g:seasonList,_p:thumbnail,_N:_i};self.dp_Episode_List(sendArgs)
	def dp_Episode_List(self,args):
		A='desc';programid=args.get(_n);programnm=args.get(_o);season=args.get(_g);programimg=args.get(_p);page_int=int(args.get(_N));SEASION_LIST,more_page=self.CoupangObj.Get_Episode_List(programid,season,page=page_int,orderby=self.get_winEpisodeOrderby())
		for i_season in SEASION_LIST:episodenm=i_season.get(_C);episodeid=i_season.get(_H);asis=i_season.get(_I);thumbnail=i_season.get(_T);mpaa=i_season.get(_V);duration=i_season.get(_S);year=i_season.get(_Q);episode=i_season.get(_f);genreList=i_season.get(_AM);desc=i_season.get(A);preTitle='%sx%s'%(season,episode);title='%s. %s'%(preTitle,episodenm);info={_G:_f,_V:mpaa,_m:genreList,_S:duration,_Q:year,_F:'%s (%s)\n\n%s'%(programnm,preTitle,desc)};params={_A:'VOD',_n:programid,_o:programnm,_C:title,_g:season,_H:episodeid,_I:asis,_T:thumbnail,_p:programimg};self.add_dir(title,sublabel='',img=thumbnail,infoLabels=info,isFolder=_B,params=params)
		if page_int==1:
			info={_F:'정렬순서를 변경합니다.'};params={};params[_A]='ORDER_BY'
			if self.get_winEpisodeOrderby()==A:title='정렬순서변경 : 최신화부터 -> 1회부터';params[_AU]='asc'
			else:title='정렬순서변경 : 1회부터 -> 최신화부터';params[_AU]=A
			icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,'sort.png');self.add_dir(title,sublabel='',img=icon_img,infoLabels=info,isFolder=_B,params=params,isLink=_D)
		if more_page:params={};params[_A]=_AT;params[_n]=programid;params[_o]=programnm;params[_g]=season;params[_p]=programimg;params[_N]=str(page_int+1);title=_A9%_AA;subtitle=str(page_int+1);icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,_AB);self.add_dir(title,sublabel=subtitle,img=icon_img,infoLabels=_E,isFolder=_D,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def play_VIDEO(self,args):
		G='inputstream.adaptive.manifest_headers';F='inputstream.adaptive.stream_headers';E='inputstream.adaptive.manifest_type';D='inputstream.adaptive';C='inputstream';B='com.widevine.alpha';A='EPISODE';mediacode=args.get(_H);asis=args.get(_I)
		if asis in[_a]:streaming_url,drm_license=self.CoupangObj.GetEventURL(mediacode,asis)
		elif asis in[_Y]:streaming_url,drm_license=self.CoupangObj.GetEventURL_Live(mediacode,asis)
		else:streaming_url,drm_license=self.CoupangObj.GetBroadURL(mediacode)
		self.addon_log('asis, url : %s - %s - %s'%(asis,mediacode,streaming_url))
		if streaming_url=='':
			if drm_license=='':self.addon_noti(__language__(30907).encode(_P))
			else:self.addon_log('drm_license_1 : %s'%drm_license);self.addon_noti(drm_license)
			return
		else:self.addon_log('drm_license : %s'%drm_license)
		"\n\t\ttmp_cookie = 'PCID=%s;token=%s;member_srl=%s;NEXT_LOCALE=%s;session_web_id=%s;device_id=%s' % (\n\t\t\tself.CoupangObj.CP['COOKIES']['PCID'],\n\t\t\tself.CoupangObj.CP['COOKIES']['token'],\n\t\t\tself.CoupangObj.CP['COOKIES']['member_srl'],\n\t\t\tself.CoupangObj.CP['COOKIES']['NEXT_LOCALE'],\n\t\t\tself.CoupangObj.CP['COOKIES']['session_web_id'],\n\t\t\tself.CoupangObj.CP['COOKIES']['device_id'],\n\t\t)\n\t\t"
		if asis in[A]:referer='https://www.coupangplay.com/play/{}/episode?titleId={}&type=EPISODE&sourceType=page_discover_title_detail%3Apage_discover_feed'.format(mediacode,mediacode)
		elif asis in[_Z]:referer='https://www.coupangplay.com/play/{}/movie?sourceType=page_discover_feed'.format(mediacode)
		else:referer='https://www.coupangplay.com/play/'+mediacode
		surl=streaming_url;self.addon_log('tobe, surl : %s'%surl);item=xbmcgui.ListItem(path=surl);post_fix=self.CoupangObj.Get_Url_PostFix(streaming_url);self.addon_log('post_fix : '+post_fix)
		if post_fix=='m3u8':PROTOCOL='hls'
		else:PROTOCOL='mpd'
		raw_headers={'user-agent':self.CoupangObj.USER_AGENT,'referer':referer};raw_cookies={}
		for(i_key,i_value)in self.CoupangObj.CP['COOKIES'].items():
			if i_key in COOKIES_DEFAULT:raw_cookies[i_key]=i_value
		stream_headers=self.CoupangObj.make_stream_header(raw_headers,raw_cookies)
		if drm_license:
			DRMHOST=drm_license;DRM=B;"\n\t\t\theaders\t= {\n\t\t\t\t\t\t'traceparent'  : traceparent,\n\t\t\t\t\t\t'tracestate'   : tracestate,\n\t\t\t\t\t\t'newrelic'     : newrelic,\n\t\t\t\t\t\t#'content-type' : 'application/octet-stream',\n\t\t\t\t\t\t'User-Agent'   : self.CoupangObj.USER_AGENT,\n\t\t\t\t\t\t'Referer'      : referer, # 2022.07.16 추가 (권한체크?)\n\t\t\t\t\t\t'Cookie'       : tmp_cookie,\n\t\t\t}\n\t\t\t";LICENSE_KEY=DRMHOST+'|'+stream_headers+'|R{SSM}|';inputstreamhelper.Helper(PROTOCOL,drm=B).check_inputstream();item.setProperty(C,D)
			if self.CoupangObj.KodiVersion<=20:item.setProperty(E,PROTOCOL)
			item.setProperty('inputstream.adaptive.license_type',DRM);item.setProperty('inputstream.adaptive.license_key',LICENSE_KEY);item.setProperty(F,stream_headers);item.setProperty(G,stream_headers);item.setMimeType('application/dash+xml');item.setContentLookup(_B)
		else:
			item.setContentLookup(_B);item.setMimeType('application/x-mpegURL');item.setProperty(C,D)
			if self.CoupangObj.KodiVersion<=20:item.setProperty(E,PROTOCOL)
			item.setProperty(F,stream_headers);item.setProperty(G,stream_headers)
		xbmcplugin.setResolvedUrl(self._addon_handle,_D,item)
		try:
			if asis==_Z:stype=_U;params={_q:mediacode,_I:asis,_C:args.get(_C),_X:args.get(_T)};self.Save_Watched_List(stype,params)
			elif asis==A:stype=_R;params={_q:args.get(_n),_I:asis,_C:'%s <%s>'%(args.get(_C),args.get(_o)),_X:args.get(_p)};self.Save_Watched_List(stype,params)
		except:_E
	def dp_Global_Search(self,args):
		mode=args.get(_A)
		if mode==_t:ott_url='ActivateWindow(10025,"plugin://plugin.video.searchm/?mode=TOTAL_SEARCH",return)'
		else:ott_url='ActivateWindow(10025,"plugin://plugin.video.searchm/?mode=TOTAL_HISTORY",return)'
		xbmc.executebuiltin(_As);xbmc.executebuiltin(ott_url)
	def dp_Bookmark_Menu(self,args):ott_url='ActivateWindow(10025,"plugin://plugin.video.bookmarkm/",return)';xbmc.executebuiltin(_As);xbmc.executebuiltin(ott_url)
	def dp_Search_List(self,args):
		page_int=int(args.get(_N))
		if _AC in args:search_key=args.get(_AC)
		else:
			search_key=self.get_keyboard_input(__language__(30908).encode(_W))
			if not search_key:return
		SEARCH_LIST,more_page=self.CoupangObj.Get_Search_List(search_key,page_int)
		for search_list in SEARCH_LIST:
			id=search_list.get(_H);title=search_list.get(_C);asis=search_list.get(_I);thumbnail=search_list.get(_T);mpaa=search_list.get(_V);year=search_list.get(_Q);duration=search_list.get(_S);badge=search_list.get(_AL)
			if asis==_AN:mode=_x;info={_G:_R,_C:title,_V:mpaa,_Q:year,_F:'Year : %s'%year};isFolder=_D
			elif asis==_Z:mode=_Z;info={_G:_U,_C:title,_V:mpaa,_S:duration,_Q:year,_F:'(%s)'%mpaa};isFolder=_B;title+=_AO%str(year)
			elif asis==_a:mode=_a;info={_G:_f,_C:title,_S:duration,_F:mode};isFolder=_B
			elif asis==_Y:mode=_Y;info={_G:_f,_C:title,_F:mode};isFolder=_B
			params={_A:mode,_H:id,_I:asis,_j:'',_C:title,_T:json.dumps(thumbnail,separators=(',',':')),_Q:year}
			if self.get_settings_makebookmark()and asis not in[_a,'']:bm_param={_AP:id,_AQ:_U if asis==_Z else _R,_AR:title,_Ap:''};bm_param_str=json.dumps(bm_param);bm_param_str=urllib.parse.quote(bm_param_str);bookmark_url=_Aq%bm_param_str;ContextMenu=[(_Ar,bookmark_url)]
			else:ContextMenu=_E
			self.add_dir(title,sublabel=badge,img=thumbnail,infoLabels=info,isFolder=isFolder,params=params,ContextMenu=ContextMenu)
		if more_page:params={};params[_A]=_l;params[_AC]=search_key;params[_N]=str(page_int+1);title=_A9%_AA;subtitle=str(page_int+1);icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,_AB);self.add_dir(title,sublabel=subtitle,img=icon_img,infoLabels=_E,isFolder=_D,params=params)
		xbmcplugin.setContent(self._addon_handle,_AS);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_D)
		if args.get(_AJ)=='Y':self.Save_Searched_List(search_key)
	def Load_List_File(self,stype):
		try:
			if stype==_y:filename=SEARCHED_FILE_NAME
			elif stype in[_R,_U]:filename=xbmcvfs.translatePath(os.path.join(__profile__,_z%stype))
			else:return[]
			fp=open(filename,'r',-1,_W);result=fp.readlines();fp.close()
		except:result=[]
		return result
	def Save_Watched_List(self,stype,in_params):
		try:
			watchfile=xbmcvfs.translatePath(os.path.join(__profile__,_z%stype));oldlist=self.Load_List_File(stype);fp=open(watchfile,_k,-1,_W);newlist=urllib.parse.urlencode(in_params);newlist=newlist+'\n';fp.write(newlist);addcount=0
			for olditem in oldlist:
				old_dic=dict(urllib.parse.parse_qsl(olditem));new_id=in_params.get(_q).strip();old_id=old_dic.get(_q).strip()
				if new_id!=old_id:
					fp.write(olditem);addcount+=1
					if addcount>=50:break
			fp.close()
		except:_E
	def Save_Searched_List(self,search_key):
		try:
			search_key=search_key.strip();oldlist=self.Load_List_File(_y);fp=open(SEARCHED_FILE_NAME,_k,-1,_W);fp.write(search_key+'\n');addcount=0
			for olditem in oldlist:
				olditem=olditem.strip()
				if search_key!=olditem:
					fp.write(olditem+'\n');addcount+=1
					if addcount>=50:break
			fp.close()
		except:_E
	def dp_Search_History(self,args):
		SEARCH_HISTORY=self.Load_List_File(_y)
		for search_history in SEARCH_HISTORY:search_history=search_history.strip();params={_A:_l,_AC:search_history,_N:_i,_AJ:'Y'};menu_param={_A:_AV,_A0:_AW,_A1:search_history,_J:'-'};menu_param_str=urllib.parse.urlencode(menu_param);ContextMenu=[('선택된 검색어 ( %s ) 삭제'%search_history,_At%menu_param_str)];self.add_dir(search_history,sublabel='',img=_E,infoLabels=_E,isFolder=_D,params=params,ContextMenu=ContextMenu)
		info={_F:'검색목록 전체를 삭제합니다.'};title='** 검색목록 전체삭제 (개별삭제는 팝업메뉴 사용) **';params={_A:_AV,_A0:_AX,_A1:'-',_J:'-'};icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,_Au);self.add_dir(title,sublabel='',img=icon_img,infoLabels=info,isFolder=_B,params=params,isLink=_D);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Listfile_Delete(self,args):
		delType=args.get(_A0);skey=args.get(_A1);vType=args.get(_J);dialog=xbmcgui.Dialog()
		if delType==_AX:ret=dialog.yesno(__language__(30911).encode(_P),__language__(30906).encode(_P))
		elif delType==_AW:ret=dialog.yesno(__language__(30912).encode(_P),__language__(30906).encode(_P))
		elif delType==_AY:ret=dialog.yesno(__language__(30913).encode(_P),__language__(30906).encode(_P))
		elif delType==_AZ:ret=dialog.yesno(__language__(30916).encode(_P),__language__(30906).encode(_P))
		if ret==_B:sys.exit()
		if delType==_AX:
			if os.path.isfile(SEARCHED_FILE_NAME):os.remove(SEARCHED_FILE_NAME)
		elif delType==_AW:
			try:
				filename=SEARCHED_FILE_NAME;oldlist=self.Load_List_File(_y);fp=open(filename,_k,-1,_W)
				for olditem in oldlist:
					if skey!=olditem.strip():fp.write(olditem)
				fp.close()
			except:_E
		elif delType==_AY:
			filename=xbmcvfs.translatePath(os.path.join(__profile__,_z%vType))
			if os.path.isfile(filename):os.remove(filename)
		elif delType==_AZ:
			filename=xbmcvfs.translatePath(os.path.join(__profile__,_z%vType))
			try:
				oldlist=self.Load_List_File(vType);fp=open(filename,_k,-1,_W)
				for olditem in oldlist:
					old_dic=dict(urllib.parse.parse_qsl(olditem));old_skey=old_dic.get(_q).strip()
					if skey!=old_skey:fp.write(olditem)
				fp.close()
			except:_E
		xbmc.executebuiltin(_Av)
	def Delete_List_File(self,stype,skey='-'):
		if stype=='ALL':
			try:filename=SEARCHED_FILE_NAME;fp=open(filename,_k,-1,_W);fp.write('');fp.close()
			except:_E
		elif stype=='ONE':
			try:
				filename=SEARCHED_FILE_NAME;oldlist=self.Load_List_File(_y);fp=open(filename,_k,-1,_W)
				for olditem in oldlist:
					if skey!=olditem.strip():fp.write(olditem)
				fp.close()
			except:_E
		elif stype in[_R,_U]:
			try:filename=xbmcvfs.translatePath(os.path.join(__profile__,_z%stype));fp=open(filename,_k,-1,_W);fp.write('');fp.close()
			except:_E
	def dp_Watch_List(self,args):
		stype=args.get(_u)
		if stype in['',_E]:
			for i_section in WATCH_GROUP:title=i_section.get(_C);params={_A:i_section.get(_A),_u:i_section.get(_u)};self.add_dir(title,sublabel='',img='',infoLabels=_E,isFolder=_D,params=params)
			xbmcplugin.endOfDirectory(self._addon_handle)
		else:
			WATCHLIST=self.Load_List_File(stype)
			for watchlist in WATCHLIST:
				hist_params=dict(urllib.parse.parse_qsl(watchlist));mediacode=hist_params.get(_q).strip();title=hist_params.get(_C).strip();thumbnail=hist_params.get(_X).strip();asis=hist_params.get(_I).strip()
				try:thumbnail=thumbnail.replace("'",'"');thumbnail=json.loads(thumbnail)
				except:_E
				info={};info[_F]=title
				if stype==_U:info[_G]=_U;params={_A:_Z,_H:mediacode,_I:asis,_C:title,_T:thumbnail};isFolder=_B
				else:info[_G]=_f;params={_A:_x,_H:mediacode,_I:asis,_C:title,_T:json.dumps(thumbnail,separators=(',',':'))};isFolder=_D
				menu_param={_A:_Aa,_A0:_AZ,_A1:mediacode,_J:stype};menu_param_str=urllib.parse.urlencode(menu_param);ContextMenu=[('선택된 시청이력 ( %s ) 삭제'%title,_At%menu_param_str)];self.add_dir(title,sublabel='',img=thumbnail,infoLabels=info,isFolder=isFolder,params=params,ContextMenu=ContextMenu)
			info={_F:'시청목록을 삭제합니다.'};title='** 시청목록 전체삭제 (개별삭제는 팝업메뉴 사용) **';params={_A:_Aa,_A0:_AY,_A1:'-',_J:stype};icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,_Au);self.add_dir(title,sublabel='',img=icon_img,infoLabels=info,isFolder=_B,params=params,isLink=_D)
			if stype==_U:xbmcplugin.setContent(self._addon_handle,_AS)
			else:xbmcplugin.setContent(self._addon_handle,_A8)
			xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Set_Bookmark(self,args):
		main_param=urllib.parse.unquote(args.get('bm_param'));main_param=json.loads(main_param);videoid=main_param.get(_AP);vidtype=main_param.get(_AQ);vtitle=main_param.get(_AR);dialog=xbmcgui.Dialog();ret=dialog.yesno(__language__(30914).encode(_P),vtitle+' \n\n'+__language__(30915))
		if ret==_B:return
		VIDEO_INFO=self.CoupangObj.GetBookmarkInfo(videoid,vidtype);bookmark_param=json.dumps(VIDEO_INFO);bookmark_param=urllib.parse.quote(bookmark_param);bookmark_url='RunPlugin(plugin://plugin.video.bookmarkm/?mode=SET_BOOKMARK&bm_param=%s)'%bookmark_param;xbmc.executebuiltin(bookmark_url)
	def sp_MultiHero_LiveList(self,args):
		LIVE_LIST=self.CoupangObj.Sports_MultiHero_LiveList()
		for i_vod in LIVE_LIST:
			id=i_vod.get(_H);title=i_vod.get(_C);startDate=i_vod.get(_Ab);image=i_vod.get(_r);subType=i_vod.get(_Ac);sublabel=startDate
			if subType:sublabel=sublabel+', '+subType
			info={_G:_L,_F:title};params={_A:_Y,_I:_Y,_H:id};self.add_dir(title,sublabel=sublabel,img=image,infoLabels=info,isFolder=_B,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def sp_Mainlist_League(self,args):
		LIVE_LIST=self.CoupangObj.Sports_MultiHero_LiveList()
		if LIVE_LIST:title='@ 주요 예정경기 @';image=LIVE_LIST[0][_r];preText=self.CoupangObj.MakeText_FreeList(LIVE_LIST,titleName='preTitle');info={_G:_L,_F:preText};params={_A:_Aw};self.add_dir(title,sublabel='',img=image,infoLabels=info,isFolder=_D,params=params)
		MAINGAME_LIST=self.CoupangObj.Sports_Mainlist_League()
		for i_list in MAINGAME_LIST:league_id=i_list.get(_e);league_name=i_list.get(_Ad);logoUrl=i_list.get('logoUrl');info={_G:_L,_F:league_name};params={_A:_Ax,_e:league_id,_Ad:league_name};self.add_dir(league_name,sublabel='',img=logoUrl,infoLabels=info,isFolder=_D,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def sp_League_FeedList(self,args):
		league_id=args.get(_e);league_name=args.get(_Ad);FEED_LIST=self.CoupangObj.Sports_League_FeedList(league_id)
		for i_list in FEED_LIST:row_name=i_list.get('row_name');preText=i_list.get(_AD);subMode=i_list.get(_Ae);gameID=i_list.get(_Af);image=i_list.get(_r);info={_G:_L,_F:league_name+'\n\n'+preText};params={_A:_Ay,_Ae:subMode,_e:league_id,'game_id':gameID};self.add_dir(row_name,sublabel='',img=image,infoLabels=info,isFolder=_D,params=params)
		title='@ 시즌별 동영상 @';info={_G:_L,_F:title};params={_A:_Az,_e:league_id};self.add_dir(title,sublabel='',img=_E,infoLabels=info,isFolder=_D,params=params);xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def sp_League_VodList(self,args):
		A='{} - {}';subMode=args.get(_Ae);league_id=args.get(_e);game_id=args.get('game_id');self.addon_log(A.format('subMode  ',subMode));self.addon_log(A.format(_e,league_id));self.addon_log(A.format('game_id  ',game_id));VOD_LIST=self.CoupangObj.Sports_League_VodList(subMode,league_id,game_id)
		for i_list in VOD_LIST:
			id=i_list.get(_H);title=i_list.get(_C);image=i_list.get(_r);startDate=i_list.get(_Ab);subType=i_list.get(_Ac);running_time=i_list.get(_A_);info={_G:_L,_F:title,_S:running_time}
			if subMode=='SP_FEED_LIVE':
				params={_A:_Y,_I:_Y,_H:id};sublabel=startDate
				if subType:sublabel=sublabel+', '+subType
			elif subMode in['SP_FEED_TOP10','SP_FEED_GAME']:params={_A:_a,_I:_a,_H:id};sublabel=subType
			self.add_dir(title,sublabel=sublabel,img=image,infoLabels=info,isFolder=_B,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def sp_Season_Group(self,args):
		league_id=args.get(_e);SEASON_LIST=self.CoupangObj.Sports_Season_Group(league_id)
		for i_list in SEASON_LIST:season=i_list.get(_g);preText=i_list.get(_AD);info={_G:_L,_F:preText};params={_A:_Ag,_A2:league_id,_A3:season,_N:_i};self.add_dir(season,sublabel=_E,img=_E,infoLabels=info,isFolder=_D,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def sp_Season_GameList(self,args):
		leagueID=args.get(_A2);seasonID=args.get(_A3);page_int=int(args.get(_N));GAME_LIST=self.CoupangObj.Sports_Season_GameList(leagueID,seasonID,page_int);game_count=len(GAME_LIST)
		for i_list in GAME_LIST:gameID=i_list.get(_H);title=i_list.get(_C);startDate=i_list.get(_Ab);preText=i_list.get(_AD);image=i_list.get(_r);info={_G:_L,_F:preText};params={_A:_B0,_A2:leagueID,_A3:seasonID,_Af:gameID,_N:args.get(_N)};self.add_dir(title,sublabel=startDate,img=image,infoLabels=info,isFolder=_D,params=params)
		if game_count>=10:params[_A]=_Ag;params[_A2]=leagueID;params[_A3]=seasonID;params[_N]=str(page_int+1);title=_A9%_AA;subtitle=str(page_int+1);icon_img=os.path.join(xbmcaddon.Addon().getAddonInfo(_d),_X,_AB);self.add_dir(title,sublabel=subtitle,img=icon_img,infoLabels=_E,isFolder=_D,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def sp_Season_VodList(self,args):
		leagueID=args.get(_A2);seasonID=args.get(_A3);page_int=int(args.get(_N));gameID=args.get(_Af);VOD_LIST=self.CoupangObj.Sports_Season_GameVod(leagueID,seasonID,page_int,gameID)
		for i_list in VOD_LIST:id=i_list.get(_H);title=i_list.get(_C);image=i_list.get(_r);subType=i_list.get(_Ac);running_time=i_list.get(_A_);info={_G:_L,_F:title,_S:running_time};params={_A:_a,_I:_a,_H:id};sublabel=subType;self.add_dir(title,sublabel=sublabel,img=image,infoLabels=info,isFolder=_B,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Pass_Group(self,args):
		collectionId=args.get(_O);GROUP_LIST=self.CoupangObj.Get_Pass_GroupList(collectionId)
		for i_list in GROUP_LIST:obj_id=i_list.get(_Ah);title=i_list.get(_C);preText=i_list.get(_AD);info={_G:_L,_F:preText};params={_A:_B1,_O:collectionId,_Ah:obj_id};self.add_dir(title,sublabel=_E,img=_E,infoLabels=info,isFolder=_D,params=params)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_Pass_VodList(self,args):
		collectionId=args.get(_O);obj_id=args.get(_Ah);GN_LIST=self.CoupangObj.Get_Pass_VodList(collectionId,obj_id)
		for gn_list in GN_LIST:
			title=gn_list.get(_C);id=gn_list.get(_H);thumbnail=gn_list.get(_T);mpaa=gn_list.get(_V);duration=gn_list.get(_S);sub_type=gn_list.get('sub_type');badge=gn_list.get(_AL);year=gn_list.get(_Q);seasonList=gn_list.get(_j);genreList=gn_list.get(_AM)
			if sub_type in[_AN]:mode=_x;info={_G:_R,_C:title,_V:mpaa,_m:genreList,_Q:year,_F:_Ao%(year,seasonList)};isFolder=_D
			else:mode=_Z;info={_G:_U,_C:title,_V:mpaa,_m:genreList,_S:duration,_Q:year,_F:'(%s)'%mpaa};isFolder=_B;title+=_AO%str(year)
			params={_A:mode,_H:id,_I:sub_type,_j:seasonList,_C:title,_T:thumbnail,_Q:year};self.add_dir(title,sublabel=badge,img=thumbnail,infoLabels=info,isFolder=isFolder,params=params,ContextMenu=_E)
		xbmcplugin.setContent(self._addon_handle,_L);xbmcplugin.endOfDirectory(self._addon_handle,cacheToDisc=_B)
	def dp_setEpOrderby(self,args):orderby=args.get(_AU);self.set_winEpisodeOrderby(orderby);xbmc.executebuiltin(_Av)
	def coupang_main(self):
		self.CoupangObj.KodiVersion=int(xbmc.getInfoLabel('System.BuildVersion').split('.')[0]);mode=self.main_params.get(_A,_E)
		if mode=='LOGOUT':self.CP_logout();return
		self.option_check()
		if mode is _E:self.dp_Main_List(self.main_params)
		elif mode==_A4:self.dp_Category_GroupList(self.main_params)
		elif mode==_AH:self.dp_Theme_GroupList(self.main_params)
		elif mode=='EVENT_GROUPLIST':self.dp_Event_GroupList(self.main_params)
		elif mode==_Am:self.dp_Event_GameList(self.main_params)
		elif mode==_An:self.dp_Event_List(self.main_params)
		elif mode==_s:self.dp_Category_List(self.main_params)
		elif mode==_x:self.dp_Season_List(self.main_params)
		elif mode==_AT:self.dp_Episode_List(self.main_params)
		elif mode=='TEST':self.dp_Test(self.main_params)
		elif mode in[_Z,'VOD',_a,_Y]:self.play_VIDEO(self.main_params)
		elif mode==_A5:self.dp_Watch_List(self.main_params)
		elif mode==_l:self.dp_Search_List(self.main_params)
		elif mode==_AI:self.dp_Search_History(self.main_params)
		elif mode in[_Aa,_AV]:self.dp_Listfile_Delete(self.main_params)
		elif mode in[_t,_A6]:self.dp_Global_Search(self.main_params)
		elif mode==_A7:self.dp_Bookmark_Menu(self.main_params)
		elif mode=='SET_BOOKMARK':self.dp_Set_Bookmark(self.main_params)
		elif mode==_Ai:self.sp_Mainlist_League(self.main_params)
		elif mode==_Ax:self.sp_League_FeedList(self.main_params)
		elif mode==_Ay:self.sp_League_VodList(self.main_params)
		elif mode==_Aw:self.sp_MultiHero_LiveList(self.main_params)
		elif mode==_Az:self.sp_Season_Group(self.main_params)
		elif mode==_Ag:self.sp_Season_GameList(self.main_params)
		elif mode==_B0:self.sp_Season_VodList(self.main_params)
		elif mode==_AG:self.dp_Pass_Group(self.main_params)
		elif mode==_B1:self.dp_Pass_VodList(self.main_params)
		elif mode=='ORDER_BY':self.dp_setEpOrderby(self.main_params)
		else:_E