@echo off
rem 双击这个文件 = 直接用 VS Code 打开练习仓库，省掉找文件夹的时间
cd /d "%~dp0"
if exist "D:\Daima\Microsoft VS Code\bin\code.cmd" (
    start "" "D:\Daima\Microsoft VS Code\bin\code.cmd" "%~dp0"
) else (
    echo 没找到 VS Code，请确认安装路径后修改本文件第 5 行
    pause
)
