@echo off
@python -c "import consolemenu"
if ERRORLEVEL 1 GOTO MISSINGLIB
GOTO :NORM
:MISSINGLIB
setlocal
echo -----------------------------------------------------------------------------------
SET /P AREYOUSURE=You're missing the console-menu prerequesite. Do you want us to install it for you?(Y/[N]): 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END
endlocal
python -m pip install --user console-menu
echo -----------------------------------------------------------------------------------
echo We finished installing the prerequesites!
pause

:NORM
python autodice.py

:END