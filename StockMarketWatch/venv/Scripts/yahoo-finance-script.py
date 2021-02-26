#!C:\Users\T1Vibudh\Desktop\GitHub\StockMarketWatch\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'yahoo-finance==1.4.0','console_scripts','yahoo-finance'
__requires__ = 'yahoo-finance==1.4.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('yahoo-finance==1.4.0', 'console_scripts', 'yahoo-finance')()
    )
