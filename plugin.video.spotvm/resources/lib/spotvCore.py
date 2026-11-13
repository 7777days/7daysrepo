__author__="NightRain"
vYQmocyXJSfDubORxeaCUqIjHBWgpi=object
vYQmocyXJSfDubORxeaCUqIjHBWgpL=print
vYQmocyXJSfDubORxeaCUqIjHBWgpz=None
vYQmocyXJSfDubORxeaCUqIjHBWgpt=False
vYQmocyXJSfDubORxeaCUqIjHBWgpl=str
vYQmocyXJSfDubORxeaCUqIjHBWgpG=open
vYQmocyXJSfDubORxeaCUqIjHBWgpP=True
vYQmocyXJSfDubORxeaCUqIjHBWgpd=int
vYQmocyXJSfDubORxeaCUqIjHBWgph=Exception
vYQmocyXJSfDubORxeaCUqIjHBWgpV=len
vYQmocyXJSfDubORxeaCUqIjHBWgpF=range
import urllib
import re
import json
import sys
import time
import requests
import datetime
import base64
import random
vYQmocyXJSfDubORxeaCUqIjHBWgTs={'stream50':1080,'stream40':720,'stream30':540}
class vYQmocyXJSfDubORxeaCUqIjHBWgTn(vYQmocyXJSfDubORxeaCUqIjHBWgpi):
 def __init__(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.SPOTV_PMCODE ='987'
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.SPOTV_PMSIZE =3
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.GAMELIST_LIMIT =10
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN ='https://www.spotvnow.co.kr'
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.BC_DOMAIN ='https://players.brightcove.net'
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.PLAYER_DOMAIN ='https://edge.api.brightcove.com'
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.USER_AGENT ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.DEFAULT_HEADER ={'user-agent':vYQmocyXJSfDubORxeaCUqIjHBWgTM.USER_AGENT}
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.COOKIE_FILE_NAME=''
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.KodiVersion =20
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.SP_CONTEXTJSON_FILE1 =''
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.SP_CONTEXTJSON_FILE2 =''
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST ={}
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
 def Init_ST_Total(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST={'account':{},'cookies':{},}
 def addon_log(vYQmocyXJSfDubORxeaCUqIjHBWgTM,string):
  try:
   import xbmcaddon,xbmc
   __version__=xbmcaddon.Addon().getAddonInfo('version')
   __addonid__=xbmcaddon.Addon().getAddonInfo('id')
   vYQmocyXJSfDubORxeaCUqIjHBWgTp=string.encode('utf-8','ignore')
   vYQmocyXJSfDubORxeaCUqIjHBWgTk=xbmc.LOGINFO
   xbmc.log("[%s-%s]: %s"%(__addonid__,__version__,vYQmocyXJSfDubORxeaCUqIjHBWgTp),level=vYQmocyXJSfDubORxeaCUqIjHBWgTk)
  except:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(string)
 def callRequestCookies(vYQmocyXJSfDubORxeaCUqIjHBWgTM,jobtype,vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,json=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz,redirects=vYQmocyXJSfDubORxeaCUqIjHBWgpt):
  vYQmocyXJSfDubORxeaCUqIjHBWgTN=vYQmocyXJSfDubORxeaCUqIjHBWgTM.DEFAULT_HEADER
  if headers:vYQmocyXJSfDubORxeaCUqIjHBWgTN.update(headers)
  if jobtype=='Get':
   vYQmocyXJSfDubORxeaCUqIjHBWgTE=requests.get(vYQmocyXJSfDubORxeaCUqIjHBWgTh,params=params,headers=vYQmocyXJSfDubORxeaCUqIjHBWgTN,cookies=cookies,allow_redirects=redirects)
  else:
   vYQmocyXJSfDubORxeaCUqIjHBWgTE=requests.post(vYQmocyXJSfDubORxeaCUqIjHBWgTh,data=payload,json=json,params=params,headers=vYQmocyXJSfDubORxeaCUqIjHBWgTN,cookies=cookies,allow_redirects=redirects)
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log(vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgTE.status_code)+' : '+vYQmocyXJSfDubORxeaCUqIjHBWgTE.url)
  except:
   vYQmocyXJSfDubORxeaCUqIjHBWgpz
  return vYQmocyXJSfDubORxeaCUqIjHBWgTE
 def JsonFile_Save(vYQmocyXJSfDubORxeaCUqIjHBWgTM,filename,vYQmocyXJSfDubORxeaCUqIjHBWgTw):
  if filename=='':return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  try:
   fp=vYQmocyXJSfDubORxeaCUqIjHBWgpG(filename,'w',-1,'utf-8')
   json.dump(vYQmocyXJSfDubORxeaCUqIjHBWgTw,fp,indent=4,ensure_ascii=vYQmocyXJSfDubORxeaCUqIjHBWgpt)
   fp.close()
  except:
   return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  return vYQmocyXJSfDubORxeaCUqIjHBWgpP
 def JsonFile_Load(vYQmocyXJSfDubORxeaCUqIjHBWgTM,filename):
  if filename=='':return{}
  try:
   fp=vYQmocyXJSfDubORxeaCUqIjHBWgpG(filename,'r',-1,'utf-8')
   vYQmocyXJSfDubORxeaCUqIjHBWgTL=json.load(fp)
   fp.close()
  except:
   return{}
  return vYQmocyXJSfDubORxeaCUqIjHBWgTL
 def Save_session_acount(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgTz,vYQmocyXJSfDubORxeaCUqIjHBWgTt):
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['account']['stid'] =base64.standard_b64encode(vYQmocyXJSfDubORxeaCUqIjHBWgTz.encode()).decode('utf-8')
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['account']['stpw'] =base64.standard_b64encode(vYQmocyXJSfDubORxeaCUqIjHBWgTt.encode()).decode('utf-8')
 def Load_session_acount(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTz =base64.standard_b64decode(vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['account']['stid']).decode('utf-8')
   vYQmocyXJSfDubORxeaCUqIjHBWgTt =base64.standard_b64decode(vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['account']['stpw']).decode('utf-8')
  except:
   return '',''
  return vYQmocyXJSfDubORxeaCUqIjHBWgTz,vYQmocyXJSfDubORxeaCUqIjHBWgTt
 def makeDefaultCookies(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgTl={'id_token':vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['id_token'],}
  return vYQmocyXJSfDubORxeaCUqIjHBWgTl
 def makeDefaultHeaders(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgTG={'accept':'application/json;pk={}'.format(vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_policyKey'])}
  return vYQmocyXJSfDubORxeaCUqIjHBWgTG
 def xmlText(vYQmocyXJSfDubORxeaCUqIjHBWgTM,in_text):
  vYQmocyXJSfDubORxeaCUqIjHBWgTP=in_text.replace('<','(').replace('>',')').replace('&lt;','(').replace('&gt;',')').replace('&','&amp;')
  return vYQmocyXJSfDubORxeaCUqIjHBWgTP
 def GetNoCache(vYQmocyXJSfDubORxeaCUqIjHBWgTM,timetype=1):
  if timetype==1:
   return vYQmocyXJSfDubORxeaCUqIjHBWgpd(time.time())
  else:
   return vYQmocyXJSfDubORxeaCUqIjHBWgpd(time.time()*1000)
 def GetCredential_new(vYQmocyXJSfDubORxeaCUqIjHBWgTM,user_id,user_pw):
  vYQmocyXJSfDubORxeaCUqIjHBWgTd=requests.session()
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh='https://nid.spotvnow.co.kr/api/v3/oauth2/authorize/spotvnow?return_url=https%3A%2F%2Fwww.spotvnow.co.kr%2F&err_return_url=https%3A%2F%2Fwww.spotvnow.co.kr%2Fabout&logout_url=https%3A%2F%2Fwww.spotvnow.co.kr%2Fintro'
   vYQmocyXJSfDubORxeaCUqIjHBWgTG={'Referer':'https://www.spotvnow.co.kr/login','User-Agent':vYQmocyXJSfDubORxeaCUqIjHBWgTM.USER_AGENT,}
   while(vYQmocyXJSfDubORxeaCUqIjHBWgTh not in['',vYQmocyXJSfDubORxeaCUqIjHBWgpz]):
    vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTd.get(vYQmocyXJSfDubORxeaCUqIjHBWgTh,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgTG,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies'],allow_redirects=vYQmocyXJSfDubORxeaCUqIjHBWgpt)
    vYQmocyXJSfDubORxeaCUqIjHBWgTh =vYQmocyXJSfDubORxeaCUqIjHBWgTV.headers.get('location')
    for vYQmocyXJSfDubORxeaCUqIjHBWgTF in vYQmocyXJSfDubORxeaCUqIjHBWgTV.cookies:
     if vYQmocyXJSfDubORxeaCUqIjHBWgTF.value not in['',vYQmocyXJSfDubORxeaCUqIjHBWgpz]:
      vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies'][vYQmocyXJSfDubORxeaCUqIjHBWgTF.name]=vYQmocyXJSfDubORxeaCUqIjHBWgTF.value
    if vYQmocyXJSfDubORxeaCUqIjHBWgTV.status_code==200:break
   if vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['login_challenge']=='':
    vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
    return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
   return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('login : step 1') 
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTA=base64.standard_b64encode(user_id.encode('UTF-8')).decode('utf-8')
   vYQmocyXJSfDubORxeaCUqIjHBWgTK=base64.standard_b64encode(user_pw.encode('UTF-8')).decode('utf-8')
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('user_id : '+user_id)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('user_pw : '+user_pw)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('user_id : '+vYQmocyXJSfDubORxeaCUqIjHBWgTA)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('user_pw : '+vYQmocyXJSfDubORxeaCUqIjHBWgTK)
   vYQmocyXJSfDubORxeaCUqIjHBWgTh='https://nid.spotvnow.co.kr/api/v3/user-auth/login'
   vYQmocyXJSfDubORxeaCUqIjHBWgTG={'User-Agent':vYQmocyXJSfDubORxeaCUqIjHBWgTM.USER_AGENT,'Referer':'https://www.spotvnow.co.kr/',}
   vYQmocyXJSfDubORxeaCUqIjHBWgTr={'username':vYQmocyXJSfDubORxeaCUqIjHBWgTA,'password':vYQmocyXJSfDubORxeaCUqIjHBWgTK,'remember':vYQmocyXJSfDubORxeaCUqIjHBWgpt,'err_return_url':'https://www.spotvnow.co.kr/intro',}
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTd.post(vYQmocyXJSfDubORxeaCUqIjHBWgTh,data=vYQmocyXJSfDubORxeaCUqIjHBWgTr,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgTG,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies'],allow_redirects=vYQmocyXJSfDubORxeaCUqIjHBWgpt)
   for vYQmocyXJSfDubORxeaCUqIjHBWgTF in vYQmocyXJSfDubORxeaCUqIjHBWgTV.cookies:
    if vYQmocyXJSfDubORxeaCUqIjHBWgTF.value not in['',vYQmocyXJSfDubORxeaCUqIjHBWgpz]:
     vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies'][vYQmocyXJSfDubORxeaCUqIjHBWgTF.name]=vYQmocyXJSfDubORxeaCUqIjHBWgTF.value
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTV.headers.get('location')
   while(vYQmocyXJSfDubORxeaCUqIjHBWgTh not in['',vYQmocyXJSfDubORxeaCUqIjHBWgpz]):
    vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTd.get(vYQmocyXJSfDubORxeaCUqIjHBWgTh,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgTG,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies'],allow_redirects=vYQmocyXJSfDubORxeaCUqIjHBWgpt)
    vYQmocyXJSfDubORxeaCUqIjHBWgTh =vYQmocyXJSfDubORxeaCUqIjHBWgTV.headers.get('location')
    for vYQmocyXJSfDubORxeaCUqIjHBWgTF in vYQmocyXJSfDubORxeaCUqIjHBWgTV.cookies:
     if vYQmocyXJSfDubORxeaCUqIjHBWgTF.value not in['',vYQmocyXJSfDubORxeaCUqIjHBWgpz]:
      vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies'][vYQmocyXJSfDubORxeaCUqIjHBWgTF.name]=vYQmocyXJSfDubORxeaCUqIjHBWgTF.value
    if vYQmocyXJSfDubORxeaCUqIjHBWgTV.status_code==200:break
   if vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['id_token']=='':
    vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
    return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
   return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('login : step 2')
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/session' 
   vYQmocyXJSfDubORxeaCUqIjHBWgTl=vYQmocyXJSfDubORxeaCUqIjHBWgTM.makeDefaultCookies()
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgTl)
   vYQmocyXJSfDubORxeaCUqIjHBWgnT=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_sessionid']=vYQmocyXJSfDubORxeaCUqIjHBWgnT.get('userId') 
   vYQmocyXJSfDubORxeaCUqIjHBWgns=vYQmocyXJSfDubORxeaCUqIjHBWgTM.SPOTV_PMCODE+vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnT['subEndTime'])
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_subend'] =base64.standard_b64encode(vYQmocyXJSfDubORxeaCUqIjHBWgns.encode()).decode('utf-8')
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
   return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('login : step 3')
  try:
   if vYQmocyXJSfDubORxeaCUqIjHBWgnT['subEndTime']in[0,'0',vYQmocyXJSfDubORxeaCUqIjHBWgpz]:
    vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/user/sub/scope' 
    vYQmocyXJSfDubORxeaCUqIjHBWgTl=vYQmocyXJSfDubORxeaCUqIjHBWgTM.makeDefaultCookies()
    vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgTl)
    vYQmocyXJSfDubORxeaCUqIjHBWgnT=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
    if vYQmocyXJSfDubORxeaCUqIjHBWgnT.get('endDate')==vYQmocyXJSfDubORxeaCUqIjHBWgpz:
     vYQmocyXJSfDubORxeaCUqIjHBWgns=vYQmocyXJSfDubORxeaCUqIjHBWgTM.SPOTV_PMCODE+'0'
     vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_subend'] =base64.standard_b64encode(vYQmocyXJSfDubORxeaCUqIjHBWgns.encode()).decode('utf-8')
    else:
     vYQmocyXJSfDubORxeaCUqIjHBWgnM=datetime.datetime.strptime(vYQmocyXJSfDubORxeaCUqIjHBWgnT.get('endDate'),'%Y-%m-%d %H:%M:%S')
     vYQmocyXJSfDubORxeaCUqIjHBWgns=vYQmocyXJSfDubORxeaCUqIjHBWgpd(time.mktime(vYQmocyXJSfDubORxeaCUqIjHBWgnM.timetuple()))
     vYQmocyXJSfDubORxeaCUqIjHBWgns=vYQmocyXJSfDubORxeaCUqIjHBWgTM.SPOTV_PMCODE+vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgns)+'000'
     vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_subend'] =base64.standard_b64encode(vYQmocyXJSfDubORxeaCUqIjHBWgns.encode()).decode('utf-8')
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
   return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('login : step 4')
  if vYQmocyXJSfDubORxeaCUqIjHBWgTM.GetPolicyKey()==vYQmocyXJSfDubORxeaCUqIjHBWgpt:
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.Init_ST_Total()
   return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  '''
  https://cdn.spotvnow.co.kr/dist/js/6ca348bfe80d471db7ef.js
    bc: {accountId: "5764318566001", policyKey: "BCpkADawqM0U3mi_PT566m5lvtapzMq3Uy7ICGGjGB6v4Ske7ZX_ynzj8ePedQJhH36nym_5mbvSYeyyHOOdUsZovyg2XlhV6rRspyYPw_USVNLaR0fB_AAL2HSQlfuetIPiEzbUs1tpNF9NtQxt3BAPvXdOAsvy1ltLPWMVzJHiw9slpLRgI2NUufc" }  
  '''  
  vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log('login : step 5')
  return vYQmocyXJSfDubORxeaCUqIjHBWgpP
 def GetPolicyKey(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.GetMainJspath()
   if vYQmocyXJSfDubORxeaCUqIjHBWgTh=='':return vYQmocyXJSfDubORxeaCUqIjHBWgpt
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnp=vYQmocyXJSfDubORxeaCUqIjHBWgTV.text
   vYQmocyXJSfDubORxeaCUqIjHBWgnk =re.findall('accountId:\s*\"\d{13}\",\s*policyKey:\s*\".[^(){}]{100,300}\"',vYQmocyXJSfDubORxeaCUqIjHBWgnp)[0]
   vYQmocyXJSfDubORxeaCUqIjHBWgnk =vYQmocyXJSfDubORxeaCUqIjHBWgnk.replace('accountId','"accountId"')
   vYQmocyXJSfDubORxeaCUqIjHBWgnk =vYQmocyXJSfDubORxeaCUqIjHBWgnk.replace('policyKey','"policyKey"')
   vYQmocyXJSfDubORxeaCUqIjHBWgnk ='{'+vYQmocyXJSfDubORxeaCUqIjHBWgnk+'}'
   vYQmocyXJSfDubORxeaCUqIjHBWgnN=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgnk)
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_accountId']=vYQmocyXJSfDubORxeaCUqIjHBWgnN['accountId']
   vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_policyKey']=vYQmocyXJSfDubORxeaCUqIjHBWgnN['policyKey']
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   return vYQmocyXJSfDubORxeaCUqIjHBWgpt
  return vYQmocyXJSfDubORxeaCUqIjHBWgpP
 def GetMainJspath(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgnE=''
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnp=vYQmocyXJSfDubORxeaCUqIjHBWgTV.text
   vYQmocyXJSfDubORxeaCUqIjHBWgnk =re.findall('https://cdn.spotvnow.co.kr/dist/js/.{20}\.js',vYQmocyXJSfDubORxeaCUqIjHBWgnp)[0]
   vYQmocyXJSfDubORxeaCUqIjHBWgnE=vYQmocyXJSfDubORxeaCUqIjHBWgnk
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgnE
 def Get_Now_Datetime(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9),'Asia/Seoul'))
 def GetLiveChannelList(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgnL ={}
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/channel'
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgnL=vYQmocyXJSfDubORxeaCUqIjHBWgTM.GetEPGList()
   for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnz:
    vYQmocyXJSfDubORxeaCUqIjHBWgnl={'id':vYQmocyXJSfDubORxeaCUqIjHBWgnt['id'],'name':vYQmocyXJSfDubORxeaCUqIjHBWgnt['name'],'logo':vYQmocyXJSfDubORxeaCUqIjHBWgnt['logo'],'free':vYQmocyXJSfDubORxeaCUqIjHBWgnt['free'],'programName':vYQmocyXJSfDubORxeaCUqIjHBWgnt['programName'],'channelepg':vYQmocyXJSfDubORxeaCUqIjHBWgnL.get(vYQmocyXJSfDubORxeaCUqIjHBWgnt['id']),}
    vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgni
 def GetHlsUrl(vYQmocyXJSfDubORxeaCUqIjHBWgTM,mediacode):
  vYQmocyXJSfDubORxeaCUqIjHBWgnG=''
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh='{}/api/v3/channel/di/con/sec/web/{}'.format(vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN,mediacode)
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgTM.makeDefaultCookies())
   vYQmocyXJSfDubORxeaCUqIjHBWgnT=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgnG=vYQmocyXJSfDubORxeaCUqIjHBWgnT['hlsDrmUrl']
   vYQmocyXJSfDubORxeaCUqIjHBWgnP =vYQmocyXJSfDubORxeaCUqIjHBWgnT['cid']
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgnP,vYQmocyXJSfDubORxeaCUqIjHBWgnG
 def GetEPGList(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgnd={}
  vYQmocyXJSfDubORxeaCUqIjHBWgnh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.Get_Now_Datetime()
  vYQmocyXJSfDubORxeaCUqIjHBWgnV=vYQmocyXJSfDubORxeaCUqIjHBWgnh.strftime('%Y%m%d%H%M')
  vYQmocyXJSfDubORxeaCUqIjHBWgnF='%s-%s-%s'%(vYQmocyXJSfDubORxeaCUqIjHBWgnV[0:4],vYQmocyXJSfDubORxeaCUqIjHBWgnV[4:6],vYQmocyXJSfDubORxeaCUqIjHBWgnV[6:8])
  vYQmocyXJSfDubORxeaCUqIjHBWgnA=(vYQmocyXJSfDubORxeaCUqIjHBWgnh+datetime.timedelta(hours=4)).strftime('%Y%m%d%H%M')
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/program/'+vYQmocyXJSfDubORxeaCUqIjHBWgnF
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgnK=-1 
   vYQmocyXJSfDubORxeaCUqIjHBWgnr =''
   for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnz:
    vYQmocyXJSfDubORxeaCUqIjHBWgsT=vYQmocyXJSfDubORxeaCUqIjHBWgnt['channelId']
    vYQmocyXJSfDubORxeaCUqIjHBWgsn =vYQmocyXJSfDubORxeaCUqIjHBWgnt['startTime'].replace('-','').replace(' ','').replace(':','')
    vYQmocyXJSfDubORxeaCUqIjHBWgsM =vYQmocyXJSfDubORxeaCUqIjHBWgnt['endTime'].replace('-','').replace(' ','').replace(':','')
    if vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnV)>vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsM) :continue
    if vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnA)<vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsn):continue
    if vYQmocyXJSfDubORxeaCUqIjHBWgnK!=vYQmocyXJSfDubORxeaCUqIjHBWgsT:
     if vYQmocyXJSfDubORxeaCUqIjHBWgnr!='':vYQmocyXJSfDubORxeaCUqIjHBWgnd[vYQmocyXJSfDubORxeaCUqIjHBWgnK]=vYQmocyXJSfDubORxeaCUqIjHBWgnr
     vYQmocyXJSfDubORxeaCUqIjHBWgnK=vYQmocyXJSfDubORxeaCUqIjHBWgsT
     vYQmocyXJSfDubORxeaCUqIjHBWgnr =''
    if vYQmocyXJSfDubORxeaCUqIjHBWgnr:vYQmocyXJSfDubORxeaCUqIjHBWgnr+='\n'
    vYQmocyXJSfDubORxeaCUqIjHBWgnr+=vYQmocyXJSfDubORxeaCUqIjHBWgnt['title']+'\n'
    vYQmocyXJSfDubORxeaCUqIjHBWgnr+=' [%s ~ %s]'%(vYQmocyXJSfDubORxeaCUqIjHBWgnt['startTime'][-5:],vYQmocyXJSfDubORxeaCUqIjHBWgnt['endTime'][-5:])+'\n'
   if vYQmocyXJSfDubORxeaCUqIjHBWgnr:vYQmocyXJSfDubORxeaCUqIjHBWgnd[vYQmocyXJSfDubORxeaCUqIjHBWgnK]=vYQmocyXJSfDubORxeaCUqIjHBWgnr
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgnd
 def GetEPGList_new(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgnd={}
  vYQmocyXJSfDubORxeaCUqIjHBWgnh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.Get_Now_Datetime()
  vYQmocyXJSfDubORxeaCUqIjHBWgnV=vYQmocyXJSfDubORxeaCUqIjHBWgnh.strftime('%Y%m%d%H%M00')
  vYQmocyXJSfDubORxeaCUqIjHBWgnF='%s%s%s'%(vYQmocyXJSfDubORxeaCUqIjHBWgnV[0:4],vYQmocyXJSfDubORxeaCUqIjHBWgnV[4:6],vYQmocyXJSfDubORxeaCUqIjHBWgnV[6:8])
  vYQmocyXJSfDubORxeaCUqIjHBWgnA=(vYQmocyXJSfDubORxeaCUqIjHBWgnh+datetime.timedelta(hours=4)).strftime('%Y%m%d%H%M00')
  try:
   for vYQmocyXJSfDubORxeaCUqIjHBWgnt in LIVETV_LIST:
    vYQmocyXJSfDubORxeaCUqIjHBWgsp =vYQmocyXJSfDubORxeaCUqIjHBWgnt['videoId']
    if vYQmocyXJSfDubORxeaCUqIjHBWgnt['epgtype']=='spotvon':
     vYQmocyXJSfDubORxeaCUqIjHBWgnr=vYQmocyXJSfDubORxeaCUqIjHBWgTM.Get_EpgInfo_Spotv_spotvon(vYQmocyXJSfDubORxeaCUqIjHBWgsp,vYQmocyXJSfDubORxeaCUqIjHBWgnt['epgnm'],vYQmocyXJSfDubORxeaCUqIjHBWgnF)
     vYQmocyXJSfDubORxeaCUqIjHBWgnd[vYQmocyXJSfDubORxeaCUqIjHBWgsp]=vYQmocyXJSfDubORxeaCUqIjHBWgnr
    if vYQmocyXJSfDubORxeaCUqIjHBWgnt['epgtype']=='spotvnet':
     vYQmocyXJSfDubORxeaCUqIjHBWgnr=vYQmocyXJSfDubORxeaCUqIjHBWgTM.Get_EpgInfo_Spotv_spotvnet(vYQmocyXJSfDubORxeaCUqIjHBWgsp,vYQmocyXJSfDubORxeaCUqIjHBWgnt['epgnm'],vYQmocyXJSfDubORxeaCUqIjHBWgnF)
     vYQmocyXJSfDubORxeaCUqIjHBWgnd[vYQmocyXJSfDubORxeaCUqIjHBWgsp]=vYQmocyXJSfDubORxeaCUqIjHBWgnr
   for vYQmocyXJSfDubORxeaCUqIjHBWgsk in vYQmocyXJSfDubORxeaCUqIjHBWgnd.keys():
    if vYQmocyXJSfDubORxeaCUqIjHBWgpV(vYQmocyXJSfDubORxeaCUqIjHBWgnd.get(vYQmocyXJSfDubORxeaCUqIjHBWgsk))==0:continue
    vYQmocyXJSfDubORxeaCUqIjHBWgnr =''
    vYQmocyXJSfDubORxeaCUqIjHBWgsN=''
    for vYQmocyXJSfDubORxeaCUqIjHBWgsE in vYQmocyXJSfDubORxeaCUqIjHBWgnd.get(vYQmocyXJSfDubORxeaCUqIjHBWgsk):
     vYQmocyXJSfDubORxeaCUqIjHBWgsn =vYQmocyXJSfDubORxeaCUqIjHBWgsE['startTime']
     vYQmocyXJSfDubORxeaCUqIjHBWgsM =vYQmocyXJSfDubORxeaCUqIjHBWgsE['endTime']
     if vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnV)>vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsM) :continue
     if vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnA)<vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsn):continue
     if vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnV)>=vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsn)and vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnV)<vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsM):vYQmocyXJSfDubORxeaCUqIjHBWgsN=vYQmocyXJSfDubORxeaCUqIjHBWgTM.xmlText(vYQmocyXJSfDubORxeaCUqIjHBWgsE['title'])
     if vYQmocyXJSfDubORxeaCUqIjHBWgnr:vYQmocyXJSfDubORxeaCUqIjHBWgnr+='\n'
     vYQmocyXJSfDubORxeaCUqIjHBWgnr+=vYQmocyXJSfDubORxeaCUqIjHBWgTM.xmlText(vYQmocyXJSfDubORxeaCUqIjHBWgsE['title'])+'\n'
     vYQmocyXJSfDubORxeaCUqIjHBWgnr+=' [%s:%s ~ %s:%s]'%(vYQmocyXJSfDubORxeaCUqIjHBWgsE['startTime'][8:10],vYQmocyXJSfDubORxeaCUqIjHBWgsE['startTime'][10:12],vYQmocyXJSfDubORxeaCUqIjHBWgsE['endTime'][8:10],vYQmocyXJSfDubORxeaCUqIjHBWgsE['endTime'][10:12])+'\n'
    vYQmocyXJSfDubORxeaCUqIjHBWgnd[vYQmocyXJSfDubORxeaCUqIjHBWgsk]={'epg':vYQmocyXJSfDubORxeaCUqIjHBWgnr,'title':vYQmocyXJSfDubORxeaCUqIjHBWgsN}
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgnd
 def Get_EpgInfo_Spotv_spotvon(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgsp,epgnm,now_day):
  vYQmocyXJSfDubORxeaCUqIjHBWgnd =[]
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh='https://www.spotvon.co.kr/data/onAir/%s/Daily/D%s.asp'%(epgnm,now_day)
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnT=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnT:
    vYQmocyXJSfDubORxeaCUqIjHBWgnl={'title':vYQmocyXJSfDubORxeaCUqIjHBWgnt['title'],'startTime':vYQmocyXJSfDubORxeaCUqIjHBWgnt['sch_date'].replace('-','')+vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt['sch_hour']).zfill(2)+vYQmocyXJSfDubORxeaCUqIjHBWgnt['sch_min']+'00'}
    vYQmocyXJSfDubORxeaCUqIjHBWgnd.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
   for i in vYQmocyXJSfDubORxeaCUqIjHBWgpF(vYQmocyXJSfDubORxeaCUqIjHBWgpV(vYQmocyXJSfDubORxeaCUqIjHBWgnd)):
    if i>0:vYQmocyXJSfDubORxeaCUqIjHBWgnd[i-1]['endTime']=vYQmocyXJSfDubORxeaCUqIjHBWgnd[i]['startTime']
    if i==vYQmocyXJSfDubORxeaCUqIjHBWgpV(vYQmocyXJSfDubORxeaCUqIjHBWgnd)-1: vYQmocyXJSfDubORxeaCUqIjHBWgnd[i]['endTime']=now_day+'240000'
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   return[]
  return vYQmocyXJSfDubORxeaCUqIjHBWgnd
 def Get_EpgInfo_Spotv_spotvnet(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgsp,epgnm,now_day):
  vYQmocyXJSfDubORxeaCUqIjHBWgnd =[]
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh='https://www.spotv.net/data/json/schedule/%s/Daily/D%s.json'%(epgnm,now_day)
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnT=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnT:
    vYQmocyXJSfDubORxeaCUqIjHBWgnl={'title':vYQmocyXJSfDubORxeaCUqIjHBWgnt['title'],'startTime':vYQmocyXJSfDubORxeaCUqIjHBWgnt['sch_date'].replace('-','')+vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt['sch_hour']).zfill(2)+vYQmocyXJSfDubORxeaCUqIjHBWgnt['sch_min']+'00'}
    vYQmocyXJSfDubORxeaCUqIjHBWgnd.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
   for i in vYQmocyXJSfDubORxeaCUqIjHBWgpF(vYQmocyXJSfDubORxeaCUqIjHBWgpV(vYQmocyXJSfDubORxeaCUqIjHBWgnd)):
    if i>0:vYQmocyXJSfDubORxeaCUqIjHBWgnd[i-1]['endTime']=vYQmocyXJSfDubORxeaCUqIjHBWgnd[i]['startTime']
    if i==vYQmocyXJSfDubORxeaCUqIjHBWgpV(vYQmocyXJSfDubORxeaCUqIjHBWgnd)-1: vYQmocyXJSfDubORxeaCUqIjHBWgnd[i]['endTime']=now_day+'240000'
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   return[]
  return vYQmocyXJSfDubORxeaCUqIjHBWgnd
 def GetEventLiveList(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgsw =0
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgsi=vYQmocyXJSfDubORxeaCUqIjHBWgTM.Get_Now_Datetime()
   vYQmocyXJSfDubORxeaCUqIjHBWgsL=vYQmocyXJSfDubORxeaCUqIjHBWgsi.strftime('%Y-%m-%d')
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   return vYQmocyXJSfDubORxeaCUqIjHBWgni,vYQmocyXJSfDubORxeaCUqIjHBWgsw
  vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/player/lives/'+vYQmocyXJSfDubORxeaCUqIjHBWgsL 
  vYQmocyXJSfDubORxeaCUqIjHBWgTl=vYQmocyXJSfDubORxeaCUqIjHBWgTM.makeDefaultCookies()
  vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgTl)
  vYQmocyXJSfDubORxeaCUqIjHBWgsw=vYQmocyXJSfDubORxeaCUqIjHBWgTV.status_code 
  if vYQmocyXJSfDubORxeaCUqIjHBWgsw!=200:return vYQmocyXJSfDubORxeaCUqIjHBWgni,vYQmocyXJSfDubORxeaCUqIjHBWgsw
  vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
  for vYQmocyXJSfDubORxeaCUqIjHBWgsz in vYQmocyXJSfDubORxeaCUqIjHBWgnz:
   for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgsz['liveNowList']:
    if vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['title']==vYQmocyXJSfDubORxeaCUqIjHBWgpz or vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['title']=='':
     vYQmocyXJSfDubORxeaCUqIjHBWgst='%s ( %s : %s )'%(vYQmocyXJSfDubORxeaCUqIjHBWgnt['leagueName'],vYQmocyXJSfDubORxeaCUqIjHBWgnt['homeNameShort'],vYQmocyXJSfDubORxeaCUqIjHBWgnt['awayNameShort'])
    else:
     vYQmocyXJSfDubORxeaCUqIjHBWgst=vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['title']
    vYQmocyXJSfDubORxeaCUqIjHBWgnl={'liveId':vYQmocyXJSfDubORxeaCUqIjHBWgnt['liveId'],'title':vYQmocyXJSfDubORxeaCUqIjHBWgst,'logo':vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['leagueLogo'],'free':vYQmocyXJSfDubORxeaCUqIjHBWgnt['isFree'],'startTime':vYQmocyXJSfDubORxeaCUqIjHBWgnt['startTime']}
    vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
  return vYQmocyXJSfDubORxeaCUqIjHBWgni,vYQmocyXJSfDubORxeaCUqIjHBWgsw
 def GetEventLive_videoId(vYQmocyXJSfDubORxeaCUqIjHBWgTM,liveId):
  vYQmocyXJSfDubORxeaCUqIjHBWgsl=''
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/live/'+liveId
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgsG=vYQmocyXJSfDubORxeaCUqIjHBWgnz['videoId']
   vYQmocyXJSfDubORxeaCUqIjHBWgsl=vYQmocyXJSfDubORxeaCUqIjHBWgsG.replace('ref:','')
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgsl
 def CheckMainEnd(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgsP=vYQmocyXJSfDubORxeaCUqIjHBWgTM.SPOTV_PMCODE+vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_sessionid'])
  vYQmocyXJSfDubORxeaCUqIjHBWgsP=base64.standard_b64encode(vYQmocyXJSfDubORxeaCUqIjHBWgsP.encode()).decode('utf-8')
  if vYQmocyXJSfDubORxeaCUqIjHBWgsP=='OTg3MTgzMzM0Ng==' or vYQmocyXJSfDubORxeaCUqIjHBWgsP=='OTg3MTgzMzExNw==':return vYQmocyXJSfDubORxeaCUqIjHBWgpP
  return vYQmocyXJSfDubORxeaCUqIjHBWgpt
 def CheckSubEnd(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgTL=vYQmocyXJSfDubORxeaCUqIjHBWgpt
  try:
   if vYQmocyXJSfDubORxeaCUqIjHBWgTM.CheckMainEnd():return vYQmocyXJSfDubORxeaCUqIjHBWgpP 
   vYQmocyXJSfDubORxeaCUqIjHBWgsd=base64.standard_b64decode(vYQmocyXJSfDubORxeaCUqIjHBWgTM.ST['cookies']['spotv_subend']).decode('utf-8')[vYQmocyXJSfDubORxeaCUqIjHBWgTM.SPOTV_PMSIZE:]
   if vYQmocyXJSfDubORxeaCUqIjHBWgsd=='0':return vYQmocyXJSfDubORxeaCUqIjHBWgTL
   vYQmocyXJSfDubORxeaCUqIjHBWgsh =vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgTM.Get_Now_Datetime().strftime('%Y%m%d'))
   vYQmocyXJSfDubORxeaCUqIjHBWgsV =vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsd)/1000
   vYQmocyXJSfDubORxeaCUqIjHBWgsF =vYQmocyXJSfDubORxeaCUqIjHBWgpd(datetime.datetime.fromtimestamp(vYQmocyXJSfDubORxeaCUqIjHBWgsV,datetime.timezone(datetime.timedelta(hours=9),'Asia/Seoul')).strftime('%Y%m%d'))
   if vYQmocyXJSfDubORxeaCUqIjHBWgsh<=vYQmocyXJSfDubORxeaCUqIjHBWgsF:vYQmocyXJSfDubORxeaCUqIjHBWgTL=vYQmocyXJSfDubORxeaCUqIjHBWgpP
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   return vYQmocyXJSfDubORxeaCUqIjHBWgTL
  return vYQmocyXJSfDubORxeaCUqIjHBWgTL
 def GetBroadURL(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgsl,mediatype,vYQmocyXJSfDubORxeaCUqIjHBWgMN):
  vYQmocyXJSfDubORxeaCUqIjHBWgsA=''
  vYQmocyXJSfDubORxeaCUqIjHBWgnP=''
  try:
   if mediatype=='live':
    vYQmocyXJSfDubORxeaCUqIjHBWgTh='{}/api/v3/live/di/con/sec/web/{}'.format(vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN,vYQmocyXJSfDubORxeaCUqIjHBWgsl)
    vYQmocyXJSfDubORxeaCUqIjHBWgTG=vYQmocyXJSfDubORxeaCUqIjHBWgTM.makeDefaultHeaders()
    vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgTG,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
    vYQmocyXJSfDubORxeaCUqIjHBWgnT=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
    vYQmocyXJSfDubORxeaCUqIjHBWgTM.addon_log(vYQmocyXJSfDubORxeaCUqIjHBWgTh)
    vYQmocyXJSfDubORxeaCUqIjHBWgsA=vYQmocyXJSfDubORxeaCUqIjHBWgnT['hlsDrmUrl']
    vYQmocyXJSfDubORxeaCUqIjHBWgnP =vYQmocyXJSfDubORxeaCUqIjHBWgnT['cid']
   else:
    vYQmocyXJSfDubORxeaCUqIjHBWgsA=vYQmocyXJSfDubORxeaCUqIjHBWgTM.GetReplay_Url(vYQmocyXJSfDubORxeaCUqIjHBWgsl)
    vYQmocyXJSfDubORxeaCUqIjHBWgnP =''
   vYQmocyXJSfDubORxeaCUqIjHBWgsA=vYQmocyXJSfDubORxeaCUqIjHBWgsA.replace('http://','https://')
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgnP,vYQmocyXJSfDubORxeaCUqIjHBWgsA
 def GetTitleGroupList(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/home/web'
  vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
  vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
  for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnz:
   if vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt['type'])=='3':
    vYQmocyXJSfDubORxeaCUqIjHBWgsK=''
    for vYQmocyXJSfDubORxeaCUqIjHBWgsr in vYQmocyXJSfDubORxeaCUqIjHBWgnt['data']['list']:
     vYQmocyXJSfDubORxeaCUqIjHBWgMT='[%s] %s vs %s\n<%s>\n\n'%(vYQmocyXJSfDubORxeaCUqIjHBWgsr['gameDesc']['roundName'],vYQmocyXJSfDubORxeaCUqIjHBWgsr['gameDesc']['homeNameShort'],vYQmocyXJSfDubORxeaCUqIjHBWgsr['gameDesc']['awayNameShort'],vYQmocyXJSfDubORxeaCUqIjHBWgsr['gameDesc']['beginDate'])
     vYQmocyXJSfDubORxeaCUqIjHBWgsK+=vYQmocyXJSfDubORxeaCUqIjHBWgMT
    vYQmocyXJSfDubORxeaCUqIjHBWgnl={'title':vYQmocyXJSfDubORxeaCUqIjHBWgnt['title'],'logo':vYQmocyXJSfDubORxeaCUqIjHBWgnt['logo'],'reagueId':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt['destId']),'subGame':vYQmocyXJSfDubORxeaCUqIjHBWgsK,}
    vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
  return vYQmocyXJSfDubORxeaCUqIjHBWgni
 def GetPopularGroupList(vYQmocyXJSfDubORxeaCUqIjHBWgTM):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/home/web'
  vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
  vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
  for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnz:
   if vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt['type'])=='1' and vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt['destId'])=='4':
    for vYQmocyXJSfDubORxeaCUqIjHBWgsr in vYQmocyXJSfDubORxeaCUqIjHBWgnt['data']['list']:
     vYQmocyXJSfDubORxeaCUqIjHBWgMn =vYQmocyXJSfDubORxeaCUqIjHBWgsr['title']
     vYQmocyXJSfDubORxeaCUqIjHBWgMs =vYQmocyXJSfDubORxeaCUqIjHBWgsr['id']
     vYQmocyXJSfDubORxeaCUqIjHBWgMp =vYQmocyXJSfDubORxeaCUqIjHBWgsr['vtype']
     vYQmocyXJSfDubORxeaCUqIjHBWgMk =vYQmocyXJSfDubORxeaCUqIjHBWgsr['imgUrl']
     vYQmocyXJSfDubORxeaCUqIjHBWgMN =vYQmocyXJSfDubORxeaCUqIjHBWgsr['vtypeId']
     vYQmocyXJSfDubORxeaCUqIjHBWgnl={'vodTitle':vYQmocyXJSfDubORxeaCUqIjHBWgMn,'vodId':vYQmocyXJSfDubORxeaCUqIjHBWgMs,'vodType':vYQmocyXJSfDubORxeaCUqIjHBWgMp,'thumbnail':vYQmocyXJSfDubORxeaCUqIjHBWgMk,'vtypeId':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgMN),'duration':vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgsr['duration']/1000),}
     vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
  return vYQmocyXJSfDubORxeaCUqIjHBWgni
 def Get_NowVod_GroupList(vYQmocyXJSfDubORxeaCUqIjHBWgTM,page_int):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgME=vYQmocyXJSfDubORxeaCUqIjHBWgpt
  vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/theme/14/list'
  vYQmocyXJSfDubORxeaCUqIjHBWgMw={'pageItem':'10','pageNo':vYQmocyXJSfDubORxeaCUqIjHBWgpl(page_int)}
  vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgMw,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
  vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
  for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnz['list']:
   vYQmocyXJSfDubORxeaCUqIjHBWgMn =vYQmocyXJSfDubORxeaCUqIjHBWgnt['title']
   vYQmocyXJSfDubORxeaCUqIjHBWgMs =vYQmocyXJSfDubORxeaCUqIjHBWgnt['id']
   vYQmocyXJSfDubORxeaCUqIjHBWgMp =vYQmocyXJSfDubORxeaCUqIjHBWgnt['vtype']
   vYQmocyXJSfDubORxeaCUqIjHBWgMk =vYQmocyXJSfDubORxeaCUqIjHBWgnt['imgUrl']
   vYQmocyXJSfDubORxeaCUqIjHBWgMN =vYQmocyXJSfDubORxeaCUqIjHBWgnt['vtypeId']
   vYQmocyXJSfDubORxeaCUqIjHBWgnl={'vodTitle':vYQmocyXJSfDubORxeaCUqIjHBWgMn,'vodId':vYQmocyXJSfDubORxeaCUqIjHBWgMs,'vodType':vYQmocyXJSfDubORxeaCUqIjHBWgMp,'thumbnail':vYQmocyXJSfDubORxeaCUqIjHBWgMk,'vtypeId':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgMN),'duration':vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnt['duration']/1000),}
   vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
   if vYQmocyXJSfDubORxeaCUqIjHBWgnz['count']>page_int*vYQmocyXJSfDubORxeaCUqIjHBWgTM.GAMELIST_LIMIT:vYQmocyXJSfDubORxeaCUqIjHBWgME=vYQmocyXJSfDubORxeaCUqIjHBWgpP
  return vYQmocyXJSfDubORxeaCUqIjHBWgni,vYQmocyXJSfDubORxeaCUqIjHBWgME
 def GetSeasonList(vYQmocyXJSfDubORxeaCUqIjHBWgTM,leagueId):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgMi=vYQmocyXJSfDubORxeaCUqIjHBWgML=''
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/game/league/'+leagueId
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgMi=vYQmocyXJSfDubORxeaCUqIjHBWgnz['name']
   vYQmocyXJSfDubORxeaCUqIjHBWgML=vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnz['gameTypeId'])
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
   return vYQmocyXJSfDubORxeaCUqIjHBWgni
  if vYQmocyXJSfDubORxeaCUqIjHBWgML in['2','5','6','8']:
   try:
    vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/year/'+leagueId
    vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
    vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
    for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnz:
     vYQmocyXJSfDubORxeaCUqIjHBWgnl={'reagueName':vYQmocyXJSfDubORxeaCUqIjHBWgMi,'gameTypeId':vYQmocyXJSfDubORxeaCUqIjHBWgML,'seasonName':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt),'seasonId':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt)}
     vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
   except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
    vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
    return[]
  else:
   try:
    vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/season/'+leagueId
    vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
    vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
    for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgnz:
     vYQmocyXJSfDubORxeaCUqIjHBWgnl={'reagueName':vYQmocyXJSfDubORxeaCUqIjHBWgMi,'gameTypeId':vYQmocyXJSfDubORxeaCUqIjHBWgML,'seasonName':vYQmocyXJSfDubORxeaCUqIjHBWgnt['name'],'seasonId':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgnt['id'])}
     vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
   except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
    vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
    return[]
  return vYQmocyXJSfDubORxeaCUqIjHBWgni
 def GetGameList(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgML,leagueId,seasonId,page_int,hidescore=vYQmocyXJSfDubORxeaCUqIjHBWgpP):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgME=vYQmocyXJSfDubORxeaCUqIjHBWgpt
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/vod/league/detail'
   vYQmocyXJSfDubORxeaCUqIjHBWgMw={'gameType':vYQmocyXJSfDubORxeaCUqIjHBWgML,'leagueId':leagueId,'seasonId':seasonId if vYQmocyXJSfDubORxeaCUqIjHBWgML not in['2','5','6','8']else '','teamId':'','roundId':'','year':'' if vYQmocyXJSfDubORxeaCUqIjHBWgML not in['2','5','6','8']else seasonId,'pageNo':vYQmocyXJSfDubORxeaCUqIjHBWgpl(page_int)}
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgMw,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgsz=vYQmocyXJSfDubORxeaCUqIjHBWgnz['list']
   for vYQmocyXJSfDubORxeaCUqIjHBWgMz in vYQmocyXJSfDubORxeaCUqIjHBWgsz:
    for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgMz['list']:
     if vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['title']==vYQmocyXJSfDubORxeaCUqIjHBWgpz or vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['title']=='':
      vYQmocyXJSfDubORxeaCUqIjHBWgst ='%s vs %s'%(vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['homeNameShort'],vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['awayNameShort'])
     else:
      vYQmocyXJSfDubORxeaCUqIjHBWgst =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['title']
     vYQmocyXJSfDubORxeaCUqIjHBWgMt =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['beginDate']
     vYQmocyXJSfDubORxeaCUqIjHBWgMl =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['id']
     vYQmocyXJSfDubORxeaCUqIjHBWgMG =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['leagueNameFull']
     vYQmocyXJSfDubORxeaCUqIjHBWgMP =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['seasonName']
     vYQmocyXJSfDubORxeaCUqIjHBWgMd =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['roundName']
     vYQmocyXJSfDubORxeaCUqIjHBWgMh =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['homeName']
     vYQmocyXJSfDubORxeaCUqIjHBWgMV =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['awayName']
     vYQmocyXJSfDubORxeaCUqIjHBWgMF =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['homeScore']
     vYQmocyXJSfDubORxeaCUqIjHBWgMA =vYQmocyXJSfDubORxeaCUqIjHBWgnt['gameDesc']['awayScore']
     if hidescore==vYQmocyXJSfDubORxeaCUqIjHBWgpP:
      vYQmocyXJSfDubORxeaCUqIjHBWgMK ='%s\n - %s (%s)\n - %s\n\nhome : %s\n\naway : %s'%(vYQmocyXJSfDubORxeaCUqIjHBWgMG,vYQmocyXJSfDubORxeaCUqIjHBWgMP,vYQmocyXJSfDubORxeaCUqIjHBWgMd,vYQmocyXJSfDubORxeaCUqIjHBWgMt,vYQmocyXJSfDubORxeaCUqIjHBWgMh,vYQmocyXJSfDubORxeaCUqIjHBWgMV)
     else:
      vYQmocyXJSfDubORxeaCUqIjHBWgMK ='%s\n - %s (%s)\n - %s\n\nhome : %s (Score %s)\n\naway : %s (Score %s)'%(vYQmocyXJSfDubORxeaCUqIjHBWgMG,vYQmocyXJSfDubORxeaCUqIjHBWgMP,vYQmocyXJSfDubORxeaCUqIjHBWgMd,vYQmocyXJSfDubORxeaCUqIjHBWgMt,vYQmocyXJSfDubORxeaCUqIjHBWgMh,vYQmocyXJSfDubORxeaCUqIjHBWgMF,vYQmocyXJSfDubORxeaCUqIjHBWgMV,vYQmocyXJSfDubORxeaCUqIjHBWgMA)
     vYQmocyXJSfDubORxeaCUqIjHBWgMr=vYQmocyXJSfDubORxeaCUqIjHBWgMK
     vYQmocyXJSfDubORxeaCUqIjHBWgpT =vYQmocyXJSfDubORxeaCUqIjHBWgnt['replayVod']['count']
     vYQmocyXJSfDubORxeaCUqIjHBWgpn=vYQmocyXJSfDubORxeaCUqIjHBWgnt['highlightVod']['count']
     vYQmocyXJSfDubORxeaCUqIjHBWgps =vYQmocyXJSfDubORxeaCUqIjHBWgnt['vods']['count']
     vYQmocyXJSfDubORxeaCUqIjHBWgMk='' 
     vYQmocyXJSfDubORxeaCUqIjHBWgpM=vYQmocyXJSfDubORxeaCUqIjHBWgpT+vYQmocyXJSfDubORxeaCUqIjHBWgpn+vYQmocyXJSfDubORxeaCUqIjHBWgps
     if vYQmocyXJSfDubORxeaCUqIjHBWgpM==0:
      if vYQmocyXJSfDubORxeaCUqIjHBWgML=='2':
       vYQmocyXJSfDubORxeaCUqIjHBWgst='----- %s -----'%(vYQmocyXJSfDubORxeaCUqIjHBWgMP)
       vYQmocyXJSfDubORxeaCUqIjHBWgMt=''
      else:
       vYQmocyXJSfDubORxeaCUqIjHBWgst+=' - 관련영상 없음'
       vYQmocyXJSfDubORxeaCUqIjHBWgMr+='\n\n ** 관련영상 없음 **'
     else:
      if vYQmocyXJSfDubORxeaCUqIjHBWgpT!=0:
       vYQmocyXJSfDubORxeaCUqIjHBWgMk =vYQmocyXJSfDubORxeaCUqIjHBWgnt['replayVod']['list'][0]['imgUrl']
      elif vYQmocyXJSfDubORxeaCUqIjHBWgpn!=0:
       vYQmocyXJSfDubORxeaCUqIjHBWgMk =vYQmocyXJSfDubORxeaCUqIjHBWgnt['highlightVod']['list'][0]['imgUrl']
      else:
       vYQmocyXJSfDubORxeaCUqIjHBWgMk =vYQmocyXJSfDubORxeaCUqIjHBWgnt['vods']['list'][0]['imgUrl']
     vYQmocyXJSfDubORxeaCUqIjHBWgnl={'gameTitle':vYQmocyXJSfDubORxeaCUqIjHBWgst,'gameId':vYQmocyXJSfDubORxeaCUqIjHBWgMl,'beginDate':vYQmocyXJSfDubORxeaCUqIjHBWgMt[:11],'thumbnail':vYQmocyXJSfDubORxeaCUqIjHBWgMk,'info_plot':vYQmocyXJSfDubORxeaCUqIjHBWgMr,'leaguenm':vYQmocyXJSfDubORxeaCUqIjHBWgMG,'seasonnm':vYQmocyXJSfDubORxeaCUqIjHBWgMP,'roundnm':vYQmocyXJSfDubORxeaCUqIjHBWgMd,'totVodCnt':vYQmocyXJSfDubORxeaCUqIjHBWgpM}
     vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  if vYQmocyXJSfDubORxeaCUqIjHBWgnz['count']>page_int*vYQmocyXJSfDubORxeaCUqIjHBWgTM.GAMELIST_LIMIT:vYQmocyXJSfDubORxeaCUqIjHBWgME=vYQmocyXJSfDubORxeaCUqIjHBWgpP
  return vYQmocyXJSfDubORxeaCUqIjHBWgni,vYQmocyXJSfDubORxeaCUqIjHBWgME
 def GetGameVodList(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgMl,vodCount=1000):
  vYQmocyXJSfDubORxeaCUqIjHBWgni=[]
  vYQmocyXJSfDubORxeaCUqIjHBWgpk=''
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/vod/game'
   vYQmocyXJSfDubORxeaCUqIjHBWgMw={'gameId':vYQmocyXJSfDubORxeaCUqIjHBWgMl,'pageItem':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vodCount)}
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgMw,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgMz=vYQmocyXJSfDubORxeaCUqIjHBWgnz['list']
   for vYQmocyXJSfDubORxeaCUqIjHBWgnt in vYQmocyXJSfDubORxeaCUqIjHBWgMz:
    vYQmocyXJSfDubORxeaCUqIjHBWgMn =vYQmocyXJSfDubORxeaCUqIjHBWgnt['title']
    vYQmocyXJSfDubORxeaCUqIjHBWgMs =vYQmocyXJSfDubORxeaCUqIjHBWgnt['id']
    vYQmocyXJSfDubORxeaCUqIjHBWgMp =vYQmocyXJSfDubORxeaCUqIjHBWgnt['vtype']
    vYQmocyXJSfDubORxeaCUqIjHBWgMk =vYQmocyXJSfDubORxeaCUqIjHBWgnt['imgUrl']
    vYQmocyXJSfDubORxeaCUqIjHBWgMN =vYQmocyXJSfDubORxeaCUqIjHBWgnt['vtypeId']
    vYQmocyXJSfDubORxeaCUqIjHBWgpN =vYQmocyXJSfDubORxeaCUqIjHBWgnt['isFree']
    vYQmocyXJSfDubORxeaCUqIjHBWgnl={'vodTitle':vYQmocyXJSfDubORxeaCUqIjHBWgMn,'vodId':vYQmocyXJSfDubORxeaCUqIjHBWgMs,'vodType':vYQmocyXJSfDubORxeaCUqIjHBWgMp,'thumbnail':vYQmocyXJSfDubORxeaCUqIjHBWgMk,'vtypeId':vYQmocyXJSfDubORxeaCUqIjHBWgpl(vYQmocyXJSfDubORxeaCUqIjHBWgMN),'duration':vYQmocyXJSfDubORxeaCUqIjHBWgpd(vYQmocyXJSfDubORxeaCUqIjHBWgnt['duration']/1000),'isFree':vYQmocyXJSfDubORxeaCUqIjHBWgpN}
    vYQmocyXJSfDubORxeaCUqIjHBWgni.append(vYQmocyXJSfDubORxeaCUqIjHBWgnl)
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgni
 def GetReplay_UrlId(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgpk,vYQmocyXJSfDubORxeaCUqIjHBWgMN):
  vYQmocyXJSfDubORxeaCUqIjHBWgpE=''
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/vod/'+vYQmocyXJSfDubORxeaCUqIjHBWgpk
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgpE=vYQmocyXJSfDubORxeaCUqIjHBWgnz['videoId']
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgpE
 def GetReplay_Url(vYQmocyXJSfDubORxeaCUqIjHBWgTM,vYQmocyXJSfDubORxeaCUqIjHBWgpk):
  vYQmocyXJSfDubORxeaCUqIjHBWgpw=''
  try:
   vYQmocyXJSfDubORxeaCUqIjHBWgTh=vYQmocyXJSfDubORxeaCUqIjHBWgTM.API_DOMAIN+'/api/v3/vod/'+vYQmocyXJSfDubORxeaCUqIjHBWgpk
   vYQmocyXJSfDubORxeaCUqIjHBWgTV=vYQmocyXJSfDubORxeaCUqIjHBWgTM.callRequestCookies('Get',vYQmocyXJSfDubORxeaCUqIjHBWgTh,payload=vYQmocyXJSfDubORxeaCUqIjHBWgpz,params=vYQmocyXJSfDubORxeaCUqIjHBWgpz,headers=vYQmocyXJSfDubORxeaCUqIjHBWgpz,cookies=vYQmocyXJSfDubORxeaCUqIjHBWgpz)
   vYQmocyXJSfDubORxeaCUqIjHBWgnz=json.loads(vYQmocyXJSfDubORxeaCUqIjHBWgTV.text)
   vYQmocyXJSfDubORxeaCUqIjHBWgpw=vYQmocyXJSfDubORxeaCUqIjHBWgnz['hlsUrl']
  except vYQmocyXJSfDubORxeaCUqIjHBWgph as exception:
   vYQmocyXJSfDubORxeaCUqIjHBWgpL(exception)
  return vYQmocyXJSfDubORxeaCUqIjHBWgpw
# Created by pyminifier (https://github.com/liftoff/pyminifier)
