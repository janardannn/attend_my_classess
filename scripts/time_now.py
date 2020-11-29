from datetime import datetime
from pytz import timezone
from tzlocal import  get_localzone

time_format = "%H:%M"

# converting timezone from UTC to IST and getting time as of now
current_time = datetime.now(timezone('UTC')).astimezone(get_localzone())
# time as per IST
current_indian_time = current_time.strftime(time_format)
