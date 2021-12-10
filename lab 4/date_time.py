from datetime import datetime
now = datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current year:", now.year)
print("Current month:", now.strftime('%B'))

print("Week number of the year :",now.strftime("%V"))
print("Week day of the week :",now.isoweekday())
day_of_year = datetime.now().timetuple().tm_yday
print("day of year :",day_of_year)
print("Day of month :",now.strftime("%d"))
print("Day of week :",now.isoweekday())
