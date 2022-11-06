from datetime import datetime
dt = datetime.now()

year = ""
while not(year.isdigit()):
    year = input("What year where you born in?  ")

month = ""
while not(month.isdigit()):
    month = input("What month where you born in?(January - 1, Febuary - 2, ect.)  ")

day = ""
while not(day.isdigit()):
    day = input("What day where you born on?")

cYear = dt.year
cMonth = dt.month
cDay = dt.day
bDay = False
yearsOld = cYear - int(year)

if not(int(month) <= cMonth and int(day) <= cDay):
    yearsOld-=1
else:
    bDay = True
if bDay:
    if cMonth == int(month):
        daysOld = cDay - int(day)
    else:
        daysOld = cDay
else:
    daysOld = cDay

monthsOld = cMonth - int(month)
if monthsOld < 0:
    monthsOld += 12

print(str(yearsOld)+ " years old, "+str(monthsOld)+" months old, "+str(daysOld)+" days old")