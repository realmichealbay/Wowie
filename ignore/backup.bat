@echo off
del F:\umad.archive\*.* /s /q
xcopy E:\ F:\umad.archive /v /s /h
echo Finished