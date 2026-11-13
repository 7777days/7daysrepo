__author__="NightRain"
rTOxgawICeoqHGbsBALPiVFjlfdpkz=object
rTOxgawICeoqHGbsBALPiVFjlfdpkM=None
rTOxgawICeoqHGbsBALPiVFjlfdpkR=False
rTOxgawICeoqHGbsBALPiVFjlfdpkv=True
rTOxgawICeoqHGbsBALPiVFjlfdpkn=getattr
rTOxgawICeoqHGbsBALPiVFjlfdpkh=type
rTOxgawICeoqHGbsBALPiVFjlfdpkJ=int
rTOxgawICeoqHGbsBALPiVFjlfdpkS=list
rTOxgawICeoqHGbsBALPiVFjlfdpkU=len
rTOxgawICeoqHGbsBALPiVFjlfdpkm=str
rTOxgawICeoqHGbsBALPiVFjlfdpku=id
rTOxgawICeoqHGbsBALPiVFjlfdpkY=open
rTOxgawICeoqHGbsBALPiVFjlfdpkD=dict
import os
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,xbmcvfs
import sys
import inputstreamhelper
import datetime
import time
import urllib
import base64
__addon__=xbmcaddon.Addon()
__language__ =__addon__.getLocalizedString
__profile__=xbmcvfs.translatePath(__addon__.getAddonInfo('profile'))
__version__=__addon__.getAddonInfo('version')
__addonid__=__addon__.getAddonInfo('id')
__addonname__=__addon__.getAddonInfo('name')
rTOxgawICeoqHGbsBALPiVFjlfdpcy=[{'title':'TV 채널 (유료사용자만 지원)','mode':'LIVE_GROUP','icon':'live.png'},{'title':'Live중계 (경기중에만 재생)','mode':'ELIVE_GROUP','icon':'live.png'},{'title':'-----------------','mode':'XXX'},{'title':'오늘의 추천 VOD','mode':'NOW_GROUP'},{'title':'인기영상 5','mode':'POP_GROUP'},{'title':'-----------------','mode':'XXX'},{'title':'VOD (리그, 경기별)','mode':'VOD_GROUP'},{'title':'Watched (시청목록)','mode':'WATCH','icon':'history.png'},]
rTOxgawICeoqHGbsBALPiVFjlfdpcE={'title':{'func':'setTitle','type':'string'},'plot':{'func':'setPlot','type':'string'},'mpaa':{'func':'setMpaa','type':'string'},'mediatype':{'func':'setMediaType','type':'string'},'tvshowtitle':{'func':'setTvShowTitle','type':'string'},'premiered':{'func':'setPremiered','type':'string'},'aired':{'func':'setFirstAired','type':'string'},'year':{'func':'setYear','type':'int'},'duration':{'func':'setDuration','type':'int'},'episode':{'func':'setEpisode','type':'int'},'season':{'func':'setSeason','type':'int'},'studio':{'func':'setStudios','type':'list'},'genre':{'func':'setGenres','type':'list'},'country':{'func':'setCountries','type':'list'},'cast':{'func':'setCast','type':'actor'},'director':{'func':'setDirectors','type':'list'},}
rTOxgawICeoqHGbsBALPiVFjlfdpcW=xbmcvfs.translatePath(os.path.join(__profile__,'spotv_cookies.json'))
from spotvCore import*
class rTOxgawICeoqHGbsBALPiVFjlfdpcN(rTOxgawICeoqHGbsBALPiVFjlfdpkz):
 def __init__(rTOxgawICeoqHGbsBALPiVFjlfdpck,rTOxgawICeoqHGbsBALPiVFjlfdpcK,rTOxgawICeoqHGbsBALPiVFjlfdpcX,rTOxgawICeoqHGbsBALPiVFjlfdpcz):
  rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_url =rTOxgawICeoqHGbsBALPiVFjlfdpcK
  rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle=rTOxgawICeoqHGbsBALPiVFjlfdpcX
  rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params =rTOxgawICeoqHGbsBALPiVFjlfdpcz
  rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj =vYQmocyXJSfDubORxeaCUqIjHBWgTn() 
 def addon_noti(rTOxgawICeoqHGbsBALPiVFjlfdpck,sting):
  try:
   rTOxgawICeoqHGbsBALPiVFjlfdpcR=xbmcgui.Dialog()
   rTOxgawICeoqHGbsBALPiVFjlfdpcR.notification(__addonname__,sting)
  except:
   rTOxgawICeoqHGbsBALPiVFjlfdpkM
 def addon_log(rTOxgawICeoqHGbsBALPiVFjlfdpck,string):
  try:
   rTOxgawICeoqHGbsBALPiVFjlfdpcv=string.encode('utf-8','ignore')
  except:
   rTOxgawICeoqHGbsBALPiVFjlfdpcv='addonException: addon_log'
  rTOxgawICeoqHGbsBALPiVFjlfdpcn=xbmc.LOGINFO
  xbmc.log("[%s-%s]: %s"%(__addonid__,__version__,rTOxgawICeoqHGbsBALPiVFjlfdpcv),level=rTOxgawICeoqHGbsBALPiVFjlfdpcn)
 def get_keyboard_input(rTOxgawICeoqHGbsBALPiVFjlfdpck,rTOxgawICeoqHGbsBALPiVFjlfdpcu):
  rTOxgawICeoqHGbsBALPiVFjlfdpch=rTOxgawICeoqHGbsBALPiVFjlfdpkM
  kb=xbmc.Keyboard()
  kb.setHeading(rTOxgawICeoqHGbsBALPiVFjlfdpcu)
  xbmc.sleep(1000)
  kb.doModal()
  if(kb.isConfirmed()):
   rTOxgawICeoqHGbsBALPiVFjlfdpch=kb.getText()
  return rTOxgawICeoqHGbsBALPiVFjlfdpch
 def get_settings_account(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  rTOxgawICeoqHGbsBALPiVFjlfdpcJ =__addon__.getSetting('id')
  rTOxgawICeoqHGbsBALPiVFjlfdpcS =__addon__.getSetting('pw')
  return(rTOxgawICeoqHGbsBALPiVFjlfdpcJ,rTOxgawICeoqHGbsBALPiVFjlfdpcS)
 def get_settings_hidescoreyn(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  rTOxgawICeoqHGbsBALPiVFjlfdpcU =__addon__.getSetting('hidescore')
  if rTOxgawICeoqHGbsBALPiVFjlfdpcU=='false':
   return rTOxgawICeoqHGbsBALPiVFjlfdpkR
  else:
   return rTOxgawICeoqHGbsBALPiVFjlfdpkv
 def add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpck,label,sublabel='',img='',infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpkM,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkv,params='',isLink=rTOxgawICeoqHGbsBALPiVFjlfdpkR,ContextMenu=rTOxgawICeoqHGbsBALPiVFjlfdpkM):
  rTOxgawICeoqHGbsBALPiVFjlfdpcm='%s?%s'%(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_url,urllib.parse.urlencode(params))
  if sublabel:rTOxgawICeoqHGbsBALPiVFjlfdpcu='%s < %s >'%(label,sublabel)
  else: rTOxgawICeoqHGbsBALPiVFjlfdpcu=label
  if not img:img='DefaultFolder.png'
  rTOxgawICeoqHGbsBALPiVFjlfdpcY=xbmcgui.ListItem(rTOxgawICeoqHGbsBALPiVFjlfdpcu)
  rTOxgawICeoqHGbsBALPiVFjlfdpcY.setArt({'thumb':img,'icon':img,'poster':img})
  if rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.KodiVersion>=20:
   if infoLabels:rTOxgawICeoqHGbsBALPiVFjlfdpck.Set_InfoTag(rTOxgawICeoqHGbsBALPiVFjlfdpcY.getVideoInfoTag(),infoLabels)
  else:
   if infoLabels:rTOxgawICeoqHGbsBALPiVFjlfdpcY.setInfo('Video',infoLabels)
  if not isFolder and not isLink:
   rTOxgawICeoqHGbsBALPiVFjlfdpcY.setProperty('IsPlayable','true')
  if ContextMenu:rTOxgawICeoqHGbsBALPiVFjlfdpcY.addContextMenuItems(ContextMenu)
  xbmcplugin.addDirectoryItem(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,rTOxgawICeoqHGbsBALPiVFjlfdpcm,rTOxgawICeoqHGbsBALPiVFjlfdpcY,isFolder)
 def Set_InfoTag(rTOxgawICeoqHGbsBALPiVFjlfdpck,video_InfoTag:xbmc.InfoTagVideo,rTOxgawICeoqHGbsBALPiVFjlfdpNz):
  for rTOxgawICeoqHGbsBALPiVFjlfdpcD,value in rTOxgawICeoqHGbsBALPiVFjlfdpNz.items():
   if rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['type']=='string':
    rTOxgawICeoqHGbsBALPiVFjlfdpkn(video_InfoTag,rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['func'])(value)
   elif rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['type']=='int':
    if rTOxgawICeoqHGbsBALPiVFjlfdpkh(value)==rTOxgawICeoqHGbsBALPiVFjlfdpkJ:
     rTOxgawICeoqHGbsBALPiVFjlfdpcQ=rTOxgawICeoqHGbsBALPiVFjlfdpkJ(value)
    else:
     rTOxgawICeoqHGbsBALPiVFjlfdpcQ=0
    rTOxgawICeoqHGbsBALPiVFjlfdpkn(video_InfoTag,rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['func'])(rTOxgawICeoqHGbsBALPiVFjlfdpcQ)
   elif rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['type']=='actor':
    if value!=[]:
     rTOxgawICeoqHGbsBALPiVFjlfdpkn(video_InfoTag,rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['func'])([xbmc.Actor(name)for name in value])
   elif rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['type']=='list':
    if rTOxgawICeoqHGbsBALPiVFjlfdpkh(value)==rTOxgawICeoqHGbsBALPiVFjlfdpkS:
     rTOxgawICeoqHGbsBALPiVFjlfdpkn(video_InfoTag,rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['func'])(value)
    else:
     rTOxgawICeoqHGbsBALPiVFjlfdpkn(video_InfoTag,rTOxgawICeoqHGbsBALPiVFjlfdpcE[rTOxgawICeoqHGbsBALPiVFjlfdpcD]['func'])([value])
 def get_selQuality(rTOxgawICeoqHGbsBALPiVFjlfdpck,etype):
  try:
   rTOxgawICeoqHGbsBALPiVFjlfdpct='selected_quality'
   rTOxgawICeoqHGbsBALPiVFjlfdpNc=[1080,720,540]
   rTOxgawICeoqHGbsBALPiVFjlfdpNy=rTOxgawICeoqHGbsBALPiVFjlfdpkJ(__addon__.getSetting(rTOxgawICeoqHGbsBALPiVFjlfdpct))
   return rTOxgawICeoqHGbsBALPiVFjlfdpNc[rTOxgawICeoqHGbsBALPiVFjlfdpNy]
  except:
   rTOxgawICeoqHGbsBALPiVFjlfdpkM
  return 1080 
 def dp_Main_List(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  for rTOxgawICeoqHGbsBALPiVFjlfdpNE in rTOxgawICeoqHGbsBALPiVFjlfdpcy:
   rTOxgawICeoqHGbsBALPiVFjlfdpcu=rTOxgawICeoqHGbsBALPiVFjlfdpNE.get('title')
   rTOxgawICeoqHGbsBALPiVFjlfdpNW=''
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':rTOxgawICeoqHGbsBALPiVFjlfdpNE.get('mode'),'page':'1'}
   if rTOxgawICeoqHGbsBALPiVFjlfdpNE.get('mode')=='XXX':
    rTOxgawICeoqHGbsBALPiVFjlfdpNK=rTOxgawICeoqHGbsBALPiVFjlfdpkR
    rTOxgawICeoqHGbsBALPiVFjlfdpNX =rTOxgawICeoqHGbsBALPiVFjlfdpkv
   else:
    rTOxgawICeoqHGbsBALPiVFjlfdpNK=rTOxgawICeoqHGbsBALPiVFjlfdpkv
    rTOxgawICeoqHGbsBALPiVFjlfdpNX =rTOxgawICeoqHGbsBALPiVFjlfdpkR
   rTOxgawICeoqHGbsBALPiVFjlfdpNz={'title':rTOxgawICeoqHGbsBALPiVFjlfdpcu,'plot':rTOxgawICeoqHGbsBALPiVFjlfdpcu}
   if rTOxgawICeoqHGbsBALPiVFjlfdpNE.get('mode')=='XXX':rTOxgawICeoqHGbsBALPiVFjlfdpNz=rTOxgawICeoqHGbsBALPiVFjlfdpkM
   if 'icon' in rTOxgawICeoqHGbsBALPiVFjlfdpNE:rTOxgawICeoqHGbsBALPiVFjlfdpNW=os.path.join(xbmcaddon.Addon().getAddonInfo('path'),'img',rTOxgawICeoqHGbsBALPiVFjlfdpNE.get('icon')) 
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel='',img=rTOxgawICeoqHGbsBALPiVFjlfdpNW,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNz,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpNK,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk,isLink=rTOxgawICeoqHGbsBALPiVFjlfdpNX)
  if rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpcy)>0:xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def dp_MainLeague_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('dp_MainLeague_List')
  rTOxgawICeoqHGbsBALPiVFjlfdpNR=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetTitleGroupList()
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('dp_MainLeague_List cnt : '+rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpNR)))
  for rTOxgawICeoqHGbsBALPiVFjlfdpNv in rTOxgawICeoqHGbsBALPiVFjlfdpNR:
   rTOxgawICeoqHGbsBALPiVFjlfdpcu =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('title')
   rTOxgawICeoqHGbsBALPiVFjlfdpNn =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('logo')
   rTOxgawICeoqHGbsBALPiVFjlfdpNh =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('reagueId')
   rTOxgawICeoqHGbsBALPiVFjlfdpNJ =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('subGame')
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'mediatype':'episode','plot':'%s\n\n%s'%(rTOxgawICeoqHGbsBALPiVFjlfdpcu,rTOxgawICeoqHGbsBALPiVFjlfdpNJ)}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'LEAGUE_GROUP','reagueId':rTOxgawICeoqHGbsBALPiVFjlfdpNh}
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpkM,img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkv,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  if rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpNR)>0:xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def dp_NowVod_GroupList(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpNU=rTOxgawICeoqHGbsBALPiVFjlfdpkJ(args.get('page'))
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('dp_NowVod_GroupList page : '+rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpNU))
  rTOxgawICeoqHGbsBALPiVFjlfdpNR,rTOxgawICeoqHGbsBALPiVFjlfdpNm=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Get_NowVod_GroupList(rTOxgawICeoqHGbsBALPiVFjlfdpNU)
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('dp_NowVod_GroupList cnt : '+rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpNR)))
  for rTOxgawICeoqHGbsBALPiVFjlfdpNv in rTOxgawICeoqHGbsBALPiVFjlfdpNR:
   rTOxgawICeoqHGbsBALPiVFjlfdpNu =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodTitle')
   rTOxgawICeoqHGbsBALPiVFjlfdpNY =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodId')
   rTOxgawICeoqHGbsBALPiVFjlfdpND =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodType')
   rTOxgawICeoqHGbsBALPiVFjlfdpNn=rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('thumbnail')
   rTOxgawICeoqHGbsBALPiVFjlfdpNQ =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vtypeId')
   rTOxgawICeoqHGbsBALPiVFjlfdpNt =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('duration')
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'mediatype':'episode','duration':rTOxgawICeoqHGbsBALPiVFjlfdpNt,'plot':rTOxgawICeoqHGbsBALPiVFjlfdpNu}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'NOW_VOD','mediacode':rTOxgawICeoqHGbsBALPiVFjlfdpNY,'mediatype':'vod','vtypeId':rTOxgawICeoqHGbsBALPiVFjlfdpNQ}
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpNu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpND,img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkR,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  if rTOxgawICeoqHGbsBALPiVFjlfdpNm:
   rTOxgawICeoqHGbsBALPiVFjlfdpNk['mode'] ='NOW_GROUP' 
   rTOxgawICeoqHGbsBALPiVFjlfdpNk['page'] =rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpNU+1)
   rTOxgawICeoqHGbsBALPiVFjlfdpcu='[B]%s >>[/B]'%'다음 페이지'
   rTOxgawICeoqHGbsBALPiVFjlfdpyc=rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpNU+1)
   rTOxgawICeoqHGbsBALPiVFjlfdpNW=os.path.join(xbmcaddon.Addon().getAddonInfo('path'),'img','next.png')
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpyc,img=rTOxgawICeoqHGbsBALPiVFjlfdpNW,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpkM,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkv,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  xbmcplugin.setContent(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,'episodes')
  xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def dp_PopVod_GroupList(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('dp_PopVod_GroupList ')
  rTOxgawICeoqHGbsBALPiVFjlfdpNR=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetPopularGroupList()
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('dp_PopVod_GroupList cnt : '+rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpNR)))
  for rTOxgawICeoqHGbsBALPiVFjlfdpNv in rTOxgawICeoqHGbsBALPiVFjlfdpNR:
   rTOxgawICeoqHGbsBALPiVFjlfdpNu =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodTitle')
   rTOxgawICeoqHGbsBALPiVFjlfdpNY =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodId')
   rTOxgawICeoqHGbsBALPiVFjlfdpND =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodType')
   rTOxgawICeoqHGbsBALPiVFjlfdpNn=rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('thumbnail')
   rTOxgawICeoqHGbsBALPiVFjlfdpNQ =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vtypeId')
   rTOxgawICeoqHGbsBALPiVFjlfdpNt =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('duration')
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'mediatype':'episode','duration':rTOxgawICeoqHGbsBALPiVFjlfdpNt,'plot':rTOxgawICeoqHGbsBALPiVFjlfdpNu}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'POP_VOD','mediacode':rTOxgawICeoqHGbsBALPiVFjlfdpNY,'mediatype':'vod','vtypeId':rTOxgawICeoqHGbsBALPiVFjlfdpNQ}
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpNu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpND,img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkR,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  xbmcplugin.setContent(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,'episodes')
  xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def dp_Season_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpNh=args.get('reagueId')
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('Season_List - reagueId : '+rTOxgawICeoqHGbsBALPiVFjlfdpNh)
  rTOxgawICeoqHGbsBALPiVFjlfdpNR=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetSeasonList(rTOxgawICeoqHGbsBALPiVFjlfdpNh)
  for rTOxgawICeoqHGbsBALPiVFjlfdpNv in rTOxgawICeoqHGbsBALPiVFjlfdpNR:
   rTOxgawICeoqHGbsBALPiVFjlfdpyE =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('reagueName')
   rTOxgawICeoqHGbsBALPiVFjlfdpyW =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('gameTypeId')
   rTOxgawICeoqHGbsBALPiVFjlfdpyk =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('seasonName')
   rTOxgawICeoqHGbsBALPiVFjlfdpyK =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('seasonId')
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'mediatype':'episode','plot':'%s - %s'%(rTOxgawICeoqHGbsBALPiVFjlfdpyE,rTOxgawICeoqHGbsBALPiVFjlfdpyk)}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'SEASON_GROUP','reagueId':rTOxgawICeoqHGbsBALPiVFjlfdpNh,'seasonId':rTOxgawICeoqHGbsBALPiVFjlfdpyK,'gameTypeId':rTOxgawICeoqHGbsBALPiVFjlfdpyW,'page':'1'}
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpyE,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpyk,img='',infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkv,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  if rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpNR)>0:xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def dp_Game_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpyW=args.get('gameTypeId')
  rTOxgawICeoqHGbsBALPiVFjlfdpNh =args.get('reagueId')
  rTOxgawICeoqHGbsBALPiVFjlfdpyK =args.get('seasonId')
  rTOxgawICeoqHGbsBALPiVFjlfdpNU =rTOxgawICeoqHGbsBALPiVFjlfdpkJ(args.get('page'))
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('Game_List - gameTypeId : '+rTOxgawICeoqHGbsBALPiVFjlfdpyW)
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('Game_List - reagueId   : '+rTOxgawICeoqHGbsBALPiVFjlfdpNh)
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('Game_List - seasonId   : '+rTOxgawICeoqHGbsBALPiVFjlfdpyK)
  rTOxgawICeoqHGbsBALPiVFjlfdpNR,rTOxgawICeoqHGbsBALPiVFjlfdpNm=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetGameList(rTOxgawICeoqHGbsBALPiVFjlfdpyW,rTOxgawICeoqHGbsBALPiVFjlfdpNh,rTOxgawICeoqHGbsBALPiVFjlfdpyK,rTOxgawICeoqHGbsBALPiVFjlfdpNU,hidescore=rTOxgawICeoqHGbsBALPiVFjlfdpck.get_settings_hidescoreyn())
  for rTOxgawICeoqHGbsBALPiVFjlfdpNv in rTOxgawICeoqHGbsBALPiVFjlfdpNR:
   rTOxgawICeoqHGbsBALPiVFjlfdpyX =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('gameTitle')
   rTOxgawICeoqHGbsBALPiVFjlfdpyz =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('beginDate')
   rTOxgawICeoqHGbsBALPiVFjlfdpNn =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('thumbnail')
   rTOxgawICeoqHGbsBALPiVFjlfdpyM =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('gameId')
   rTOxgawICeoqHGbsBALPiVFjlfdpyR =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('totVodCnt')
   rTOxgawICeoqHGbsBALPiVFjlfdpyv =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('leaguenm')
   rTOxgawICeoqHGbsBALPiVFjlfdpyn =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('seasonnm')
   rTOxgawICeoqHGbsBALPiVFjlfdpyh =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('roundnm')
   rTOxgawICeoqHGbsBALPiVFjlfdpyJ =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('info_plot')
   rTOxgawICeoqHGbsBALPiVFjlfdpyS ='%s < %s >'%(rTOxgawICeoqHGbsBALPiVFjlfdpyX,rTOxgawICeoqHGbsBALPiVFjlfdpyz)
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'mediatype':'video','plot':rTOxgawICeoqHGbsBALPiVFjlfdpyJ}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'GAME_VOD_GROUP' if rTOxgawICeoqHGbsBALPiVFjlfdpyR!=0 else 'XXX','saveTitle':rTOxgawICeoqHGbsBALPiVFjlfdpyS,'saveImg':rTOxgawICeoqHGbsBALPiVFjlfdpNn,'saveInfo':rTOxgawICeoqHGbsBALPiVFjlfdpNS['plot'],'gameid':rTOxgawICeoqHGbsBALPiVFjlfdpyM,'totVodCnt':rTOxgawICeoqHGbsBALPiVFjlfdpyR,}
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpyX,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpyz,img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkv,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  if rTOxgawICeoqHGbsBALPiVFjlfdpNm:
   rTOxgawICeoqHGbsBALPiVFjlfdpNk['mode'] ='SEASON_GROUP' 
   rTOxgawICeoqHGbsBALPiVFjlfdpNk['reagueId'] =rTOxgawICeoqHGbsBALPiVFjlfdpNh
   rTOxgawICeoqHGbsBALPiVFjlfdpNk['seasonId'] =rTOxgawICeoqHGbsBALPiVFjlfdpyK
   rTOxgawICeoqHGbsBALPiVFjlfdpNk['gameTypeId']=rTOxgawICeoqHGbsBALPiVFjlfdpyW
   rTOxgawICeoqHGbsBALPiVFjlfdpNk['page'] =rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpNU+1)
   rTOxgawICeoqHGbsBALPiVFjlfdpcu='[B]%s >>[/B]'%'다음 페이지'
   rTOxgawICeoqHGbsBALPiVFjlfdpyc=rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpNU+1)
   rTOxgawICeoqHGbsBALPiVFjlfdpNW=os.path.join(xbmcaddon.Addon().getAddonInfo('path'),'img','next.png')
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpyc,img=rTOxgawICeoqHGbsBALPiVFjlfdpNW,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpkM,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkv,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  if rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpNR)>0:xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def dp_GameVod_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpyU =args.get('gameid')
  rTOxgawICeoqHGbsBALPiVFjlfdpyS=args.get('saveTitle')
  rTOxgawICeoqHGbsBALPiVFjlfdpym =args.get('saveImg')
  rTOxgawICeoqHGbsBALPiVFjlfdpyu =args.get('saveInfo')
  rTOxgawICeoqHGbsBALPiVFjlfdpNR=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetGameVodList(rTOxgawICeoqHGbsBALPiVFjlfdpyU)
  for rTOxgawICeoqHGbsBALPiVFjlfdpNv in rTOxgawICeoqHGbsBALPiVFjlfdpNR:
   rTOxgawICeoqHGbsBALPiVFjlfdpNu =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodTitle')
   rTOxgawICeoqHGbsBALPiVFjlfdpNY =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodId')
   rTOxgawICeoqHGbsBALPiVFjlfdpND =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vodType')
   rTOxgawICeoqHGbsBALPiVFjlfdpNn=rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('thumbnail')
   rTOxgawICeoqHGbsBALPiVFjlfdpNQ =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('vtypeId')
   rTOxgawICeoqHGbsBALPiVFjlfdpNt =rTOxgawICeoqHGbsBALPiVFjlfdpNv.get('duration')
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'mediatype':'episode','duration':rTOxgawICeoqHGbsBALPiVFjlfdpNt,'plot':'%s \n\n %s'%(rTOxgawICeoqHGbsBALPiVFjlfdpNu,rTOxgawICeoqHGbsBALPiVFjlfdpyu)}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'GAME_VOD','saveTitle':rTOxgawICeoqHGbsBALPiVFjlfdpyS,'saveImg':rTOxgawICeoqHGbsBALPiVFjlfdpym,'saveId':rTOxgawICeoqHGbsBALPiVFjlfdpyU,'saveInfo':rTOxgawICeoqHGbsBALPiVFjlfdpyu,'mediacode':rTOxgawICeoqHGbsBALPiVFjlfdpNY,'mediatype':'vod','vtypeId':rTOxgawICeoqHGbsBALPiVFjlfdpNQ}
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpNu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpND,img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkR,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  xbmcplugin.setContent(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,'episodes')
  xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def login_main(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  (rTOxgawICeoqHGbsBALPiVFjlfdpyY,rTOxgawICeoqHGbsBALPiVFjlfdpyD)=rTOxgawICeoqHGbsBALPiVFjlfdpck.get_settings_account()
  if not(rTOxgawICeoqHGbsBALPiVFjlfdpyY and rTOxgawICeoqHGbsBALPiVFjlfdpyD):
   rTOxgawICeoqHGbsBALPiVFjlfdpcR=xbmcgui.Dialog()
   rTOxgawICeoqHGbsBALPiVFjlfdpyQ=rTOxgawICeoqHGbsBALPiVFjlfdpcR.yesno(__language__(30901).encode('utf8'),__language__(30902).encode('utf8'))
   if rTOxgawICeoqHGbsBALPiVFjlfdpyQ==rTOxgawICeoqHGbsBALPiVFjlfdpkv:
    __addon__.openSettings()
    sys.exit()
   else:
    sys.exit()
  if rTOxgawICeoqHGbsBALPiVFjlfdpck.cookiefile_check():return
  if xbmcgui.Window(10000).getProperty('SPOTV_M_LOGINWAIT')=='TRUE':
   rTOxgawICeoqHGbsBALPiVFjlfdpyt=0
   while rTOxgawICeoqHGbsBALPiVFjlfdpkv:
    rTOxgawICeoqHGbsBALPiVFjlfdpyt+=1
    time.sleep(0.05)
    if rTOxgawICeoqHGbsBALPiVFjlfdpyt>600:return
  else:
   xbmcgui.Window(10000).setProperty('SPOTV_M_LOGINWAIT','TRUE')
  rTOxgawICeoqHGbsBALPiVFjlfdpEc=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetCredential_new(rTOxgawICeoqHGbsBALPiVFjlfdpyY,rTOxgawICeoqHGbsBALPiVFjlfdpyD)
  if rTOxgawICeoqHGbsBALPiVFjlfdpEc:rTOxgawICeoqHGbsBALPiVFjlfdpck.cookiefile_save()
  xbmcgui.Window(10000).setProperty('SPOTV_M_LOGINWAIT','FALSE')
  if rTOxgawICeoqHGbsBALPiVFjlfdpEc==rTOxgawICeoqHGbsBALPiVFjlfdpkR:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_noti(__language__(30903).encode('utf8'))
   sys.exit()
 def dp_LiveChannel_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpEN=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetLiveChannelList()
  for rTOxgawICeoqHGbsBALPiVFjlfdpEy in rTOxgawICeoqHGbsBALPiVFjlfdpEN:
   rTOxgawICeoqHGbsBALPiVFjlfdpku =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('id')
   rTOxgawICeoqHGbsBALPiVFjlfdpcu =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('name')
   rTOxgawICeoqHGbsBALPiVFjlfdpNM =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('programName')
   rTOxgawICeoqHGbsBALPiVFjlfdpNn =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('logo')
   rTOxgawICeoqHGbsBALPiVFjlfdpEW=rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('channelepg')
   rTOxgawICeoqHGbsBALPiVFjlfdpEk =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('free')
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'plot':'%s\n\n%s'%(rTOxgawICeoqHGbsBALPiVFjlfdpcu,rTOxgawICeoqHGbsBALPiVFjlfdpEW),'mediatype':'episode',}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'LIVE','mediacode':rTOxgawICeoqHGbsBALPiVFjlfdpku,'free':rTOxgawICeoqHGbsBALPiVFjlfdpEk,'mediatype':'live'}
   if rTOxgawICeoqHGbsBALPiVFjlfdpEk:rTOxgawICeoqHGbsBALPiVFjlfdpcu+=' [free]'
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpNM,img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkR,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  xbmcplugin.setContent(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,'episodes')
  if rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpEN)>0:xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def dp_EventLiveChannel_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpEN,rTOxgawICeoqHGbsBALPiVFjlfdpEK=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetEventLiveList()
  if rTOxgawICeoqHGbsBALPiVFjlfdpEK!=401 and rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpEN)==0:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_noti(__language__(30907).encode('utf8'))
  for rTOxgawICeoqHGbsBALPiVFjlfdpEy in rTOxgawICeoqHGbsBALPiVFjlfdpEN:
   rTOxgawICeoqHGbsBALPiVFjlfdpcu =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('title')
   rTOxgawICeoqHGbsBALPiVFjlfdpNM =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('startTime')
   rTOxgawICeoqHGbsBALPiVFjlfdpNn =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('logo')
   rTOxgawICeoqHGbsBALPiVFjlfdpEk =rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('free')
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'mediatype':'episode','plot':'%s\n\n%s'%(rTOxgawICeoqHGbsBALPiVFjlfdpcu,rTOxgawICeoqHGbsBALPiVFjlfdpNM)}
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'ELIVE','mediacode':rTOxgawICeoqHGbsBALPiVFjlfdpEy.get('liveId'),'free':rTOxgawICeoqHGbsBALPiVFjlfdpEk,'mediatype':'live'}
   if rTOxgawICeoqHGbsBALPiVFjlfdpEk:rTOxgawICeoqHGbsBALPiVFjlfdpcu+=' [free]'
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel=rTOxgawICeoqHGbsBALPiVFjlfdpNM,img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkR,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  xbmcplugin.setContent(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,'episodes')
  if rTOxgawICeoqHGbsBALPiVFjlfdpkU(rTOxgawICeoqHGbsBALPiVFjlfdpEN)>0:xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
  return rTOxgawICeoqHGbsBALPiVFjlfdpEK
 def make_stream_header(rTOxgawICeoqHGbsBALPiVFjlfdpck,rTOxgawICeoqHGbsBALPiVFjlfdpER,cookies):
  rTOxgawICeoqHGbsBALPiVFjlfdpEX=''
  if cookies not in[{},rTOxgawICeoqHGbsBALPiVFjlfdpkM,'']:
   rTOxgawICeoqHGbsBALPiVFjlfdpEz=rTOxgawICeoqHGbsBALPiVFjlfdpkU(cookies)
   for rTOxgawICeoqHGbsBALPiVFjlfdpcD,rTOxgawICeoqHGbsBALPiVFjlfdpEM in cookies.items():
    rTOxgawICeoqHGbsBALPiVFjlfdpEX+='{}={}'.format(rTOxgawICeoqHGbsBALPiVFjlfdpcD,rTOxgawICeoqHGbsBALPiVFjlfdpEM)
    rTOxgawICeoqHGbsBALPiVFjlfdpEz+=-1
    if rTOxgawICeoqHGbsBALPiVFjlfdpEz>0:rTOxgawICeoqHGbsBALPiVFjlfdpEX+='; '
   rTOxgawICeoqHGbsBALPiVFjlfdpER['cookie']=rTOxgawICeoqHGbsBALPiVFjlfdpEX
  rTOxgawICeoqHGbsBALPiVFjlfdpEv=''
  i=0
  for rTOxgawICeoqHGbsBALPiVFjlfdpcD,rTOxgawICeoqHGbsBALPiVFjlfdpEM in rTOxgawICeoqHGbsBALPiVFjlfdpER.items():
   i=i+1
   if i>1:rTOxgawICeoqHGbsBALPiVFjlfdpEv+='&'
   rTOxgawICeoqHGbsBALPiVFjlfdpEv+='{}={}'.format(rTOxgawICeoqHGbsBALPiVFjlfdpcD,urllib.parse.quote(rTOxgawICeoqHGbsBALPiVFjlfdpEM))
  return rTOxgawICeoqHGbsBALPiVFjlfdpEv
 def play_VIDEO(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpEn =args.get('mode')
  rTOxgawICeoqHGbsBALPiVFjlfdpEh =args.get('mediacode')
  rTOxgawICeoqHGbsBALPiVFjlfdpEJ =args.get('mediatype')
  rTOxgawICeoqHGbsBALPiVFjlfdpNQ =args.get('vtypeId')
  if rTOxgawICeoqHGbsBALPiVFjlfdpEn=='LIVE':
   if args.get('free')=='False':
    if rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.CheckSubEnd()==rTOxgawICeoqHGbsBALPiVFjlfdpkR:
     rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_noti(__language__(30908).encode('utf8'))
     return
  elif rTOxgawICeoqHGbsBALPiVFjlfdpEn=='ELIVE':
   if args.get('free')=='False':
    if rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.CheckSubEnd()==rTOxgawICeoqHGbsBALPiVFjlfdpkR:
     rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_noti(__language__(30908).encode('utf8'))
     return
  if rTOxgawICeoqHGbsBALPiVFjlfdpEh=='' or rTOxgawICeoqHGbsBALPiVFjlfdpEh==rTOxgawICeoqHGbsBALPiVFjlfdpkM:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_noti(__language__(30907).encode('utf8'))
   return
  if rTOxgawICeoqHGbsBALPiVFjlfdpEn=='LIVE':
   rTOxgawICeoqHGbsBALPiVFjlfdpES,rTOxgawICeoqHGbsBALPiVFjlfdpEU=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetHlsUrl(rTOxgawICeoqHGbsBALPiVFjlfdpEh)
  else:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('mediacode : '+rTOxgawICeoqHGbsBALPiVFjlfdpEh)
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('mediatype : '+rTOxgawICeoqHGbsBALPiVFjlfdpEJ)
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('vtypeId   : '+rTOxgawICeoqHGbsBALPiVFjlfdpkm(rTOxgawICeoqHGbsBALPiVFjlfdpNQ))
   rTOxgawICeoqHGbsBALPiVFjlfdpES,rTOxgawICeoqHGbsBALPiVFjlfdpEU=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.GetBroadURL(rTOxgawICeoqHGbsBALPiVFjlfdpEh,rTOxgawICeoqHGbsBALPiVFjlfdpEJ,rTOxgawICeoqHGbsBALPiVFjlfdpNQ)
  if rTOxgawICeoqHGbsBALPiVFjlfdpEU=='':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_noti(__language__(30908).encode('utf8'))
   return
  rTOxgawICeoqHGbsBALPiVFjlfdpEm=rTOxgawICeoqHGbsBALPiVFjlfdpEU
  try:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log('mainMode  = '+rTOxgawICeoqHGbsBALPiVFjlfdpEn)
  except:
   rTOxgawICeoqHGbsBALPiVFjlfdpkM
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log(rTOxgawICeoqHGbsBALPiVFjlfdpEm)
  rTOxgawICeoqHGbsBALPiVFjlfdpEu=xbmcgui.ListItem(path=rTOxgawICeoqHGbsBALPiVFjlfdpEm)
  if rTOxgawICeoqHGbsBALPiVFjlfdpEn in['LIVE','ELIVE']:
   rTOxgawICeoqHGbsBALPiVFjlfdpEY={}
   rTOxgawICeoqHGbsBALPiVFjlfdpEY['content-type']='application/octet-stream' 
   rTOxgawICeoqHGbsBALPiVFjlfdpEY['user-agent'] =rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.USER_AGENT
   rTOxgawICeoqHGbsBALPiVFjlfdpED ='https://www.spotvnow.co.kr/drm/widevine/{}/{}'.format(rTOxgawICeoqHGbsBALPiVFjlfdpES,rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.ST['cookies']['spotv_sessionid'])
   rTOxgawICeoqHGbsBALPiVFjlfdpEQ=rTOxgawICeoqHGbsBALPiVFjlfdpED+'|'+urllib.parse.urlencode(rTOxgawICeoqHGbsBALPiVFjlfdpEY)+'|R{SSM}|'
   rTOxgawICeoqHGbsBALPiVFjlfdpEt=rTOxgawICeoqHGbsBALPiVFjlfdpck.make_stream_header(rTOxgawICeoqHGbsBALPiVFjlfdpEY,rTOxgawICeoqHGbsBALPiVFjlfdpkM)
   rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_log(rTOxgawICeoqHGbsBALPiVFjlfdpED)
   inputstreamhelper.Helper('hls',drm='com.widevine.alpha').check_inputstream()
   rTOxgawICeoqHGbsBALPiVFjlfdpEu.setProperty('inputstream','inputstream.adaptive')
   if rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.KodiVersion<=20:
    rTOxgawICeoqHGbsBALPiVFjlfdpEu.setProperty('inputstream.adaptive.manifest_type','hls')
   rTOxgawICeoqHGbsBALPiVFjlfdpEu.setProperty('inputstream.adaptive.license_type','com.widevine.alpha')
   rTOxgawICeoqHGbsBALPiVFjlfdpEu.setProperty('inputstream.adaptive.license_key',rTOxgawICeoqHGbsBALPiVFjlfdpEQ)
   rTOxgawICeoqHGbsBALPiVFjlfdpEu.setProperty('inputstream.adaptive.stream_headers',rTOxgawICeoqHGbsBALPiVFjlfdpEt)
   rTOxgawICeoqHGbsBALPiVFjlfdpEu.setProperty('inputstream.adaptive.manifest_headers',rTOxgawICeoqHGbsBALPiVFjlfdpEt)
  xbmcplugin.setResolvedUrl(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,rTOxgawICeoqHGbsBALPiVFjlfdpkv,rTOxgawICeoqHGbsBALPiVFjlfdpEu)
  try:
   if rTOxgawICeoqHGbsBALPiVFjlfdpEJ=='vod' and rTOxgawICeoqHGbsBALPiVFjlfdpEn not in['POP_VOD','NOW_VOD']:
    rTOxgawICeoqHGbsBALPiVFjlfdpNk={'code':args.get('saveId'),'img':args.get('saveImg'),'title':args.get('saveTitle'),'info':args.get('saveInfo')}
    rTOxgawICeoqHGbsBALPiVFjlfdpck.Save_Watched_List(rTOxgawICeoqHGbsBALPiVFjlfdpEJ,rTOxgawICeoqHGbsBALPiVFjlfdpNk)
  except:
   rTOxgawICeoqHGbsBALPiVFjlfdpkM
 def logout(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  rTOxgawICeoqHGbsBALPiVFjlfdpcR=xbmcgui.Dialog()
  rTOxgawICeoqHGbsBALPiVFjlfdpyQ=rTOxgawICeoqHGbsBALPiVFjlfdpcR.yesno(__language__(30910).encode('utf8'),__language__(30905).encode('utf8'))
  if rTOxgawICeoqHGbsBALPiVFjlfdpyQ==rTOxgawICeoqHGbsBALPiVFjlfdpkR:sys.exit()
  rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Init_ST_Total()
  if os.path.isfile(rTOxgawICeoqHGbsBALPiVFjlfdpcW):os.remove(rTOxgawICeoqHGbsBALPiVFjlfdpcW)
  rTOxgawICeoqHGbsBALPiVFjlfdpck.addon_noti(__language__(30909).encode('utf-8'))
 def cookiefile_save(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  rTOxgawICeoqHGbsBALPiVFjlfdpWN =rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Get_Now_Datetime()
  rTOxgawICeoqHGbsBALPiVFjlfdpWy=rTOxgawICeoqHGbsBALPiVFjlfdpWN+datetime.timedelta(days=0)
  (rTOxgawICeoqHGbsBALPiVFjlfdpyY,rTOxgawICeoqHGbsBALPiVFjlfdpyD)=rTOxgawICeoqHGbsBALPiVFjlfdpck.get_settings_account()
  rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Save_session_acount(rTOxgawICeoqHGbsBALPiVFjlfdpyY,rTOxgawICeoqHGbsBALPiVFjlfdpyD)
  rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.ST['account']['token_limit']=rTOxgawICeoqHGbsBALPiVFjlfdpWy.strftime('%Y%m%d')
  rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.JsonFile_Save(rTOxgawICeoqHGbsBALPiVFjlfdpcW,rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.ST)
 def cookiefile_check(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.ST=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.JsonFile_Load(rTOxgawICeoqHGbsBALPiVFjlfdpcW)
  if 'account' not in rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.ST:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Init_ST_Total()
   return rTOxgawICeoqHGbsBALPiVFjlfdpkR
  (rTOxgawICeoqHGbsBALPiVFjlfdpWE,rTOxgawICeoqHGbsBALPiVFjlfdpWk)=rTOxgawICeoqHGbsBALPiVFjlfdpck.get_settings_account()
  (rTOxgawICeoqHGbsBALPiVFjlfdpWK,rTOxgawICeoqHGbsBALPiVFjlfdpWX)=rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Load_session_acount()
  if rTOxgawICeoqHGbsBALPiVFjlfdpWE!=rTOxgawICeoqHGbsBALPiVFjlfdpWK or rTOxgawICeoqHGbsBALPiVFjlfdpWk!=rTOxgawICeoqHGbsBALPiVFjlfdpWX:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Init_ST_Total()
   return rTOxgawICeoqHGbsBALPiVFjlfdpkR
  if rTOxgawICeoqHGbsBALPiVFjlfdpkJ(rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Get_Now_Datetime().strftime('%Y%m%d'))>rTOxgawICeoqHGbsBALPiVFjlfdpkJ(rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.ST['account']['token_limit']):
   rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.Init_ST_Total()
   return rTOxgawICeoqHGbsBALPiVFjlfdpkR
  return rTOxgawICeoqHGbsBALPiVFjlfdpkv
 def dp_History_Remove(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpWz=args.get('delType')
  rTOxgawICeoqHGbsBALPiVFjlfdpWM =args.get('sKey')
  rTOxgawICeoqHGbsBALPiVFjlfdpWR =args.get('vType')
  rTOxgawICeoqHGbsBALPiVFjlfdpcR=xbmcgui.Dialog()
  if rTOxgawICeoqHGbsBALPiVFjlfdpWz=='WATCH_ALL':
   rTOxgawICeoqHGbsBALPiVFjlfdpyQ=rTOxgawICeoqHGbsBALPiVFjlfdpcR.yesno(__language__(30904).encode('utf8'),__language__(30905).encode('utf8'))
  elif rTOxgawICeoqHGbsBALPiVFjlfdpWz=='WATCH_ONE':
   rTOxgawICeoqHGbsBALPiVFjlfdpyQ=rTOxgawICeoqHGbsBALPiVFjlfdpcR.yesno(__language__(30911).encode('utf8'),__language__(30905).encode('utf8'))
  if rTOxgawICeoqHGbsBALPiVFjlfdpyQ==rTOxgawICeoqHGbsBALPiVFjlfdpkR:sys.exit()
  if rTOxgawICeoqHGbsBALPiVFjlfdpWz=='WATCH_ALL':
   rTOxgawICeoqHGbsBALPiVFjlfdpWv=xbmcvfs.translatePath(os.path.join(__profile__,'watchedlist_%s.txt'%rTOxgawICeoqHGbsBALPiVFjlfdpWR))
   if os.path.isfile(rTOxgawICeoqHGbsBALPiVFjlfdpWv):os.remove(rTOxgawICeoqHGbsBALPiVFjlfdpWv)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpWz=='WATCH_ONE':
   rTOxgawICeoqHGbsBALPiVFjlfdpWv=xbmcvfs.translatePath(os.path.join(__profile__,'watchedlist_%s.txt'%rTOxgawICeoqHGbsBALPiVFjlfdpWR))
   try:
    rTOxgawICeoqHGbsBALPiVFjlfdpWn=rTOxgawICeoqHGbsBALPiVFjlfdpck.Load_List_File(rTOxgawICeoqHGbsBALPiVFjlfdpWR) 
    fp=rTOxgawICeoqHGbsBALPiVFjlfdpkY(rTOxgawICeoqHGbsBALPiVFjlfdpWv,'w',-1,'utf-8')
    for rTOxgawICeoqHGbsBALPiVFjlfdpWh in rTOxgawICeoqHGbsBALPiVFjlfdpWn:
     rTOxgawICeoqHGbsBALPiVFjlfdpWJ=rTOxgawICeoqHGbsBALPiVFjlfdpkD(urllib.parse.parse_qsl(rTOxgawICeoqHGbsBALPiVFjlfdpWh))
     rTOxgawICeoqHGbsBALPiVFjlfdpWS=rTOxgawICeoqHGbsBALPiVFjlfdpWJ.get('code').strip()
     if rTOxgawICeoqHGbsBALPiVFjlfdpWM!=rTOxgawICeoqHGbsBALPiVFjlfdpWS:
      fp.write(rTOxgawICeoqHGbsBALPiVFjlfdpWh)
    fp.close()
   except:
    rTOxgawICeoqHGbsBALPiVFjlfdpkM
  xbmc.executebuiltin("Container.Refresh")
 def Load_List_File(rTOxgawICeoqHGbsBALPiVFjlfdpck,rTOxgawICeoqHGbsBALPiVFjlfdpEJ):
  try:
   rTOxgawICeoqHGbsBALPiVFjlfdpWU=xbmcvfs.translatePath(os.path.join(__profile__,'watchedlist_%s.txt'%rTOxgawICeoqHGbsBALPiVFjlfdpEJ))
   fp=rTOxgawICeoqHGbsBALPiVFjlfdpkY(rTOxgawICeoqHGbsBALPiVFjlfdpWU,'r',-1,'utf-8')
   rTOxgawICeoqHGbsBALPiVFjlfdpWm=fp.readlines()
   fp.close()
  except:
   rTOxgawICeoqHGbsBALPiVFjlfdpWm=[]
  return rTOxgawICeoqHGbsBALPiVFjlfdpWm
 def Save_Watched_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,stype,rTOxgawICeoqHGbsBALPiVFjlfdpcz):
  try:
   rTOxgawICeoqHGbsBALPiVFjlfdpWU=xbmcvfs.translatePath(os.path.join(__profile__,'watchedlist_%s.txt'%stype))
   rTOxgawICeoqHGbsBALPiVFjlfdpWn=rTOxgawICeoqHGbsBALPiVFjlfdpck.Load_List_File(stype) 
   fp=rTOxgawICeoqHGbsBALPiVFjlfdpkY(rTOxgawICeoqHGbsBALPiVFjlfdpWU,'w',-1,'utf-8')
   rTOxgawICeoqHGbsBALPiVFjlfdpWu=urllib.parse.urlencode(rTOxgawICeoqHGbsBALPiVFjlfdpcz)
   rTOxgawICeoqHGbsBALPiVFjlfdpWu=rTOxgawICeoqHGbsBALPiVFjlfdpWu+'\n'
   fp.write(rTOxgawICeoqHGbsBALPiVFjlfdpWu)
   rTOxgawICeoqHGbsBALPiVFjlfdpWY=0
   for rTOxgawICeoqHGbsBALPiVFjlfdpWh in rTOxgawICeoqHGbsBALPiVFjlfdpWn:
    rTOxgawICeoqHGbsBALPiVFjlfdpWJ=rTOxgawICeoqHGbsBALPiVFjlfdpkD(urllib.parse.parse_qsl(rTOxgawICeoqHGbsBALPiVFjlfdpWh))
    rTOxgawICeoqHGbsBALPiVFjlfdpWD=rTOxgawICeoqHGbsBALPiVFjlfdpcz.get('code')
    rTOxgawICeoqHGbsBALPiVFjlfdpWQ=rTOxgawICeoqHGbsBALPiVFjlfdpWJ.get('code')
    if rTOxgawICeoqHGbsBALPiVFjlfdpWD!=rTOxgawICeoqHGbsBALPiVFjlfdpWQ:
     fp.write(rTOxgawICeoqHGbsBALPiVFjlfdpWh)
     rTOxgawICeoqHGbsBALPiVFjlfdpWY+=1
     if rTOxgawICeoqHGbsBALPiVFjlfdpWY>=50:break
   fp.close()
  except:
   rTOxgawICeoqHGbsBALPiVFjlfdpkM
 def dp_Watch_List(rTOxgawICeoqHGbsBALPiVFjlfdpck,args):
  rTOxgawICeoqHGbsBALPiVFjlfdpEJ ='vod'
  if rTOxgawICeoqHGbsBALPiVFjlfdpEJ=='vod':
   rTOxgawICeoqHGbsBALPiVFjlfdpWt=rTOxgawICeoqHGbsBALPiVFjlfdpck.Load_List_File(rTOxgawICeoqHGbsBALPiVFjlfdpEJ)
   for rTOxgawICeoqHGbsBALPiVFjlfdpkc in rTOxgawICeoqHGbsBALPiVFjlfdpWt:
    rTOxgawICeoqHGbsBALPiVFjlfdpkN=rTOxgawICeoqHGbsBALPiVFjlfdpkD(urllib.parse.parse_qsl(rTOxgawICeoqHGbsBALPiVFjlfdpkc))
    rTOxgawICeoqHGbsBALPiVFjlfdpcu =rTOxgawICeoqHGbsBALPiVFjlfdpkN.get('title')
    rTOxgawICeoqHGbsBALPiVFjlfdpNn=rTOxgawICeoqHGbsBALPiVFjlfdpkN.get('img')
    rTOxgawICeoqHGbsBALPiVFjlfdpEh=rTOxgawICeoqHGbsBALPiVFjlfdpkN.get('code')
    rTOxgawICeoqHGbsBALPiVFjlfdpky =rTOxgawICeoqHGbsBALPiVFjlfdpkN.get('info')
    rTOxgawICeoqHGbsBALPiVFjlfdpNS={}
    rTOxgawICeoqHGbsBALPiVFjlfdpNS['plot'] =rTOxgawICeoqHGbsBALPiVFjlfdpky
    rTOxgawICeoqHGbsBALPiVFjlfdpNS['mediatype']='tvshow'
    rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'GAME_VOD_GROUP','gameid':rTOxgawICeoqHGbsBALPiVFjlfdpEh,'saveTitle':rTOxgawICeoqHGbsBALPiVFjlfdpcu,'saveImg':rTOxgawICeoqHGbsBALPiVFjlfdpNn,'saveInfo':rTOxgawICeoqHGbsBALPiVFjlfdpky,'mediatype':rTOxgawICeoqHGbsBALPiVFjlfdpEJ}
    rTOxgawICeoqHGbsBALPiVFjlfdpkE={'mode':'MYVIEW_REMOVE','delType':'WATCH_ONE','sKey':rTOxgawICeoqHGbsBALPiVFjlfdpEh,'vType':rTOxgawICeoqHGbsBALPiVFjlfdpEJ,}
    rTOxgawICeoqHGbsBALPiVFjlfdpkW=urllib.parse.urlencode(rTOxgawICeoqHGbsBALPiVFjlfdpkE)
    rTOxgawICeoqHGbsBALPiVFjlfdpkK=[('선택된 시청이력 ( %s ) 삭제'%(rTOxgawICeoqHGbsBALPiVFjlfdpcu),'RunPlugin(plugin://plugin.video.spotvm/?%s)'%(rTOxgawICeoqHGbsBALPiVFjlfdpkW))]
    rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel='',img=rTOxgawICeoqHGbsBALPiVFjlfdpNn,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkv,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk,ContextMenu=rTOxgawICeoqHGbsBALPiVFjlfdpkK)
   rTOxgawICeoqHGbsBALPiVFjlfdpNS={'plot':'시청목록을 삭제합니다.'}
   rTOxgawICeoqHGbsBALPiVFjlfdpcu='*** 시청목록 삭제 ***'
   rTOxgawICeoqHGbsBALPiVFjlfdpNk={'mode':'MYVIEW_REMOVE','delType':'WATCH_ALL','skey':'-','vType':rTOxgawICeoqHGbsBALPiVFjlfdpEJ,}
   rTOxgawICeoqHGbsBALPiVFjlfdpNW=os.path.join(xbmcaddon.Addon().getAddonInfo('path'),'img','delete.png')
   rTOxgawICeoqHGbsBALPiVFjlfdpck.add_dir(rTOxgawICeoqHGbsBALPiVFjlfdpcu,sublabel='',img=rTOxgawICeoqHGbsBALPiVFjlfdpNW,infoLabels=rTOxgawICeoqHGbsBALPiVFjlfdpNS,isFolder=rTOxgawICeoqHGbsBALPiVFjlfdpkR,params=rTOxgawICeoqHGbsBALPiVFjlfdpNk,isLink=rTOxgawICeoqHGbsBALPiVFjlfdpkv)
   xbmcplugin.endOfDirectory(rTOxgawICeoqHGbsBALPiVFjlfdpck._addon_handle,cacheToDisc=rTOxgawICeoqHGbsBALPiVFjlfdpkR)
 def spotv_main(rTOxgawICeoqHGbsBALPiVFjlfdpck):
  rTOxgawICeoqHGbsBALPiVFjlfdpck.SpotvObj.KodiVersion=rTOxgawICeoqHGbsBALPiVFjlfdpkJ(xbmc.getInfoLabel('System.BuildVersion').split('.')[0])
  rTOxgawICeoqHGbsBALPiVFjlfdpkX=rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params.get('mode',rTOxgawICeoqHGbsBALPiVFjlfdpkM)
  if rTOxgawICeoqHGbsBALPiVFjlfdpkX=='LOGOUT':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.logout()
   return
  rTOxgawICeoqHGbsBALPiVFjlfdpck.login_main()
  if rTOxgawICeoqHGbsBALPiVFjlfdpkX is rTOxgawICeoqHGbsBALPiVFjlfdpkM:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_Main_List()
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='LIVE_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_LiveChannel_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='ELIVE_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpEK=rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_EventLiveChannel_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
   if rTOxgawICeoqHGbsBALPiVFjlfdpEK==401:
    if os.path.isfile(rTOxgawICeoqHGbsBALPiVFjlfdpcW):os.remove(rTOxgawICeoqHGbsBALPiVFjlfdpcW)
    rTOxgawICeoqHGbsBALPiVFjlfdpck.login_main()
    rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_EventLiveChannel_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX in['LIVE','GAME_VOD','POP_VOD','NOW_VOD','ELIVE']:
   rTOxgawICeoqHGbsBALPiVFjlfdpck.play_VIDEO(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='VOD_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_MainLeague_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='NOW_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_NowVod_GroupList(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='POP_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_PopVod_GroupList(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='LEAGUE_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_Season_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='SEASON_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_Game_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='GAME_VOD_GROUP':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_GameVod_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='WATCH':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_Watch_List(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  elif rTOxgawICeoqHGbsBALPiVFjlfdpkX=='MYVIEW_REMOVE':
   rTOxgawICeoqHGbsBALPiVFjlfdpck.dp_History_Remove(rTOxgawICeoqHGbsBALPiVFjlfdpck.main_params)
  else:
   rTOxgawICeoqHGbsBALPiVFjlfdpkM
# Created by pyminifier (https://github.com/liftoff/pyminifier)
