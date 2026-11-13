__author__="NightRain"
yqQsrovSChuTatiwOjVXAzdWePbmgD=int
import os
import sys
import xbmcaddon,xbmcvfs
import urllib
__cwd__=xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('path'))
__lib__=os.path.join(__cwd__,'resources','lib')
sys.path.append(__lib__)
from spotvRun import*
def get_params():
 p=urllib.parse.parse_qs(sys.argv[2][1:])
 for i in p.keys():
  p[i]=p[i][0]
 return p
yqQsrovSChuTatiwOjVXAzdWePbmgE=rTOxgawICeoqHGbsBALPiVFjlfdpcN(sys.argv[0],yqQsrovSChuTatiwOjVXAzdWePbmgD(sys.argv[1]),get_params()) 
yqQsrovSChuTatiwOjVXAzdWePbmgE.spotv_main()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
