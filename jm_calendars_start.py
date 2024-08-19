# Import the calendar module
import calendar

def main():
    # # Create a plain text calendar
    text_cal = calendar.TextCalendar(calendar.SUNDAY)
    # text_cal_str = text_cal.formatmonth(2024, 1, 0, 0)
    # print(text_cal_str)
    
    # Create a html formatted calendar
    # html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
    # html_cal_str = html_cal.formatmonth(2024, 1)
    # print(html_cal_str)

    # Loop over the days of the month
    # Zeroes means day of overlapping month
    # for i in text_cal.itermonthdays(2024,8):
    #     print(i)
    
    # for any_month_name in calendar.month_name:
    #     print(any_month_name)
        
    # for any_day in calendar.day_name:
    #     print(any_day)
    
    print("Team meetings will be on")
    for the_month in range(1,13):
        cal = calendar.monthcalendar(2024, the_month)
        weekone = cal[0]
        weektwo = cal[1]
        print("weekone", weekone)
        print("weektwo", weektwo)
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]
        print(calendar.month_name[the_month], meetday)
    

if __name__ == "__main__":
    main()