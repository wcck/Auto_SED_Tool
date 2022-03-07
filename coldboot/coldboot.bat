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

	if %1 == RESTART GOTO RESTART
	echo Unrecognized option - try RESTART
	GOTO STOP

	:RESTART
	echo Restarting Test by deleting count.txt
	del %CD%\count.txt


	:START
	rem ------------  settings -----------------
	set RESET_TIME=10:58 AM
	set SHUTDOWN_DELAY=20
	set CYCLES=1
	set STABILITY_DELAY=20

	rem rem count.txt holds the number of iterations
	rem rem if count.txt already exists, do not reset COUNTER to 0
	rem if EXIST %CD%\count.txt goto COUNTEXIST
	rem set /a COUNTER=0
	rem goto INCREMENTCOUNTER

	rem rem if count.txt exists, pull the value from count.txt
	rem rem and use it as the iteration count.
	rem :COUNTEXIST
	rem set /p COUNTER=<%CD%\count.txt


	rem rem increment the iteration count if the amount of cycles is not reached
	rem :INCREMENTCOUNTER
	rem if %COUNTER% GEQ %CYCLES% goto PASS
	rem set /a COUNTER=%COUNTER%+1
	rem echo %COUNTER% > %CD%\count.txt
	rem echo Iteration %COUNTER% of %CYCLES%
	time %RESET_TIME%
        
	timeout /t %STABILITY_DELAY%

	rem if %errorlevel%==1 goto FAIL
	goto CYCLE

	:CYCLE
	shutdown -s -t %SHUTDOWN_DELAY% -c "Cold Boot cycle test - Iteration %COUNTER% :: Press enter in command window to abort"
	goto WAITFORABORT

	:WAITFORABORT
	echo Abort shutdown?
	pause
	shutdown -a
	goto STOP


	rem :PASS
	rem echo =================================================
	rem echo %COUNTER% of %CYCLES% cold boot cycles executed
	rem echo TEST PASSED
	rem echo =================================================
	rem goto STOP

	rem :FAIL
	rem echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	rem echo %COUNTER% of %CYCLES% cold boot cycles executed
	rem echo TEST FAILED
	rem echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	goto STOP

	:STOP
	shutdown -a
	pause

