import xml.dom.minidom
import sys

#write AndoridManifest.xml
f = open('./AndroidManifest.xml','r')
xmlLines = f.readlines()
i = 0
for line in xmlLines:
   if not line.find('android:versionCode') == -1:
      one = line.find('=')
      three = line.rfind('\"')
      print one
      line2 = line[:(one+2)]+sys.argv[1]+line[three:]
      print line2
      xmlLines[i] = line2
   elif not line.find('android:versionName') == -1:
      two = line.find('=')
      three = line.rfind('\"')
      print two
      line3 = line[:(two+2)]+sys.argv[2]+line[three:]
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
        line2 = 'app_version=v'+sys.argv[2]+'\n'
        lines[i] = line2
    elif not line.find('build.type=') == -1:
        if int(sys.argv[3]) == 1:
            lines[i] = 'build.type=release\n'
        elif int(sys.argv[3]) == 2:
            lines[i] = 'build.type=debug\n'
    else:
        lines[i] = line
    i = i + 1
    
f = open('./ant_utf8.properties','w')
for line in lines:
   f.write(line)
f.close()

print 'Write ant_utf8.properties success'
