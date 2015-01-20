@ECHO ON & setLocal enableDelayedExpansion
@color 5e
@echo ============================================准备工作=====================================================
@rem ==============================start,以下这些环境变量需要根据自己机器来配置=========================
@set CUR_DIR=%~dp0
@set TARGET_DIR=%CUR_DIR%out\target\
@cd %CUR_DIR%
@rem 先转码，把ant.properties中的中文转成utf-8
@call native2ascii -encoding utf-8 ant.properties ant_utf8.properties
@rem 删除目标目录下的所有文件，不包括文件夹
@rem del %TARGET_DIR%
@rem ---------------------------------------------------------------------------------------------------------
@set chooseVersion=1
@rem 生成不同版本的apk
@echo .
@echo .
@echo .
@echo .
@echo .
@echo =========打包不同版本的apk菜单===========
@echo * * * * * * * * * * * * * * * * * * * * *
@echo *                                       *
@echo *   1: release版本                      *
@echo *                                       *
@echo *   2: debug版本                        *
@echo *                                       *
@echo *   3: 退出程序                         *
@echo *                                       *
@echo * * * * * * * * * * * * * * * * * * * * *
@echo =========================================
@echo .
@echo .
@echo .
@echo .
:menu
@set /p input=输入要打包的版本编号:
@if "%input%"=="1" goto release
@if "%input%"=="2" goto debug
@if "%input%"=="3" goto end
@echo =========ERROR:请输入正确的编号==============
@goto menu
:release
@cd %projectpath%
@echo 你选择的是   - release版本 
@echo           .
@echo           .         .
@echo           .         .       .
@set chooseVersion=1
@call ant copy_files_release

@goto secondstep
:debug
@cd %projectpath%
@echo 你选择的是  - debug版本
@echo           .
@echo           .         .
@echo           .         .       .
@set chooseVersion=2
@call ant copy_files_debug

@goto secondstep

:secondstep
@rem 确定AndroidManifest的版本号
@rem 打印当前版本号给用户
@echo ======================当前版本号===========================
@call python %CUR_DIR%\config\getVersion.py
@echo ========根据您的选择，我们为您私人定制一个版本号===========
@call python %CUR_DIR%\config\chooseVersion.py %chooseVersion%
@echo ===========================================================
@set /p input=同意请输入1，其他键手动输入版本：
@if "%input%"=="1" goto thirdstep
:version
@set /p input=手动输入一个VersionCode：
@set versionCode=%input%
@set /p input=手动输入一个VersionName:
@set versionName=%input%
@echo ===========您输入的版本号如下：===================
@echo VersionCode = %versionCode%
@echo VersionName = %versionName%
@set /p input=确定请输入1，其他键重新输入：
@if "%input%"=="1" goto forthsetp
@goto version

:thirdstep
@rem 用定制的versioncode和versionname,修改AndroidManifest的版本号
@call python %CUR_DIR%\config\setVersionOne.py %chooseVersion%
goto fifthstep

:forthsetp
@rem 用手动输入的versioncode和versionname，修改版本号
@call python %CUR_DIR%\config\setVersionTwo.py %versionCode% %versionName% %chooseVersion%
goto fifthstep

:fifthstep
@rem 正式开始编译
@call ant android_release
@echo 编译APK完成

:end
@echo ====================!!程序执行结束!!=======================
@pause