cd C:\Users\Flores\Joey-Repositories\Python-Projects\completed\fileorganizer\windowsfiles
echo off
:loop
SET /p orgdir=Put path to be organized here:
py organize.py %orgdir%
goto loop