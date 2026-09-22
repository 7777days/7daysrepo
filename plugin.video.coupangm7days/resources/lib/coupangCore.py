_Bw='{}/api-discover/v2/discover/channels/{}/feed'
_Bv='{}/api-discover/v2/sports/leagues/{}/schedule/previous'
_Bu='Live-Sports-Matches'
_Bt='Live-Events-Curation'
_Bs='SP_FEED_LIVE'
_Br='{}/api-discover/v1/discover/sports/leagues/{}/feed'
_Bq='league_id'
_Bp='x-title-streamable'
_Bo='x-title-region'
_Bn='x-title-deal-id'
_Bm='x-title-brightcove-id'
_Bl='x-title-downloadable'
_Bk='x-title-availability'
_Bj='x-title-age-rating'
_Bi='titleType'
_Bh='/api-discover/v1/discover/titles/'
_Bg='description'
_Bf='Explores-Categories'
_Be='ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
_Bd='bm_sv_ex ok'
_Bc='pageProps'
_Bb='Sec-ch-ua'
_Ba='application/json'
_BZ='licenseKey'
_BY='accountID'
_BX='Accept-Language'
_BW='%Y-%m-%dT%H:%M'
_BV='https://www.coupangplay.com'
_BU='theme_mode'
_BT='prime_status'
_BS='NEXT_LOCALE'
_BR='_ga_WS2DFNF7E6'
_BQ='event_id'
_BP='SP_FEED_GAME'
_BO='{} <{}>'
_BN='SP_FEED_TOP10'
_BM='top10'
_BL='preTitle'
_BK='sub_type'
_BJ='startAt'
_BI='x-profileType'
_BH='x-profileId'
_BG='x-force-raw'
_BF='/api/playback/play'
_BE='/api-discover/v1/discover/events/'
_BD='totalPages'
_BC='pagination'
_BB='genreList'
_BA='movies'
_B9='MOVIES'
_B8='TVSHOWS'
_B7='accept-language'
_B6='accept'
_B5='u=0, i'
_B4='priority'
_B3='pragma'
_B2='ko-KR,ko;q=0.9'
_B1='Upgrade-Insecure-Requests'
_B0='Sec-Fetch-User'
_A_='Sec-Fetch-Site'
_Az='Sec-Fetch-Mode'
_Ay='Sec-Fetch-Dest'
_Ax='Sec-Ch-Ua-Platform'
_Aw='Sec-Ch-Ua-Mobile'
_Av='%Y-%m-%d'
_Au='channels'
_At='title_treatment_url'
_As='hero_url'
_Ar='application/x-mpegURL'
_Aq='titleId'
_Ap='meta'
_Ao='tags'
_An='standard'
_Am='/api-discover/v3/discover/feed'
_Al='pre_title'
_Ak='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
_Aj='cache-control'
_Ai='detail'
_Ah='x-nr-session-id'
_Ag='x-device-os-version'
_Af='x-device-id'
_Ae='navigate'
_Ad='document'
_Ac='"Windows"'
_Ab='cookie'
_Aa='application/dash+xml'
_AZ='releaseYear'
_AY='?imwidth=300'
_AX='includeChannelContents'
_AW='collectionId'
_AV='home'
_AU='ALL'
_AT='bm_sv_ex'
_AS='x-app-version'
_AR='poster_url'
_AQ='undefined'
_AP='streamable'
_AO='deal_id'
_AN='asset_id'
_AM='age_rating'
_AL='clearlogo'
_AK='title-treatment'
_AJ='shouldIncludeTVOD'
_AI='error'
_AH='session_web_id'
_AG='device_id'
_AF='obj_id'
_AE='license_url'
_AD='year'
_AC='mpaa'
_AB='preferMultiHeroMixedContentRow'
_AA='preferRecoFeed'
_A9='no-cache'
_A8='ACCOUNT'
_A7='user-agent'
_A6='participants'
_A5='preText'
_A4='asis'
_A3='text'
_A2='?imwidth=350'
_A1='x-profileid'
_A0='row_name'
_z='https://'
_y='sources'
_x='raw'
_w='includeSportsChannelContents'
_v='duration'
_u='seasonList'
_t='startDate'
_s='fanart'
_r='thumb'
_q='x-platform'
_p='filterRestrictedContent'
_o='subType'
_n='story_art_url'
_m='badge'
_l='KR'
_k='com.widevine.alpha'
_j='thumbnail'
_i='category'
_h='x-pcid'
_g='PCID'
_f='perPage'
_e='page'
_d='profileId'
_c='utf-8'
_b='name'
_a='?imwidth=600'
_Z='1'
_Y='src'
_X='running_time'
_W='region'
_V='poster'
_U='key_systems'
_T='url'
_S='false'
_R='story-art'
_Q='ko'
_P='locale'
_O='image'
_N='platform'
_M='type'
_L='SESSION'
_K='COOKIES'
_J='WEBCLIENT'
_I='Get'
_H='true'
_G='id'
_F=False
_E=True
_D='title'
_C='data'
_B='images'
_A=None
__author__='NightRain'
import urllib,re,json,requests,datetime,time,random,base64
from bs4 import BeautifulSoup
try:from Cryptodome.Cipher import PKCS1_OAEP,AES;from Cryptodome.Util import Padding;print('Cryptodome')
except ImportError:from Crypto.Cipher import PKCS1_OAEP,AES;from Crypto.Util import Padding;print('Crypto')
Sports_VODtype={'LONG_HIGHLIGHT':'하이라이트','SHORT_HIGHLIGHT':'하이라이트','PREVIEW':'프리뷰','FULL_MATCH':'다시보기','KEY_MOMENT':'','OTHER':'프로그램'}
COOKIES_PROFILES=['_fbp','_ga',_BR,'_gcl_au','#ak_bmsc','bm_lso','bm_s','CT_AT','CT_ATH','CT_LSID',_AG,_BS,'P_AT',_g,_BT,_AH,_BU,'token','bm_so','CT_DPOP','bm_sv','bm_mi']
COOKIES_DEFAULT=['_fbp','_ga',_BR,'_gcl_au','ak_bmsc','bm_lso','bm_s','CT_AT','CT_ATH','CT_LSID',_AG,_BS,'P_AT',_g,_BT,_AH,_BU,'token','bm_so','CT_DPOP']
class Coupang:
	def __init__(A):A.USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36';A.MODEL='Chrome_152';A.OS_VERSION='152';A.x_app_version='1.76.3';A.DEFAULT_HEADER={_A7:A.USER_AGENT};A.API_DOMAIN=_BV;A.API_VIEWURL='https://discover.coupangstreaming.com';A.PAGE_LIMIT=50;A.SEARCH_LIMIT=20;A.KodiVersion=20;A.CP={};A.Init_CP();A.CP_DEVICE_FILENAME='';A.CP_COOKIE_FILENAME='';A.CP_SESSION_COOKIES1='';A.CP_SESSION_COOKIES2='';A.CP_SESSION_COOKIES3='';A.CP_SESSION_COOKIES4=''
	def callRequestCookies(G,jobtype,url,payload=_A,json=_A,params=_A,headers=_A,cookies=_A,redirects=_F):
		F=redirects;E=cookies;D=headers;C=params;B=G.DEFAULT_HEADER
		if D:B.update(D)
		if jobtype==_I:A=requests.get(url,params=C,headers=B,cookies=E,allow_redirects=F)
		else:A=requests.post(url,data=payload,json=json,params=C,headers=B,cookies=E,allow_redirects=F)
		print(str(A.status_code)+' - '+str(A.url));return A
	def callRequestCookies_test(B,jobtype,url,payload=_A,params=_A,headers=_A,cookies=_A,redirects=_F):
		A=headers;D=B.DEFAULT_HEADER
		if A:D.update(A)
		C=requests.Request('POST',url,headers=A,data=payload,params=params,cookies=cookies);E=C.prepare();B.pretty_print_POST(E);return C
	def pretty_print_POST(B,req):A=req;print('{}\n{}\r\n{}\r\n\r\n{}'.format('-----------START-----------',A.method+' '+A.url,'\r\n'.join('{}: {}'.format(A,B)for(A,B)in A.headers.items()),A.body))
	def dic_To_jsonfile(C,filename,dic):
		A=filename
		if A=='':return
		B=open(A,'w',-1,_c);json.dump(dic,B,indent=4,ensure_ascii=_F);B.close()
	def jsonfile_To_dic(E,filename):
		A=filename
		if A=='':return
		try:B=open(A,'r',-1,_c);C=json.load(B);B.close()
		except Exception as D:print(D);C={}
		return C
	def TextFile_Save(C,filename,resText):
		A=filename
		if A=='':return _F
		try:B=open(A,'w',-1,_c);B.write(resText);B.close()
		except:return _F
		return _E
	def JsonFile_Save(C,filename,dic):
		A=filename
		if A=='':return _F
		try:B=open(A,'w',-1,_c);json.dump(dic,B,indent=4,ensure_ascii=_F);B.close()
		except:return _F
		return _E
	def WebCookies_Load(A,wc_file):
		try:B=open(wc_file,'r',-1,_c);C=B.read();B.close();D=A.Web_DecryptPlaintext(C);A.CP=json.loads(D)
		except:return _F
		return _E
	def Web_DecryptKey(C):A=bytes('kss2lym0kdw1lks3',_c);B=bytes('6yhlJ4WF9ZIj6I8n',_c);return A,B
	def Web_DecryptPlaintext(A,ciphertext):B,C=A.Web_DecryptKey();D=AES.new(B,AES.MODE_CBC,C);E=Padding.unpad(D.decrypt(base64.standard_b64decode(ciphertext)),16);return E.decode(_c)
	def convert_TimeStr(D,datetimeStr):
		B=datetimeStr
		try:
			B=B[0:16];C=datetime.datetime.strptime(B,_BW)+datetime.timedelta(hours=9);A=C.weekday()
			if A==0:A='월'
			elif A==1:A='화'
			elif A==2:A='수'
			elif A==3:A='목'
			elif A==4:A='금'
			elif A==5:A='토'
			elif A==6:A='일'
			return C.strftime(_Av)+'('+A+')'+C.strftime(' %H:%M')
		except Exception as E:return B
	def convert_DateStr(D,datetimeStr):
		B=datetimeStr
		try:
			B=B[0:16];C=datetime.datetime.strptime(B,_BW)+datetime.timedelta(hours=9);A=C.weekday()
			if A==0:A='월'
			elif A==1:A='화'
			elif A==2:A='수'
			elif A==3:A='목'
			elif A==4:A='금'
			elif A==5:A='토'
			elif A==6:A='일'
			return C.strftime(_Av)+'('+A+')'
		except:return B
	def Get_Now_Datetime(A):return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9),'Asia/Seoul'))
	def GetNoCache(B):A=int(time.time()*1000);return A
	def generatePcId(A):B=A.GetNoCache();C=random.random();D=str(B)+str(C)[2:12];return D
	def generatePvId(E,genType=_Z):
		import hashlib as C;B=C.md5();D=str(random.random());B.update(D.encode(_c));A=str(B.hexdigest())
		if genType==_Z:return'%s-%s-%s-%s-%s'%(A[:8],A[8:12],A[12:16],A[16:20],A[20:])
		else:return A
	def Get_DeviceID(C):
		A=''
		try:B=open(C.CP_DEVICE_FILENAME,'r',-1,_c);D=json.load(B);B.close();A=D.get(_AG)
		except Exception as E:_A
		if A=='':
			A=C.generatePvId(genType=_Z)
			try:B=open(C.CP_DEVICE_FILENAME,'w',-1,_c);json.dump({_AG:A},B,indent=4,ensure_ascii=_F);B.close()
			except Exception as E:return''
		return A
	def make_stream_header(J,headers,cookies):
		I='{}={}';G=headers;A=cookies;B=''
		if A not in[{},_A,'']:
			H=len(A)
			for(C,D)in A.items():
				B+=I.format(C,D);H+=-1
				if H>0:B+='; '
			G[_Ab]=B
		E='';F=0
		for(C,D)in G.items():
			F=F+1
			if F>1:E+='&'
			E+=I.format(C,urllib.parse.quote(D))
		return E
	def Init_CP(A):A.CP={};A.CP[_A8]={'cpid':'','cppw':'','cppf':'0'};A.CP[_L]={};A.CP[_K]={}
	def Save_session_acount(A,cpid,cppw,cppf):A.CP[_A8]['cpid']=base64.standard_b64encode(cpid.encode()).decode(_c);A.CP[_A8]['cppw']=base64.standard_b64encode(cppw.encode()).decode(_c);A.CP[_A8]['cppf']=str(cppf)
	def Load_session_acount(A):B=base64.standard_b64decode(A.CP[_A8]['cpid']).decode(_c);C=base64.standard_b64decode(A.CP[_A8]['cppw']).decode(_c);D=A.CP[_A8]['cppf'];return B,C,D
	def make_CP_DefaultCookies(A):return A.CP[_K]
	def make_Cookies_Str(D,cookies_key=[]):
		B=cookies_key;A=''
		for(C,E)in D.CP[_K].items():
			if C in B or B==[]:A='{} {}={};'.format(A,C,E)
		return A.strip()
	def Get_CP_Login_old(A,userid,userpw,userpf):
		J=userpw;I=userid
		try:
			E=A.API_DOMAIN;F={_BX:_B2,_Aw:'?0',_Ax:_Ac,_Ay:_Ad,_Az:_Ae,_A_:'none',_B0:'?1',_B1:_Z,_A7:A.USER_AGENT};G=A.make_CP_DefaultCookies();C=A.callRequestCookies(_I,E,payload=_A,params=_A,headers=F,cookies=G,redirects=_E)
			if C.status_code not in[200]:return _F
			for D in C.cookies:A.CP[_K][D.name]=D.value
			B=re.findall('NREUM.loader_config={[\\w\\d":,-]+\\}',C.text)[0].split('=')[1];B=B.replace('{','{"').replace(':','":').replace(',',',"');B=json.loads(B);A.CP[_L]['NREUM']={'ac':B[_BY],'tk':B['trustKey'],'ap':B['agentID'],'lk':B[_BZ]}
		except Exception as H:print(H);return _F
		try:
			E=A.API_DOMAIN+'/api/auth';K=A.Get_DeviceID();M=K.split('-')[0];F={'content-type':_Ba,_AS:A.x_app_version,_Af:'',_Ag:A.OS_VERSION,_Ah:A.CP[_K][_AH],_h:''};N={'device':{'deviceId':'web-'+K,'model':A.MODEL,_b:'Chrome Desktop '+M,'os':'Windows','osVersion':'10',_M:'webclient'},'email':I,'password':J};G=A.make_CP_DefaultCookies();C=A.callRequestCookies('Post',E,json=N,params=_A,headers=F,cookies=G,redirects=_F)
			if C.status_code not in[200]:
				L=json.loads(C.text)
				if _AI in L:A.CP[_L][_AI]=L.get(_AI).get(_Ai)
				return _F
			print('---')
			for D in C.cookies:A.CP[_K][D.name]=D.value
		except Exception as H:print(H);return _F
		A.Save_session_acount(I,J,userpf);return _E
	def Get_CP_Login(B,userid,userpw,userpf):
		P='rtnUrl';O='"Chromium";v="{}", "Google Chrome";v="{}", "Not/A)Brand";v="99"';N='gzip, deflate, br, zstd';M='accept-encoding';L='{} - {}';from curl_cffi import requests as Q;J='chrome124';K=Q.Session()
		try:
			E=_BV;F={'Accept':_Ak,M:N,_BX:_B2,_Aj:_A9,_B3:_A9,_B4:_B5,_Bb:O.format(B.OS_VERSION,B.OS_VERSION),_Aw:'?0',_Ax:_Ac,_Ay:_Ad,_Az:_Ae,_A_:'none',_B0:'?1',_B1:_Z,_A7:B.USER_AGENT};A=K.get(E,headers=F,impersonate=J);print(L.format(A.status_code,A.url))
			if A.status_code not in[200]:return _F
			for C in A.cookies.jar:B.CP[_K][C.name]=C.value
			D=re.findall('NREUM.loader_config={[\\w\\d":,-]+}',A.text)[0].split('=')[1];D=D.replace('{','{"').replace(':','":').replace(',',',"');D=json.loads(D);B.CP[_L]['NREUM']={'ac':D[_BY],'tk':D['trustKey'],'ap':D['agentID'],'lk':D[_BZ]};H=re.findall('<meta name="coupangplay:git-sha" content="[\\w\\d]+"/>',A.text)[0];H=re.findall('content="[\\w\\d]+"',H)[0].split('=')[1];H=H.replace('"','')
		except Exception as G:print(G);return _F
		time.sleep(1.1)
		try:
			E='https://www.coupangplay.com/_next/data/{}/ko/oauth2/login.json'.format(H);R={'returnPath':'/','sourcePage':'page_home_pre_login','isSignup':_S,'hideQR':_S,'doNotForceLogout':_S,P:'https://www.coupangplay.com/login/callback?returnpath=%252F&sourcePage=page_home_pre_login'};F={_A7:B.USER_AGENT};A=K.get(E,params=R,headers=F,cookies=_A,impersonate=J);print(L.format(A.status_code,A.url))
			if A.status_code not in[200]:return _F
			for C in A.cookies.jar:B.CP[_K][C.name]=C.value
			I=json.loads(A.text);I=I.get(_Bc).get('__N_REDIRECT')
		except Exception as G:print(G);return _F
		time.sleep(1.1)
		try:
			E=I;F={_A7:B.USER_AGENT};A=K.get(E,params=_A,headers=F,cookies=_A,impersonate=J);print(L.format(A.status_code,A.url))
			if A.status_code not in[200]:return _F
			for C in A.cookies.jar:B.CP[_K][C.name]=C.value
		except Exception as G:print(G);return _F
		time.sleep(1.1)
		try:
			S=urllib.parse.urlparse(I);T=dict(urllib.parse.parse_qsl(S.query));E=T.get(P);F={_B6:_Ak,M:N,_B7:_B2,_Aj:_A9,_B3:_A9,_B4:_B5,'referer':I,'sec-ch-ua':O.format(B.OS_VERSION,B.OS_VERSION),'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':_Ac,'sec-fetch-dest':_Ad,'sec-fetch-mode':_Ae,'sec-fetch-site':'same-origin','sec-fetch-user':'?1','upgrade-insecure-requests':_Z,_A7:B.USER_AGENT};A=K.get(E,headers=F,cookies=_A,impersonate=J,allow_redirects=_E);print(L.format(A.status_code,A.url))
			if A.status_code not in[200]:return _F
			for C in A.cookies.jar:B.CP[_K][C.name]=C.value
		except Exception as G:print(G);return _F
		return;'\n\t\ttry:\n\t\t\t# 3차 200\n\t\t\turl = \'https://login.coupang.com/login/v2/signin\'\n\n\t\t\theaders\t= {\n\t\t\t\t\t\t\'content-type\'  \t\t: \'application/json\',\n\t\t\t\t\t\t\'x-requested-with\'      : \'XMLHttpRequest\',\n\t\t\t\t\t\t\'user-agent\'            : self.USER_AGENT,\n\t\t\t\t\t\t\'referer\'               : \'https://login.coupang.com/login/login.pang?response_type=code&platform=PC_WEB&client_id=eb4e1d26-d400-40f3-a663-ca2b470b004a&state=cf6d79700f34b2b05c186044b8f2ecc931bbc292425e454efe5b3563117fe3e7&service=play&nonce=xmiuANiFyBv8rUNFqiFUvFC7g82Y_G9sg5GdQOg0u7k&code_challenge=5LpVnOarb1sVKMPkBUz7Yh36hqZdBOOzigB9UNLv1UQ&code_challenge_method=S256&max_age=14400&client_info=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F144.0.0.0+Safari%2F537.36&redirect_uri=https%3A%2F%2Fwww.coupangplay.com%2Flogin%2Fcallback&scope=openid+offline+play&audience=https%3A%2F%2Fwww.coupangplay.com\',\n\t\t\t\t\t\t\'Accept-Language\'           : \'ko-KR,ko;q=0.9\',\n\t\t\t\t\t\t#\'Accept-Encoding\'           : \'gzip, deflate, br, zstd\',\n\t\t\t\t\t\t\'Cache-Control\'             : \'no-cache\',\n\t\t\t\t\t\t\'Pragma\'                    : \'no-cache\',\n\t\t\t\t\t\t\'priority\'                  : \'u=0, i\',\n\t\t\t\t\t\t\'Sec-Ch-Ua\'                 : \'"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"\',\n\t\t\t\t\t\t\'Sec-Ch-Ua-Mobile\'          : \'?0\',\n\t\t\t\t\t\t\'Sec-Ch-Ua-Platform\'        : \'"Windows"\',\n\t\t\t\t\t\t\'Sec-Fetch-Dest\'            : \'empty\',\n\t\t\t\t\t\t\'Sec-Fetch-Mode\'            : \'cors\',\n\t\t\t\t\t\t\'Sec-Fetch-Site\'            : \'same-origin\',\n\t\t\t}\n\t\t\tpayload = {\n\t\t\t\t\t\t\'captcha\' : {\n\t\t\t\t\t\t\t\t\t\'captchaAnswer\' : \'\',\n\t\t\t\t\t\t\t\t\t\'captchaToken\'\t: \'\',\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\'commonParams\' : {\n\t\t\t\t\t\t\t\t\t\'enableEasyLogin\' : None,\n\t\t\t\t\t\t\t\t\t\'rememberMe\'      : True,\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\'deviceMetadata\' : {\n\t\t\t\t\t\t\t\t\t#\'fingerPrint\' : \'-540ko-KRArial,Arial Black,Arial Narrow,Arial Unicode MS,Book Antiqua,Bookman Old Style,Calibri,Cambria,Cambria Math,Century,Century Gothic,Century Schoolbook,Comic Sans MS,Consolas,Courier,Courier New,Georgia,Helvetica,Impact,Lucida Bright,Lucida Calligraphy,Lucida Console,Lucida Fax,Lucida Handwriting,Lucida Sans,Lucida Sans Typewriter,Lucida Sans Unicode,Microsoft Sans Serif,Monotype Corsiva,MS Gothic,MS PGothic,MS Reference Sans Serif,MS Sans Serif,MS Serif,Palatino Linotype,Segoe Print,Segoe Script,Segoe UI,Segoe UI Light,Segoe UI Semibold,Segoe UI Symbol,Tahoma,Times,Times New Roman,Trebuchet MS,Verdana,Wingdings,Wingdings 2,Wingdings 353c2e04e2289ac6e5bfc5fabf5628d1d48accelerometer: granted,camera: prompt,clipboard-read: prompt,clipboard-write: granted,geolocation: prompt,background-sync: granted,magnetometer: granted,microphone: prompt,midi: prompt,notifications: prompt,payment-handler: granted,persistent-storage: promptaudio/aac: probably,audio/flac: probably,audio/mpeg: probably,audio/mp4; codecs="mp4a.40.2": probably,audio/ogg; codecs="flac": probably,audio/ogg; codecs="vorbis": probably,audio/ogg; codecs="opus": probably,audio/wav; codecs="1": probably,audio/webm; codecs="vorbis": probably,audio/webm; codecs="opus": probably,audio/x-mpegurl: maybechannelCount: 2,channelCountMode: explicit,channelInterpretation: speakers,maxChannelCount: 2,numberOfInputs: 1,numberOfOutputs: 0,sampleRate: 48000,state: runningvideo/mp4; codecs="flac": probably,video/ogg; codecs="opus": probably,video/webm; codecs="vp9, opus": probably,video/webm; codecs="vp8, vorbis": probably\',\n\t\t\t\t\t\t\t\t\t\'fingerPrint\'     : \'\',\n\t\t\t\t\t\t\t\t\t\'mediaDeviceInfo\' : [],\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\'loginMethod\'  : \'EMAIL_PASSWORD\',\n\t\t\t\t\t\t\'passwordCredentials\' : {\n\t\t\t\t\t\t\t\t\t\'email\'    : userid,\n\t\t\t\t\t\t\t\t\t\'password\' : userpw,\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\'termsConsent\' : None,\n\t\t\t}\n\n\t\t\tcookies = self.make_CP_DefaultCookies()\n\t\t\t#response = httpx.post(url, json=payload, headers=headers, cookies=cookies )\n\t\t\tresponse = SESSION.post(url, json=payload, headers=headers, cookies=cookies, impersonate=impersonate )\n\t\t\tprint( \'{} - {}\'.format(response.status_code, response.url ) )\n\n\t\t\tif response.status_code not in [200] :\n\t\t\t\tres_json = json.loads( response.text )\n\t\t\t\tif \'error\' in res_json:\n\t\t\t\t\tself.CP[\'SESSION\'][\'error\'] = res_json.get(\'error\').get(\'detail\')\n\t\t\t\treturn False\n\n\t\t\tprint( \'---\' )\n\n\t\t\tfor cookie in response.cookies:\n\t\t\t\tself.CP[\'COOKIES\'][cookie] = response.cookies[cookie]\n\n\t\texcept Exception as exception:\n\t\t\tprint(exception)\n\t\t\treturn False\n\n\n\t\t#####\n\t\tself.Save_session_acount( userid, userpw, userpf )\n\t\tself.dic_To_jsonfile( self.CP_COOKIE_FILENAME, self.CP ) # cookies_save\n\t\t#####\n\t\t';return _E
	def Get_CP_profile_old(A,userpf,limit_days=1,re_check=_F):
		G='accountId';E=re_check;B=userpf
		if E==_E:
			if A.CP[_L][_AT]>int(time.time()):print(_Bd);return _E
		try:
			H=A.API_DOMAIN+'/api/profiles';I={_AS:A.x_app_version,_Af:'',_Ag:A.OS_VERSION,_Ah:A.CP[_K][_AH],_h:'','referer':'https://www.coupangplay.com/home'};J=A.make_CP_DefaultCookies();D=A.callRequestCookies(_I,H,payload=_A,params=_A,headers=I,cookies=J,redirects=_E)
			if D.status_code not in[200]:return _F
			K=json.loads(D.text);F=0
			for C in D.cookies:
				A.CP[_K][C.name]=C.value
				if C.name=='bm_sv':F=1;A.CP[_L][_AT]=C.expires
			if F==0:A.CP[_L][_AT]=int(time.time())+7200
			B=K.get(_C)[int(B)];A.CP[_L][G]=B.get(G);A.CP[_L][_d]=B.get(_d)
		except Exception as L:print(L);return _F
		if E==_F:M=A.Get_Now_Datetime();N=M+datetime.timedelta(days=limit_days);A.CP[_L]['limitdate']=N.strftime(_Av)
		else:print('re check')
		A.dic_To_jsonfile(A.CP_COOKIE_FILENAME,A.CP);return _E
	def Get_CP_profile(A):
		if A.CP[_L][_AT]>int(time.time()):print(_Bd);return _E
		try:
			D='https://www.coupangplay.com/api/profiles';E={_B6:_Ak,_B7:_Be,_Aj:_A9,_Ab:A.make_Cookies_Str(COOKIES_PROFILES),'dpr':_Z,_B3:_A9,_B4:_B5,_Bb:'"Chromium";v="{}", "Not?A_Brand";v="24", "Google Chrome";v="{}"'.format(A.OS_VERSION,A.OS_VERSION),_Aw:'?0',_Ax:_Ac,_Ay:_Ad,_Az:_Ae,_A_:'none',_B0:'?1',_B1:_Z,_A7:A.USER_AGENT,'viewport-width':'399'};B=A.callRequestCookies(_I,D,payload=_A,params=_A,headers=E,cookies=_A,redirects=_E)
			if B.status_code not in[200]:return _F
			for C in B.cookies:A.CP[_K][C.name]=C.value
			A.CP[_L][_AT]=int(time.time())+7200
		except Exception as F:print(F);return _F
		A.dic_To_jsonfile(A.CP_COOKIE_FILENAME,A.CP);return _E
	def Get_Category_GroupList(A,vType):
		B=vType;C=[];D={_AU:_AV,_B8:'tv',_B9:_BA}
		try:
			H=A.API_DOMAIN+'/'+D.get(B,_AV);I={_B6:_Ak,_B7:_Be,_Aj:_A9,_Ab:A.make_Cookies_Str(COOKIES_DEFAULT)};E=A.callRequestCookies(_I,H,payload=_A,params=_A,headers=I,cookies=_A,redirects=_E)
			if E.status_code not in[200]:return[]
			J=BeautifulSoup(E.text,'html.parser');K=J.find('script',id='__NEXT_DATA__',type=_Ba);L=json.loads(K.string.strip())
			for F in L.get('props').get(_Bc).get('initialFeedData').get(_C):
				if F.get(_M)==_Bf:
					for G in F.get(_C):M={_AW:G.get(_G),_D:G.get(_b),_i:D.get(B,_AV),_Al:''};C.append(M)
					break
		except Exception as N:print(N);return[]
		return C
	def Get_Category_GroupList_old(A,vType):
		B=vType;E=[]
		try:
			I=A.API_DOMAIN+_Am;J={_N:_J,_W:_l,_P:_Q,_e:_Z,_f:'7',_p:_S,_AA:_H,_AB:_H,_AJ:_H,_i:B,'profile':A.CP[_L][_d]};K={_AS:A.x_app_version,_Af:A.CP[_K][_AG],_Ag:A.OS_VERSION,_Ah:A.CP[_K][_AH],_h:A.CP[_K][_g],_q:_J,_A1:A.CP[_L][_d],'x-profiletype':_An};F=A.callRequestCookies(_I,I,payload=_A,params=J,headers=K,cookies=_A,redirects=_E)
			if F.status_code not in[200]:return[]
			L=json.loads(F.text)
			if B in[_B8,_B9]:G='Explores'
			elif B in[_AU]:G=_Bf
			for C in L.get(_C):
				if C.get(_M)==G:
					for D in C.get(_C):
						if B in[_B8,_B9]:H=D.get(_AW)
						elif B in[_AU]:H=D.get(_G)
						M={_AW:H,_D:D.get(_b),_i:C.get(_i),_Al:''};E.append(M)
					break
		except Exception as N:print(N);return[]
		return E
	def Get_Category_List(B,vType,collectionId,page_int):
		T='/titles';I=collectionId;H=vType;C=page_int;J=[];K=_F
		try:
			if H in[_AV,'tv',_BA]:D={_N:_J,_e:str(C),_f:str(B.PAGE_LIMIT),_P:_Q,'sort':''};U={_h:B.CP[_K][_g],_A1:B.CP[_L][_d],_q:_J,_AS:B.x_app_version};E=B.API_DOMAIN+'/api-discover/v1/discover/categories/'+I+T;F=B.callRequestCookies(_I,E,payload=_A,params=D,headers=U,cookies=_A,redirects=_E)
			else:D={_N:_J,_P:_Q,_e:str(C),_f:str(B.PAGE_LIMIT),'sort':'',_p:_S,_AX:''};E=B.API_DOMAIN+'/api-discover/v1/discover/collections/'+I+T;F=B.callRequestCookies(_I,E,payload=_A,params=D,headers=_A,cookies=_A,redirects=_E)
			if F.status_code not in[200]:return[],_F
			G=json.loads(F.text)
			if H in[_AV,'tv',_BA]:L=G.get(_C).get(_C)
			else:L=G.get(_C)
			for A in L:
				M=N=O=P=''
				if _V in A.get(_B):M=A.get(_B).get(_V).get(_T)+_A2
				if _R in A.get(_B):N=A.get(_B).get(_R).get(_T)+_a
				if _AK in A.get(_B):O=A.get(_B).get(_AK).get(_T)+_AY
				if _R in A.get(_B):P=A.get(_B).get(_R).get(_T)+_a
				Q=''
				if A.get(_m)not in[{},_A]:
					for V in A.get(_m).get(_A3):Q+=V.get(_A3)
				R=''
				if A.get(_u)!=_A:R=','.join(str(A)for A in A.get(_u))
				S=[]
				for W in A.get(_Ao):S.append(W.get('tag'))
				X={_G:A.get(_G),_D:A.get(_D),_j:{_V:M,_r:N,_AL:O,_s:P},_AC:A.get(_AM),_v:A.get(_X),_A4:A.get('as'),_m:Q,_AD:A.get(_Ap).get(_AZ),_u:R,_BB:S};J.append(X)
			if G.get(_BC).get(_BD)>C:K=_E
		except Exception as Y:print(Y);return[],_F
		return J,K
	def Get_Episode_List(B,programId,season,page=1,orderby='asc'):
		K='episode';E=season;D=programId;F=[];G=_F
		try:
			L=B.API_DOMAIN+'/api-discover/v2/discover/titles/'+D+'/episodes';M={_Aq:D,'seasonRange':'{}~{}'.format(E,E),_f:str(B.PAGE_LIMIT),_AX:_S,_P:_Q,_e:str(page),_N:_J,'sort':_H,'overrideSortOrder':orderby};H=B.callRequestCookies(_I,L,payload=_A,params=M,headers=_A,cookies=_A,redirects=_E)
			if H.status_code not in[200]:return[],_F
			I=json.loads(H.text)
			for A in I.get(_C):
				C=''
				if _R in A.get(_B):C=A.get(_B).get(_R).get(_T)+_a
				J=[]
				for N in A.get(_Ao):J.append(N.get('tag'))
				O={_G:A.get(_G),_D:A.get(_D),_j:{_r:C,_s:C},_AC:A.get(_AM),_v:A.get(_X),_A4:A.get('as'),_AD:A.get(_Ap).get(_AZ),K:A.get(K),_BB:J,'desc':A.get(_Bg)};F.append(O)
			if I.get(_BC).get(_BD)>page:G=_E
		except Exception as P:print(P);return[]
		return F,G
	def Get_vInfo(B,titleId):
		F='downloadable';E='availability'
		try:
			G=B.API_DOMAIN+_Bh+titleId;H={_N:_J,_P:_Q,_p:_S};C=B.callRequestCookies(_I,G,payload=_A,params=H,headers=_A,cookies=_A,redirects=_E)
			if C.status_code not in[200]:return'','',''
			A=json.loads(C.text).get(_C);D=''
			if A.get(_u)!=_A:D=','.join(str(A)for A in A.get(_u))
			I={_AM:A.get(_AM),_AN:A.get(_AN),E:A.get(E),_AO:A.get(_AO),F:_H if A.get(F)else _S,_W:A.get(_W),_AP:_H if A.get(_AP)else _S,_A4:A.get('as'),_u:D}
		except Exception as J:print(J);return{}
		return I
	def Get_eInfo(B,eventId):
		try:
			D=B.API_DOMAIN+_BE+eventId;E={_P:_Q,_N:_J,_w:_H};C=B.callRequestCookies(_I,D,payload=_A,params=E,headers=_A,cookies=_A,redirects=_E)
			if C.status_code not in[200]:return'','',''
			A=json.loads(C.text).get(_C);F={_AN:A.get(_AN),_AO:A.get(_AO),_W:A.get(_W),_AP:_H if A.get(_AP)else _S}
		except Exception as G:print(G);return{}
		return F
	def GetBroadURL(B,titleId):
		F='codecs';C='';D=''
		try:
			H=B.API_DOMAIN+_BF;I={_Aq:titleId};J={_Ab:B.make_Cookies_Str(COOKIES_DEFAULT),_AS:B.x_app_version,_Af:B.CP[_K][_AG],_Ag:B.OS_VERSION,_BG:_H,_Ah:B.CP[_K][_AH],_h:B.CP[_K][_g],_q:'web',_BH:B.CP[_L][_d],_BI:_An,'x-sessionid':B.generatePvId(genType=_Z)};G=B.callRequestCookies(_I,H,payload=_A,params=I,headers=J,cookies=_A,redirects=_E)
			if G.status_code not in[200]:return'',json.loads(G.text).get(_AI).get(_Ai)
			E=json.loads(G.text)
			if C=='':
				for A in E.get(_C).get(_x).get(_y):
					if _U in A and F not in A:
						if A.get(_M)==_Aa and _k in A.get(_U)and A.get(_Y).startswith(_z)==_E:C=A.get(_Y);D=A.get(_U).get(_k).get(_AE);break
			if C=='':
				for A in E.get(_C).get(_x).get(_y):
					if _U in A and F not in A:
						if A.get(_M)==_Ar and _k in A.get(_U)and A.get(_Y).startswith(_z)==_E:C=A.get(_Y);D=A.get(_U).get(_k).get(_AE);break
			if C=='':
				for A in E.get(_C).get(_x).get(_y):
					if _U in A and F in A:
						if A.get(_M)==_Aa and _k in A.get(_U)and A.get(_Y).startswith(_z)==_E:C=A.get(_Y);D=A.get(_U).get(_k).get(_AE);break
			if C=='':
				for A in E.get(_C).get(_x).get(_y):
					if _U in A and F in A:
						if A.get(_M)==_Ar and _k in A.get(_U)and A.get(_Y).startswith(_z)==_E:C=A.get(_Y);D=A.get(_U).get(_k).get(_AE);break
		except Exception as K:print(K);return'',''
		return C,D
	def GetEventURL(A,eventId,asis):
		E=eventId;F='';G='';B=A.Get_eInfo(E)
		if B=={}:return'',''
		try:
			H=A.API_DOMAIN+_BF;I={_Aq:E,_Bi:asis};J={_Ab:A.make_Cookies_Str(COOKIES_DEFAULT),_AS:A.x_app_version,_Af:A.CP[_K][_AG],_Ag:A.OS_VERSION,_Ah:A.CP[_K][_AH],'x-sessionid':A.generatePvId(genType=_Z),_BG:_H,_h:A.CP[_K][_g],_q:'web',_BH:A.CP[_L][_d],_BI:_An,_Bj:_AQ,_Bk:_AQ,_Bl:_AQ,_Bm:B.get(_AN),_Bn:B.get(_AO),_Bo:B.get(_W),_Bp:B.get(_AP)};K=A.make_CP_DefaultCookies();D=A.callRequestCookies(_I,H,payload=_A,params=I,headers=J,cookies=K,redirects=_E)
			print('COUPANG_DEBUG_STATUS:', D.status_code); print('COUPANG_DEBUG_BODY:', D.text[:3000])
			if D.status_code not in[200]:return'',json.loads(D.text).get(_AI).get(_Ai)
			L=json.loads(D.text)
			for C in L.get(_C).get(_x).get(_y):
				if C.get(_M)==_Aa and C.get(_Y)[0:8]==_z:
					F=C.get(_Y)
					if _U in C:G=C.get(_U).get(_k).get(_AE)
					break
		except Exception as M:print(M);return'',''
		return F,G
	def GetEventURL_Live(C,eventId,asis):
		H=eventId;B='';F='';D=C.Get_eInfo(H)
		if D=={}:return'',''
		try:
			I=C.API_DOMAIN+_BF;J={_Aq:H,_Bi:asis};K={_Ab:C.make_Cookies_Str(COOKIES_DEFAULT),_AS:C.x_app_version,_Af:C.CP[_K][_AG],_Ag:C.OS_VERSION,_Ah:C.CP[_K][_AH],'x-sessionid':C.generatePvId(genType=_Z),_BG:_H,_h:C.CP[_K][_g],_q:'web',_BH:C.CP[_L][_d],_BI:_An,_Bj:_AQ,_Bk:_AQ,_Bm:D.get(_AN),_Bn:D.get(_AO),_Bl:_AQ,_Bo:D.get(_W),_Bp:D.get(_AP)};L=C.make_CP_DefaultCookies();G=C.callRequestCookies(_I,I,payload=_A,params=J,headers=K,cookies=L,redirects=_E)
			if G.status_code not in[200]:return'',json.loads(G.text).get(_AI).get(_Ai)
			E=json.loads(G.text)
			if B=='':
				for A in E.get(_C).get(_x).get(_y):
					if _U in A:
						if A.get(_M)==_Aa and _k in A.get(_U)and A.get(_Y).startswith(_z)==_E:B=A.get(_Y);F=A.get(_U).get(_k).get(_AE)
			if B=='':
				for A in E.get(_C).get(_x).get(_y):
					if _U in A:
						if A.get(_M)==_Ar and _k in A.get(_U)and A.get(_Y).startswith(_z)==_E:B=A.get(_Y);F=A.get(_U).get(_k).get(_AE)
			if B=='':
				for A in E.get(_C).get(_x).get(_y):
					if A.get(_M)==_Aa and A.get(_Y).startswith(_z)==_E:B=A.get(_Y)
			if B=='':
				for A in E.get(_C).get(_x).get(_y):
					if A.get(_M)==_Ar and A.get(_Y).startswith(_z)==_E:B=A.get(_Y)
		except Exception as M:print(M);return'',''
		return B,F
	def Get_Url_PostFix(E,in_url):C=urllib.parse.urlparse(in_url);A=C.path.strip('/').split('/');D=A[len(A)-1];B=D.split('.');return B[len(B)-1]
	def Get_Theme_GroupList(C,vType):
		E=[]
		try:
			H=C.API_DOMAIN+_Am;I={_N:_J,_W:_l,_P:_Q,_e:_Z,_f:str(C.PAGE_LIMIT),_p:_S,_AA:_H,_AB:_H,_AJ:_H,_i:vType,'profile':C.CP[_L][_d]};F=C.callRequestCookies(_I,H,payload=_A,params=I,headers=_A,cookies=_A,redirects=_E)
			if F.status_code not in[200]:return[]
			J=json.loads(F.text)
			for A in J.get(_C):
				if A.get(_M)=='Title-Rails-Curation':
					B='';K=7
					try:
						for G in range(len(A.get(_C))):
							if G>=K:B=B+'...';break
							B=B+A[_C][G][_D]+'\n'
					except Exception as D:print(D)
					L={_AW:A.get(_AF),_D:A.get(_A0),_i:A.get(_i),_Al:B};E.append(L)
		except Exception as D:print(D);return[]
		return E
	def Get_Event_GroupList(D):
		E=[]
		try:
			H=D.API_DOMAIN+_Am;I={_i:'LIVE',_N:_J,_W:_l,_P:_Q,_e:_Z,_f:7,_p:_S,_AA:_H,_AB:_H,_AJ:_H,_AX:_S};F=D.callRequestCookies(_I,H,payload=_A,params=I,headers=_A,cookies=_A,redirects=_E)
			if F.status_code not in[200]:return[]
			J=json.loads(F.text)
			for A in J.get(_C):
				if A.get(_A0).strip()!='':
					B='';K=7
					try:
						for G in range(len(A.get(_C))):
							if G>=K:B=B+'...';break
							B=B+A[_C][G][_D]+'\n'
					except Exception as C:print(C)
					L={_AW:A.get(_AF),_D:A.get(_A0),_i:A.get(_M),_Al:B};E.append(L)
		except Exception as C:print(C);return[]
		return E
	def Get_Event_GameList(B,collectionId):
		C=[]
		try:
			I=B.API_DOMAIN+_Am;J={_i:'LIVE',_N:_J,_W:_l,_P:_Q,_e:_Z,_f:7,_p:_S,_AA:_H,_AB:_H,_AJ:_H,_AX:_S};D=B.callRequestCookies(_I,I,payload=_A,params=J,headers=_A,cookies=_A,redirects=_E)
			if D.status_code not in[200]:return[]
			K=json.loads(D.text)
			for E in K.get(_C):
				if E.get(_AF)==collectionId:
					for A in E.get(_C):
						F=G=H=''
						if _AR in A.get(_B):F=A.get(_B).get(_AR)+_A2
						if _n in A.get(_B):G=A.get(_B).get(_n)+_a
						if _As in A.get(_B):H=A.get(_B).get(_As)+_a
						L={_G:A.get(_G),_D:A.get(_D),_j:{_V:F,_r:G,_s:H},_A4:A.get(_M),'starttm':B.convert_TimeStr(A.get(_BJ))};C.append(L)
		except Exception as M:print(M);return[]
		return C
	def Get_Event_List(B,gameId):
		N=gameId;G=[]
		try:
			H=B.API_DOMAIN+_BE+N;I={_N:_J,_P:_Q,_p:_S};C=B.callRequestCookies(_I,H,payload=_A,params=I,headers=_A,cookies=_A,redirects=_E)
			if C.status_code not in[200]:return[]
			J=json.loads(C.text);A=J.get(_C);K=A.get('end_at');K=K[0:19].replace('-','').replace(':','').replace('T','');O=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')
			if int(O)<int(K):
				D=E=F=''
				if _V in A.get(_B):D=A.get(_B).get(_V).get(_T)+_A2
				if _R in A.get(_B):E=A.get(_B).get(_R).get(_T)+_a
				if _R in A.get(_B):F=A.get(_B).get(_R).get(_T)+_a
				L={_G:A.get(_G),_D:A.get(_D),_j:{_V:D,_r:E,_s:F},_v:A.get(_X),_A4:A.get(_M),'starttm':B.convert_TimeStr(A.get('start_at'))};G.append(L)
		except Exception as M:print(M);return[]
		try:
			H=B.API_DOMAIN+_BE+N+'/related';I={_P:_Q,_e:_Z,_f:'25',_N:_J,'currentPageTracking':'page_discover_title_detail'};C=B.callRequestCookies(_I,H,payload=_A,params=I,headers=_A,cookies=_A,redirects=_E)
			if C.status_code not in[200]:return[]
			J=json.loads(C.text)
			for A in J.get(_C).get(_C):
				D=E=F=''
				if _V in A.get(_B):D=A.get(_B).get(_V).get(_T)+_A2
				if _R in A.get(_B):E=A.get(_B).get(_R).get(_T)+_a
				if _R in A.get(_B):F=A.get(_B).get(_R).get(_T)+_a
				L={_G:A.get(_G),_D:A.get(_D),_j:{_V:D,_r:E,_s:F},_v:A.get(_X),_A4:A.get(_M)};G.append(L)
		except Exception as M:print(M);return[]
		return G
	def Get_Search_List_back(B,search_key,page_int):
		D=page_int;E=[];F=_F
		try:
			N=B.API_DOMAIN+'/api-discover/v2/search';O={'query':search_key,_N:_J,_e:str(D),_f:str(B.SEARCH_LIMIT)};P={_h:B.CP[_K][_g],_A1:B.CP[_L][_d],_q:_J};G=B.callRequestCookies(_I,N,payload=_A,params=O,headers=P,cookies=_A,redirects=_E)
			if G.status_code not in[200]:return[],_F
			H=json.loads(G.text)
			for A in H.get(_C).get(_C):
				A=A.get(_C);I=J=K=L=''
				if _V in A.get(_B):I=A.get(_B).get(_V).get(_T)+_A2
				if _R in A.get(_B):J=A.get(_B).get(_R).get(_T)+_a
				if _AK in A.get(_B):K=A.get(_B).get(_AK).get(_T)+_AY
				if _R in A.get(_B):L=A.get(_B).get(_R).get(_T)+_a
				C=''
				if A.get(_m)not in[{},_A]:
					for Q in A.get(_m).get(_A3):
						if C!='':C+=' '
						C+=Q.get(_A3)
				if'as'in A:M=A.get('as')
				else:M=A.get(_M)
				R={_G:A.get(_G),_D:A.get(_D),_A4:M,_j:{_V:I,_r:J,_AL:K,_s:L},_AC:A.get(_AM),_v:A.get(_X),_m:C,_AD:A.get(_Ap).get(_AZ)};E.append(R)
			if H.get(_BC).get(_BD)>D:F=_E
		except Exception as S:print(S);return[],_F
		return E,F
	def Get_Search_List(B,search_key,page_int):
		D=[];J=_F
		try:
			K=B.API_DOMAIN+'/api-discover/v3/search';L={'query':search_key,_N:_J,_e:str(page_int),_f:'48','filterSearchGroupTypes':'','filterSearchGroupType':'TITLES-EVENT_LIVE-EVENT_CHANNELS',_AX:_H,_w:_H};M={_h:B.CP[_K][_g],_A1:B.CP[_L][_d]};E=B.callRequestCookies(_I,K,payload=_A,params=L,headers=M,cookies=_A,redirects=_E)
			if E.status_code not in[200]:return[],_F
			N=json.loads(E.text)
			for A in N.get(_C).get('contents'):
				F=G=H=I=''
				if _AR in A.get(_B):F=A.get(_B).get(_AR)+_A2
				if _n in A.get(_B):G=A.get(_B).get(_n)+_a
				if _At in A.get(_B):H=A.get(_B).get(_At)+_AY
				if _n in A.get(_B):I=A.get(_B).get(_n)+_a
				C=''
				if A.get(_m)not in[{},_A]:
					for O in A.get(_m).get(_A3):
						if C!='':C+=' '
						C+=O.get(_A3)
				P=A.get(_BK);Q={_G:A.get(_G),_D:A.get(_D),_A4:P,_j:{_V:F,_r:G,_AL:H,_s:I},_AC:A.get('ageRatingLocalized'),_v:A.get(_X),_m:C,_AD:A.get('airing_date_friendly')[8:12]};D.append(Q)
		except Exception as R:print(R);return[],_F
		return D,J
	def GetBookmarkInfo(M,videoid,vidtype):
		Y='role';X='background';W='movie';V='genre';U='director';T='cast';S='plot';N=videoid;F=vidtype;D='infoLabels';C='saveinfo';B={'indexinfo':{'ott':'coupang','videoid':N,'vidtype':F},C:{_D:'','subtitle':'',_j:{_V:'',_r:'',_AL:'','icon':'','banner':'',_s:''},D:{'mediatype':F,_D:'',_AC:'',S:'',_AD:'','studio':'',_v:0,T:[],U:[],V:[],'premiered':'','country':''}}};Z=M.API_DOMAIN+_Bh+N;a={_P:_Q};O=M.callRequestCookies(_I,Z,payload=_A,params=a,headers=_A,cookies=_A,redirects=_E)
		if O.status_code not in[200]:return{}
		A=json.loads(O.text).get(_C);G=A.get(_D);P=A.get(_Ap).get(_AZ);B[C][D][_D]=G
		if F==W:G='%s  (%s)'%(G,P)
		B[C][_D]=G;B[C][D][_AC]=A.get(_AM);B[C][D][S]='%s\n\n%s'%(A.get('short_description'),A.get(_Bg));B[C][D][_AD]=P
		if F==W:B[C][D][_v]=A.get(_X)
		Q='';H='';I='';R=''
		if A.get(_B).get(_V)!=_A:Q=A.get(_B).get(_V).get(_T)+_A2
		if A.get(_B).get(X)!=_A:H=A.get(_B).get(X).get(_T)+_a
		if A.get(_B).get(_R)!=_A:I=A.get(_B).get(_R).get(_T)+_a
		if A.get(_B).get(_AK)!=_A:R=A.get(_B).get(_AK).get(_T)+_AY
		if H=='':H=I
		B[C][_j][_V]=Q;B[C][_j][_s]=H;B[C][_j][_r]=I;B[C][_j][_AL]=R;J=[]
		for E in A.get(_Ao):J.append(E.get('tag'))
		if len(J)>0:B[C][D][V]=J
		K=[];L=[]
		for E in A.get('people'):
			if E.get(Y)=='CAST':K.append(E.get(_b))
			if E.get(Y)=='DIRECTOR':L.append(E.get(_b))
		if len(K)>0:B[C][D][T]=K
		if len(L)>0:B[C][D][U]=L
		return B
	def MakeText_FreeList(E,search_list,titleName=_D):
		B=search_list;A='';D=5
		try:
			for C in range(len(B)):
				if C>=D:A=A+'...';break
				A=A+B[C][titleName]+'\n'
		except:return''
		return A
	def Sports_Mainlist_League(B):
		E='logoUrl';C=[]
		try:
			F='{}/api-discover/v1/sports/leagues/pills'.format(B.API_DOMAIN);G={_N:_J,'useCircularLogo':_H};D=B.callRequestCookies(_I,F,payload=_A,params=G,headers=_A,cookies=_A)
			if D.status_code not in[200]:return[]
			H=json.loads(D.text)
			for A in H.get(_C):I={_Bq:A[_G],'league_name':A[_b],E:A[E]};C.append(I)
		except Exception as J:print(J);return[]
		return C
	def Sports_League_FeedList(B,leagueID):
		I=leagueID;H='subMode';F=[]
		try:
			K=_Br.format(B.API_DOMAIN,I);L={_N:_J,_W:_l,_P:_Q,_w:_H};J=B.callRequestCookies(_I,K,payload=_A,params=L,headers=_A,cookies=_A)
			if J.status_code not in[200]:return[]
			M=json.loads(J.text).get(_C)
			for C in M.get(_C):
				if C[_M]=='Calendar':
					A=B.Sports_leagueHome_Livelist(I)
					if A:G=B.MakeText_FreeList(A,titleName=_BL);D={_A0:'@ 예정 경기 @',_A5:G,H:_Bs,_O:A[0][_O]};F.append(D)
				elif C[_M]==_Bt:
					A=B.Sports_LeagueHome_List(data=C,sType=_BM)
					if A:G=B.MakeText_FreeList(A,titleName=_D);D={_A0:C[_A0],_A5:G,H:_BN,_O:A[0][_O]};F.append(D)
				elif C[_M]==_Bu:
					A=B.Sports_LeagueHome_List(data=C,sType='gameVod')
					for E in A:D={_A0:_BO.format(E[_D],E[_t]),_A5:E[_A5],H:_BP,'gameID':E[_G],_O:E[_O]};F.append(D)
		except Exception as N:print(N);return[]
		return F
	def Sports_League_VodList(B,subMode,leagueID,gameID):
		H=leagueID;E=subMode;F=[]
		try:
			if E==_Bs:
				C=B.Sports_leagueHome_Livelist(H)
				for A in C:D={_G:A.get(_BQ),_D:A.get(_D),_O:A.get(_O),_t:A.get(_t),_o:A.get(_o)};F.append(D)
			elif E in[_BN,_BP]:
				K=_Br.format(B.API_DOMAIN,H);L={_N:_J,_W:_l,_P:_Q,_w:_H};I=B.callRequestCookies(_I,K,payload=_A,params=L,headers=_A,cookies=_A)
				if I.status_code not in[200]:return[]
				M=json.loads(I.text).get(_C)
				for G in M.get(_C):
					if G[_M]==_Bt and E==_BN:
						C=B.Sports_LeagueHome_List(data=G,sType=_BM)
						for A in C:D={_G:A.get(_G),_D:A.get(_D),_O:A.get(_O),_t:A.get(_t),_o:A.get(_o),_X:A.get(_X)};F.append(D)
					elif G[_M]==_Bu and E==_BP:
						for J in G[_C]:
							if gameID==J[_G]:
								C=B.Sports_LeagueHome_SubVods(data=J)
								for A in C:D={_G:A.get(_G),_D:A.get(_D),_O:A.get(_O),_o:A.get(_o),_X:A.get(_X)};F.append(D)
								break
		except Exception as N:print(N);return[]
		return F
	def Sports_LeagueHome_List(B,data,sType=''):
		F=sType;D=[]
		try:
			if F==_BM:
				for A in data.get(_C):
					G=''
					if _Au in A:G='패스'
					E={_G:A[_G],_D:A[_D],_o:G,_O:A[_B][_n],_X:A[_X],_t:B.convert_DateStr(A[_BJ])};D.append(E)
			elif F=='gameVod':
				for A in data.get(_C):
					if len(A[_A6])>=2:C=A[_A6][0][_b];I=A[_A6][1][_b];C=C+' vs '+I
					else:C=A[_A6][0][_b]
					H=B.Sports_LeagueHome_SubVods(A);J=B.MakeText_FreeList(H,titleName=_D);E={_G:A[_G],_D:C,_t:B.convert_DateStr(A['startsAt']),_A5:J,_O:H[0][_O]};D.append(E)
		except Exception as K:print(K);return[]
		return D
	def Sports_LeagueHome_SubVods(F,data):
		B=[]
		try:
			for A in data.get('highlights'):
				C=''
				if _Au in A:C='패스'
				D={_G:A[_G],_D:A[_D],_O:A[_B][_R][_T],_o:C,_X:A[_X]};B.append(D)
		except Exception as E:print(E);return[]
		return B
	def Sports_leagueHome_Livelist(B,leagueID):
		D='teams';E=[]
		try:
			J='{}/api-discover/v1/sports/curated-schedule/events'.format(B.API_DOMAIN);K={_Bq:leagueID,_W:_l,_P:_Q,'scope':'live-upcoming','includeHighlights':_S,_w:_H};L={_h:B.CP[_K][_g],_A1:B.CP[_L][_d],_q:_J};F=B.callRequestCookies(_I,J,payload=_A,params=K,headers=L,cookies=_A)
			if F.status_code not in[200]:return[]
			M=json.loads(F.text).get(_C)
			for A in M:
				if len(A[D])>=2:C=A[D][0][_b];N=A[D][1][_b];C=C+' vs '+N
				else:C=A[D][0][_b]
				G=''
				if A.get(_B):G=A.get(_B).get(_n)
				H=B.convert_TimeStr(A['start_at']);I=''
				if _Au in A:I='패스'
				O={_BQ:A[_BQ],_D:C,_t:H,_O:G,_BL:_BO.format(C,H),_o:I};E.append(O)
		except Exception as P:print(P);return[]
		return E
	def Sports_MultiHero_LiveList(B):
		I='sports_hero_mobile_url';D=[]
		try:
			J='{}/api-discover/v1/sports/feed'.format(B.API_DOMAIN);K={_N:_J,_W:_l,_P:_Q,_p:_S,_AA:_H,_AB:_H,_i:'LIVE',_f:'7','allowOtherRailsAboveHero':_H,_w:_H,_e:_Z};E=B.callRequestCookies(_I,J,payload=_A,params=K,headers=_A,cookies=_A)
			if E.status_code not in[200]:return[]
			L=json.loads(E.text).get(_C)
			for F in L:
				if F.get(_M)=='Multi-Hero-Live-Event-Curation':
					for A in F.get(_C):
						G=B.convert_TimeStr(A[_BJ]);"\n\t\t\t\t\t\ttry:\n\t\t\t\t\t\t\tstartDate = self.convert_TimeStr( i_vod['startAt'] )\n\t\t\t\t\t\texcept Exception as exception:\n\t\t\t\t\t\t\taa = 'exception = {}'.format( exception )\n\t\t\t\t\t\t\tbb = { 'aa' : aa }\n\t\t\t\t\t\t\tself.dic_To_jsonfile( 'd:\\Naver MYBOX\\sync\\job\\cp_cookies1.json', bb )\n\t\t\t\t\t\t";C=''
						if A.get(_B):
							if A.get(_B).get(_As):C=A.get(_B).get(_As)
							elif A.get(_B).get(I):C=A.get(_B).get(I)
						H=''
						if _Au in A:H='패스'
						M={_G:A[_G],_D:A[_D],_t:G,_O:C,_BL:_BO.format(A[_D],G),_o:H};D.append(M)
					break
		except Exception as N:print(N);return[]
		return D
	def Sports_Season_Group(A,leagueID):
		F='season';B=[]
		try:
			G='{}/api-discover/v1/discover/sports/leagues/{}/filters'.format(A.API_DOMAIN,leagueID);H={_N:_J,_P:_Q,_w:_H};I={_h:A.CP[_K][_g],_A1:A.CP[_L][_d],_q:_J};C=A.callRequestCookies(_I,G,payload=_A,params=H,headers=I,cookies=_A)
			if C.status_code not in[200]:return[]
			J=json.loads(C.text).get(_C)
			for D in J:
				E=[]
				for K in D.get('stages'):L={_D:K[_b]};E.append(L)
				M=A.MakeText_FreeList(E,titleName=_D);N={F:D[F],_A5:M};B.append(N)
		except Exception as O:print(O);return[]
		return B
	def Sports_Season_GameList(A,leagueID,seasonID,page=1):
		D=[]
		try:
			G=_Bv.format(A.API_DOMAIN,leagueID);H={'seasons':seasonID,'stageIds':'','teamIds':'',_N:_J,_P:_Q,_W:_l,_f:'10',_w:_H,_e:str(page)};N={_h:A.CP[_K][_g],_A1:A.CP[_L][_d],_q:_J};E=A.callRequestCookies(_I,G,payload=_A,params=H,headers=_A,cookies=_A)
			if E.status_code not in[200]:return[]
			I=json.loads(E.text).get(_C)
			for B in I:
				if len(B[_A6])>=2:C=B[_A6][0][_b];J=B[_A6][1][_b];C=C+' vs '+J
				else:C=B[_A6][0][_b]
				F=A.Sports_LeagueHome_SubVods(B);K=A.MakeText_FreeList(F,titleName=_D);L={_G:B[_G],_D:C,_t:A.convert_DateStr(B['startsAt']),_A5:K,_O:F[0][_O]};D.append(L)
		except Exception as M:print(M);return[]
		return D
	def Sports_Season_GameVod(A,leagueID,seasonID,page,gameID):
		C=[]
		try:
			F=_Bv.format(A.API_DOMAIN,leagueID);G={'seasons':seasonID,'stageIds':'','teamIds':'',_N:_J,_P:_Q,_W:_l,_f:'10',_w:_H,_e:str(page)};L={_h:A.CP[_K][_g],_A1:A.CP[_L][_d],_q:_J};D=A.callRequestCookies(_I,F,payload=_A,params=G,headers=_A,cookies=_A)
			if D.status_code not in[200]:return[]
			H=json.loads(D.text).get(_C)
			for E in H:
				if gameID==E[_G]:
					I=A.Sports_LeagueHome_SubVods(E)
					for B in I:J={_G:B.get(_G),_D:B.get(_D),_O:B.get(_O),_o:B.get(_o),_X:B.get(_X)};C.append(J)
		except Exception as K:print(K);return[]
		return C
	def Get_Pass_GroupList(B,collectionId):
		C=[]
		try:
			E=_Bw.format(B.API_DOMAIN,collectionId);F={_N:_J,_W:_l,_P:_Q,_e:_Z,_f:str(B.PAGE_LIMIT),_p:_S,_AA:_H,_AB:_H,_AJ:_H,_i:_AU};D=B.callRequestCookies(_I,E,payload=_A,params=F,headers=_A,cookies=_A)
			if D.status_code not in[200]:return[]
			G=json.loads(D.text).get(_C)
			for A in G:
				if A.get(_A0)and A.get(_AF):H=B.MakeText_FreeList(A.get(_C),titleName=_D);I={_AF:A.get(_AF),_D:A.get(_A0),_A5:H};C.append(I)
		except Exception as J:print(J);return[]
		return C
	def Get_Pass_VodList(B,collectionId,obj_id):
		C=[]
		try:
			M=_Bw.format(B.API_DOMAIN,collectionId);N={_N:_J,_W:_l,_P:_Q,_e:_Z,_f:str(B.PAGE_LIMIT),_p:_S,_AA:_H,_AB:_H,_AJ:_H,_i:_AU};D=B.callRequestCookies(_I,M,payload=_A,params=N,headers=_A,cookies=_A)
			if D.status_code not in[200]:return[]
			O=json.loads(D.text).get(_C)
			for E in O:
				if E.get(_AF)==obj_id:
					for A in E.get(_C):
						F=G=H=I=''
						if _AR in A.get(_B):F=A.get(_B).get(_AR)+_A2
						if _n in A.get(_B):G=A.get(_B).get(_n)+_a
						if _At in A.get(_B):H=A.get(_B).get(_At)+_AY
						if _n in A.get(_B):I=A.get(_B).get(_n)+_a
						J=''
						if A.get(_m)not in[{},_A]:
							for P in A.get(_m).get(_A3):J+=P.get(_A3)
						K=''
						if A.get(_u)!=_A:K=','.join(str(A)for A in A.get(_u))
						L=[]
						for Q in A.get(_Ao):L.append(Q.get('tag'))
						R={_G:A.get(_G),_D:A.get(_D),_j:{_V:F,_r:G,_AL:H,_s:I},_AC:A.get('ageRating'),_v:A.get(_X),_BK:A.get(_BK),_m:J,_AD:A.get(_AZ),_u:K,_BB:L};C.append(R)
					break
		except Exception as S:print(S);return[]
		return C