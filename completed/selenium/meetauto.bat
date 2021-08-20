echo off
@REM TODO write log in txt file
:loop
cls
echo Starting script...
echo Started: %date% %time%
python "C:\Users\Flores\Joey-Repositories\Python-Projects\completed\selenium\meetopener.py"
echo.
echo Ending script...
echo Completed: %date% %time%
echo waiting for 40 minutes...
timeout /t 2400 /nobreak > nul
goto loop