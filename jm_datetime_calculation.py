# Perform date time calculation using timedelta
import datetime

# Create some date objects
# 10 am
dt1 = datetime.datetime(2024, 1, 15, 10)
# 3 pm
dt2 = datetime.datetime(2024, 1, 20, 15)
# TODO Date and times can be compared
print(dt1 < dt2)
print(dt2 < dt1)

# Subtracting one date from another creates a timedelta
# delta = dt2 - dt1
# timedeltas have components
# print(delta)
# print(delta.days)
# print(delta.seconds)


# TODO timedeltas can be used to perform date math
now = datetime.datetime.now()
oneyear_delta = datetime.timedelta(days=365)
oneweek_delta = datetime.timedelta(weeks=1)

print("One year from now will be", now + oneyear_delta)
print("One week from now will be", now + oneweek_delta)
print("One week ago", now - oneweek_delta)