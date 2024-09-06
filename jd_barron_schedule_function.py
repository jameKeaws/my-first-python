import time
import sched

def schedule_function(event_time, function, *args):
    # 
    zcheduler = sched.scheduler(time.time, time.sleep)
    # Schedule the event at absolute event_time
    # Set the priority to 1
    # function = function to execute 
    zcheduler.enterabs(event_time, 1, function, args)
    print(f"{function.__name__}() is scheduled for {time.asctime(time.localtime(event_time))}")
    zcheduler.run()
    
# Schedule the event 2 seconds from now
schedule_function( time.time() + 2, print, "Howdy partner", "How are you")