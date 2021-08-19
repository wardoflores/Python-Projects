echo off
:loop
echo Starting script...
echo Started: %date% %time%
python "C:\Users\Flores\Joey-Repositories\Python-Projects\completed\selenium\meetopener.py"
echo Ending script.
echo Completed: %date% %time%
timeout /t 7200 /nobreak > nul
@REM wait for 2 hours
goto loop