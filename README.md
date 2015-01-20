## Android多渠道打包工具(完美支持中文属性)

### 功能介绍
1. 支持动态配置属性
在工程目录下config目录的build_config.xml，可以配置一些自己的属性，debug和release会根据不同文件夹的内容打包。
2. 支持一次生成多个渠道包
在ant.properties中，渠道名字可以使用英文或中文，用英文逗号分开即可。工具会自动生成配置的渠道包。
3. 支持自动更新版本号和手动设置版本号
执行AntGenerateApk.bat，cmd会显示当前版本号和修改版本号的方式。
4. 支持生成debug和release、release默认添加混淆
可以在debug和release这两个文件夹中放入不同的project.properties，用于控制混淆。如不需要控制，也可以删除这两个文件夹的project.properties。
5. 支持中文的配置信息
可以在ant.properties中加入中文的配置信息，比如ant.app.name是中文，最后的apk名字会使用这个名字。渠道名也可以使用中文。


详细介绍可参考我的博文：[Android多渠道打包工具](http://lzyblog.com/2015/01/20/AndroidAntPackage/)