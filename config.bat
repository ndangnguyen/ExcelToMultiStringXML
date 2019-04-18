@echo off

REM    _____ ____  _   _ ______ _____ _____ 
REM   / ____/ __ \| \ | |  ____|_   _/ ____|
REM  | |   | |  | |  \| | |__    | || |  __ 
REM  | |   | |  | | . ` |  __|   | || | |_ |
REM  | |___| |__| | |\  | |     _| || |__| |
REM   \_____\____/|_| \_|_|    |_____\_____|

REM make sure files name have extensions (excel: .xls && xml: .xml)
SET EXCEL_FILE_NAME=excel_form.xls
SET XML_FILE_NAME=multi_game_strings.xml

REM if you want to use sheet name
SET USE_SHEET_NAME=0
SET SHEET_NAME=GLClassicContent

REM set running mode
REM OVERRIDE MODE = 0
REM MERGE MODE = 1
SET MODE=0