set arg=%1
if "%arg%"=="" (
	C:\Python37\python.exe %~dp0old.py
) else (
	C:\Python37\python.exe %1
)
@pause
