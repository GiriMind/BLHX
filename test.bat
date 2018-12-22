set arg=%1
if "%arg%"=="" (
	%~dp0Python36\python.exe %~dp0old.py
) else (
	%~dp0Python36\python.exe %1
)
@pause
