from datetime import datetime
import pytz


portland_time  = datetime.now()
NewYork_time = pytz.timezone('America/New_York')
datetime_NY =datetime.now(NewYork_time)
London_time = pytz.timezone('Europe/London')
datetime_LD =datetime.now(London_time)

print(portland_time)
print(datetime_NY)
print(datetime_LD)

def open_or_close(country_time):
    if 5<= country_time.hour <= 17:
      print("Open")
    else:
      print("close")

open_or_close(portland_time)
open_or_close(datetime_NY)
open_or_close(datetime_LD)
