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
        
versionCode_str = str(versionCode_int)

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
        
version3 = str(third_int)
versionName_str = version1+'.'+version2+'.'+version3

#write AndoridManifest.xml
f = open('./AndroidManifest.xml','r')
xmlLines = f.readlines()
i = 0
for line in xmlLines:
    if not line.find('android:versionCode') == -1:
        one = line.find('=')
        three = line.rfind('\"')
        print one
        line2 = line[:(one+2)]+versionCode_str+line[three:]
        print line2
        xmlLines[i] = line2
    elif not line.find('android:versionName') == -1:
        two = line.find('=')
        three = line.rfind('\"')
        print two
        line3 = line[:(two+2)]+versionName_str+line[three:]
        print line3
        xmlLines[i] = line3
    else:
        xmlLines[i] = line
    i = i + 1
    
f = open('./AndroidManifest.xml','w')
for line in xmlLines:
    f.write(line)
f.close()

print 'Write AndroidManifest.xml success'

#write ant_utf8.properties
fp = open('./ant_utf8.properties','r')
lines = fp.readlines()
i = 0
for line in lines:
    if not line.find('app_version=v') == -1:
        line2 = 'app_version=v'+versionName_str+'\n'
        lines[i] = line2
    elif not line.find('build.type=') == -1:
        if int(sys.argv[1]) == 1:
            lines[i] = 'build.type=release\n'
        elif int(sys.argv[1]) == 2:
            lines[i] = 'build.type=debug\n'
    else:
        lines[i] = line
    i = i + 1
    
f = open('./ant_utf8.properties','w')
for line in lines:
    f.write(line)
f.close()

print 'Write ant_utf8.properties success'


