set arg=%1
if "%arg%"=="" (
	C:\Python36\python.exe %~dp0BLHX.py
) else (
	C:\Python36\python.exe %1
)
@pause
