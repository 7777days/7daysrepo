__author__='NightRain'
import os,sys,xbmcaddon,xbmcvfs,urllib
__cwd__=xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('path'))
__lib__=os.path.join(__cwd__,'resources','lib')
sys.path.append(__lib__)
from coupangRun import*
def get_params():
	p=urllib.parse.parse_qs(sys.argv[2][1:])
	for i in p.keys():p[i]=p[i][0]
	return p
runObj=CoupangRun(sys.argv[0],int(sys.argv[1]),get_params())
runObj.coupang_main()