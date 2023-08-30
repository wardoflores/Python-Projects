cd C:\Users\Flores\coalemus\Python-Projects\fileorganizer\windowsfiles
echo off
:loop
SET /p orgdir=Put path to be organized here:
py organize.py %orgdir%
goto loop