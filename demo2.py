if __name__=='__main__':     

    import locale
    locale.setlocale(locale.LC_ALL , 'fr_FR.UTF-8') 

from datetime import datetime

def getmonth(date):
    print(date.strftime("%b"))







date =datetime(2021,12,12)

print(date.strftime("%b"))

class test:
    name="oronce"
    
    def getname(self):
        print(self.name)
        
        
print(test().name)
        