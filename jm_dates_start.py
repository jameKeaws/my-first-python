# Import date , time , and datetime classes from datetime module
from datetime import date
from datetime import time
from datetime import datetime 

def main():
    pass
    # Get today's date from the simple today() method from date class
    
    today = date.today()
    print("Today's date is :", today)
    
    # Print out the date's individual components
    print("Date components", today.day, today.month, today.year)
    
    # Retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is", today.weekday())
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("which is a", days[today.weekday()])
    
    # Get today's date from the datetime class
    todaydt = datetime.now()
    print("Today's date as per datetime.now() :", todaydt)
    
    # Get the current time
    t = datetime.time(datetime.now())
    print("Today's current time as per datetime.time(datetime.now()) :", t)

if __name__ == "__main__":
    main()