SETLOCAL ENABLEDELAYEDEXPANSION

call CONFIG.bat

SET projectDir=%cd%
SET arg1=%MODE%
SET arg2=%EXCEL_FILE_NAME%
SET arg3=%XML_FILE_NAME%

SET arg4=%USE_SHEET_NAME%
SET arg5=%SHEET_NAME%


cd %cd%"\Library\Python27"
call python "..\..\script.py" %arg1% %arg2% %arg3% %arg4% %arg5%