#!c:\devtools\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PyInstaller==3.4','console_scripts','pyi-set_version'
__requires__ = 'PyInstaller==3.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('PyInstaller==3.4', 'console_scripts', 'pyi-set_version')()
    )
