echo off
:loop
cls
echo Starting script...
echo Started: %date% %time%
python "C:\Users\Flores\Joey-Repositories\Python-Projects\completed\selenium\meetopener.py"
echo Ending script...
echo Completed: %date% %time%
echo waiting for 50 minutes...
timeout /t 3000 /nobreak > nul
goto loop