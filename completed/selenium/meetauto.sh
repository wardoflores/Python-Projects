:loop
cls
echo Started: %date% %time%
echo Exiting script if today is a weekend...
echo.
for /f %%i in ('powershell ^(get-date^).DayOfWeek') do set dow=%%i
if %dow% == Saturday goto exit 
if %dow% == Sunday goto exit
echo Starting script...
python "C:\Users\Flores\Joey-Repositories\Python-Projects\completed\selenium\meetopener.py"
echo.
echo Ending script...
echo Completed: %date% %time%
echo waiting for 40 minutes...
timeout /t 2400 /nobreak > nul
goto loop
:exit
exit