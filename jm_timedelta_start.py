# Import date , time , and datetime classes from datetime module
from datetime import date
from datetime import time
from datetime import datetime 
from datetime import timedelta

def main():
    # # Construct a timedelta and print it
    # print(timedelta(days=365, hours=5, minutes=1))
    
    # # Print today's date
    # now = datetime.now()
    # print("Today is", now)
    
    # # Print today's date one year from now
    # print("One year from now it will be", str(now + timedelta(days=365)))
    
    # # Create a time delta that uses more than one argument
    # print("In two weeks and 3 days from now it will be", str(now + timedelta(weeks=2, days=3)))
    
    # # Calculate date 1 week ago, formatted as string
    # t = datetime.now() - timedelta(weeks=1)
    # s = t.strftime("%A %B %d, %Y")
    # print("One week ago it was", s)
    
    # How many days until April fools day
    today = date.today()
    afd = date(today.year, 4, 1)
    
    if afd < today:
        print("April fool's day already went by", ((today-afd).days) )
        afd = afd.replace(year = today.year+1)
        
    time_to_afd = afd - today
    print("It is this many number of days before next April fools day", time_to_afd.days)
    
if __name__ == "__main__":
    main()