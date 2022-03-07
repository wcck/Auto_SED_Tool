        timeout /t 5
	@echo off 

	:: BatchGotAdmin
	:-------------------------------------
	REM  --> Check for permissions
	>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

	REM --> If error flag set, we do not have admin.
	if '%errorlevel%' NEQ '0' (
    	echo Requesting administrative privileges...
    	goto UACPrompt
	) else ( goto gotAdmin )

	:UACPrompt
    	echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    	echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

    	"%temp%\getadmin.vbs"
    	exit /B

	:gotAdmin
    	if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    	pushd "%CD%"
    	CD /D "%~dp0"
	:--------------------------------------
	@echo off
                      
	echo Coldboot cycle test

	if ""%1"" == """" GOTO START

	:START
	rem ------------  settings -----------------
	set RESET_TIME=10:58 AM
	set SHUTDOWN_DELAY=20
	set CYCLES=1
	set STABILITY_DELAY=20

	time %RESET_TIME%        
	timeout /t %STABILITY_DELAY%

	goto CYCLE

	:CYCLE
	shutdown -s -t %SHUTDOWN_DELAY% -c "Cold Boot cycle test - Iteration %COUNTER% :: Press enter in command window to abort"
	goto WAITFORABORT

	:WAITFORABORT
	echo Abort shutdown?
	pause
	shutdown -a
	goto STOP

	:STOP
	shutdown -a
	pause

