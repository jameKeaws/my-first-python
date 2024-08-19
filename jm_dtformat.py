import datetime

# Create a datetime for today
now = datetime.datetime.now()

# Print various day and month formatting
# print(now.strftime("%a, %A, %w, %d"))
# print(now.strftime("%b, %B, %m"))


# Print various time formatting
# print(now.strftime("%H, %I, %M, %S, %p"))

# Locale-specific
# print(now.strftime("%c"))
# print(now.strftime("%X"))

# Short date format (m/d/y)
output = now.strftime("%m,%d,%y")
print("today is ", output)

# Long date format (Day, number, month, year)
ldf_output = now.strftime("%A, %d, %B, %Y")
print("Long date format: ", ldf_output)

# Short date and time
sdt_output = now.strftime("%m/%d/%y %I:%M %p")
print("Short date with time: ", sdt_output)