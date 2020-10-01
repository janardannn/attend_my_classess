from datetime import datetime
from pytz import timezone
from tzlocal import  get_localzone


def time_now():
	time_format = "%H:%M:%S"
	current_time = datetime.now(timezone('UTC')).astimezone(get_localzone())
	current_indian_time = current_time.strftime(time_format)
	return current_indian_time

def today_date():
	date_format = "%d" + "/" + "%m" + "/" + "%y"
	current_time = datetime.now(timezone('UTC')).astimezone(get_localzone())
	current_indian_date = current_time.strftime(date_format)
	return current_indian_date

