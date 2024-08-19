from datetime import datetime

def main():
    # Date Formatting
    now = datetime.now()
    print("datetime.now()", now)
    # %y%Y - Year, %a%A - weekday, %b%B - month, %d - day of month
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%A, %d, %B, %y"))
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x and Locale time: %X"))
    
    # Time formatting
    # %I/%H - 12/24 hour format, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time 12 hr format: %I:%M:%S %p"))
    print(now.strftime("Current time 24 hr format: %H:%M:%S %p"))

if __name__ == "__main__":
    main()