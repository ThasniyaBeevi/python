from datetime import date

def day_between(date1,date2):
    delta = date2 - date1
    print(delta.days)

f_date = date(2000, 2, 28)
l_date = date(2001, 2, 28)
day_between(f_date,l_date)
