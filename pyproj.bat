@rem Sized for a half full window. Some scripts could be found in other repository.
echo off
echo.
echo Current Python APIs are:
echo. 
echo discordbot 
echo wolfram
echo TTS
echo voassist
echo.
echo Current Python scripts are:
echo .
echo meet
echo netspeed
echo clicker ( 's' start/stop 'e' exit )
echo organize (input abspath, BE CAREFUL)
echo textspam
echo filespam
echo keylogger
echo calculator
echo meditate
echo birthday
echo .
echo Current batch scripts are:
echo .
echo root
echo pyserver
echo apache
echo apacherun
echo apachestop
echo apacherestart
echo .
rem Aliases
doskey root=cd C:\Windows\system32
rem server scripts not in repo
doskey apache=cd C:\Apache24\bin
doskey apacherun=C:\Apache24\bin\httpd.exe -k start
doskey apachestop=C:\Apache24\bin\httpd.exe -k stop
doskey apachereboot=C:\Apache24\bin\httpd.exe -k restart
doskey pyserver=python "pyserver project directory"
rem Repo scripts
doskey organize=CALL "organize.bat"
doskey calculator=python "calculator project directory"
doskey simplespam=python "simplespam project directory"
doskey filespam=python "navyspam project directory"
doskey spam=python "spam project directory"
doskey clicker=python "clicker project directory"
doskey idleclicks=python "idleclicks project directory"
doskey keylogger=python "keylogger project directory"
doskey birthday=python "birthday project directory"
doskey meditate=python "meditate project directory"
doskey wolfram=python "wolframalpha project directory"
doskey meet=python "meetopener project directory"
doskey TTS=python "TTS project directory"
doskey voassist=python "voassist project directory"
rem scripts not inside of this repository
doskey discordbot=CALL "discorbot.bat"
doskey redditbot=CALL "redditbot.bat"
doskey twitterbot=CALL "twitterbot.bat"
doskey adbcheck=CALL "adbstart.bat"
doskey scrcpy=CALL "scrcpystart.bat"
