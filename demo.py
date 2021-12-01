from datetime import datetime
if __name__=='__main__':     

    import locale
    locale.setlocale(locale.LC_ALL , 'fr_FR.UTF-8') 

from demo2 import getmonth

from datetime import datetime

getmonth(datetime(2021,4,12))