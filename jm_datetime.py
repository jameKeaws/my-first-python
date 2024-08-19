# Basics of date and time
from datetime import date, time, timedelta, datetime

# TODO Create a new date object
d1 = date.today()
print(d1)

# TODO Create a new time object
t1 = time(12, 30, 30)
print(t1)

# TODO Create a new datetime object
dt1 = datetime.now()
print(dt1)

# TODO Access the different components of the date and time objects
# print(d1.day)
# print(d1.month)
# print(d1.year)

# print(t1.hour)
# print(t1.minute)
# print(t1.second)


# days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print(dt1.month)
# print(dt1.weekday())
# print(days[dt1.weekday()])

# TODO Modify the values of date and time objects, use the replace function
d1 = d1.replace(year=2024,month=10,day=13)
print(d1)
t1 = t1.replace(hour=5)
print(t1)
dt1 = dt1.replace(year=2024,month=10,day=14)
print(dt1)