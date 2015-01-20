import xml.dom.minidom
import sys

dom = xml.dom.minidom.parse('./AndroidManifest.xml')
root = dom.documentElement

versionCode = root.getAttribute('android:versionCode')
versionCode_int = int(versionCode)
if versionCode_int % 2 == 0:
    if int(sys.argv[1]) == 1:
        versionCode_int = versionCode_int + 1
    elif int(sys.argv[1]) == 2:
        versionCode_int = versionCode_int + 2
    else:
        versionCode_int = versionCode_int + 2
else:
    if int(sys.argv[1]) == 1:
        versionCode_int = versionCode_int + 2
    elif int(sys.argv[1]) == 2:
        versionCode_int = versionCode_int + 1
    else:
        versionCode_int = versionCode_int + 1
        
print 'VersionCode = ',(versionCode_int)

versionName = root.getAttribute('android:versionName')
nameLength = len(versionName)
first = versionName.index('.')
version1 = versionName[:(first)]

version_remain = versionName[(first)+1:]
second = version_remain.index('.')
version2 = version_remain[:(second)]

third = version_remain[(second)+1:]
third_int = int(third)
if third_int % 2 == 0:
    if int(sys.argv[1]) == 1:
        third_int = third_int + 1
    elif int(sys.argv[1]) == 2:
        third_int = third_int + 2
    else:
        third_int = third_int + 2
else:
    if int(sys.argv[1]) == 1:
        third_int = third_int + 2
    elif int(sys.argv[1]) == 2:
        third_int = third_int + 1
    else:
        third_int = third_int + 1
        
print 'VersionName = %s.%s.%d' % (version1,version2,third_int)        


        
        
