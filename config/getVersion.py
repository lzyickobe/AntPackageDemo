import xml.dom.minidom

dom = xml.dom.minidom.parse('./AndroidManifest.xml')
root = dom.documentElement
print 'Android'+root.nodeName

versionCode = root.getAttribute('android:versionCode')
print 'VersionCode = '+versionCode

versionName = root.getAttribute('android:versionName')
print 'VersionName = '+versionName