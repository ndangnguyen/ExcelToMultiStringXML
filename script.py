#Created by nguyen.nguyendang on 26/3/2019

import pandas as pd;
from pandas import ExcelWriter
from pandas import ExcelFile
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

MODE = sys.argv[1]
EXCEL_FILE_NAME = '../../' +sys.argv[2]
XML_FILE_NAME = sys.argv[3]
USE_SHEET_NAME = sys.argv[4]
SHEET_NAME = sys.argv[5]

languages = ['en','fr','de','es','it','br','tr','th','vi','ar','pl','ru','latam']

def makeDirectory(lang):
    path = os.getcwd() + '../../../Output'
    if lang == 'en':
        path += r'/values/'
    elif lang == 'latam':
        path += r'/values-le/'
    else:
        path += r'/values-'+lang+r'/'
    
    print 'Creating directory ' + str(path)
    try:  
        os.mkdir(path)
    except OSError:  
        print 'Folder exist ... continue...'
    else:  
        print 'Successfully created the directory ' + str(path)
    return path

def generate():
    if USE_SHEET_NAME == '1':
        df = pd.read_excel(EXCEL_FILE_NAME, sheet_name=SHEET_NAME, encoding='utf-8')
    else:
        df = pd.read_excel(EXCEL_FILE_NAME, encoding='utf-8')

    for lang in languages:
        dir = makeDirectory(lang)
        print 'Generating ' +lang.upper()+ ' at: ' + dir

        if MODE=='0':
            file = open(dir + XML_FILE_NAME, 'w+')
            file.write('<?xml version="1.0" encoding="utf-8"?>\n')
            file.write('<resources>\n')
        else:
            with open(dir + XML_FILE_NAME, "r") as file:
                lines = file.readlines()
            with open(dir + XML_FILE_NAME, "w") as file:
                for line in lines:
                    if line.strip("\n") != "</resources>":
                        file.write(line)
            file = open(dir + XML_FILE_NAME, 'a+')

        for i in df.index:
            file.write('\t<string name="' + str(df["::ID::"][i]).encode("utf-8").strip() + '">' + str(df["::"+lang+"::"][i]).encode("utf-8").strip()  + '</string>\n')

        file.write('</resources>\n')
        file.close()
        print 'Done!\n'

def main():
    # os.remove(os.getcwd()+'/Output')
    try:  
        print 'Creating Output folder...'
        os.mkdir(os.getcwd()+'../../../Output')
    except OSError:  
        print 'Folder exist ... continue...\n'
    else: 
        print 'Successfully created the directory' + os.getcwd()+'/Output\n'

    generate()
   

main()


