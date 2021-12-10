import os

import datetime
os.chdir('c:/Users/DELL/Desktop/Lab Work/python/lab 5/list_file_date')
for f in os.listdir():
    
    if f.endswith(".txt"):
        day=f[0:2]
        
        month=f[2:4]
        
        year=f[4:]
        
        month_name = datetime.date(1900, int(month), 1).strftime('%b')

        print(month_name,"-",f)

