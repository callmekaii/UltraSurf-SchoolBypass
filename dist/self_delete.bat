@echo off
REM Wait a moment to ensure the program finishes
timeout /t 2 > nul

REM Delete the executable in the current directory (relative path)
del /f /q "%~dp0UltrasurfDownloader.exe"

REM Delete the batch file itself
del /f /q "%~f0"

exit