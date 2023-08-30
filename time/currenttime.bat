echo off
echo Started: %date% %time%
FOR /F "TOKENS=1 DELIMS=:" %%A IN ('TIME/T') DO SET HH=%%A
FOR /F "TOKENS=2 DELIMS=:" %%A IN ('TIME/T') DO SET MM=%%A
echo %HH%:%MM%
echo %DATE%
echo Completed: %date% %time%
rem only print the weekday please
