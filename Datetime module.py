

from datetime import date
from datetime import timedelta
today = date.today()
print("today date is:",today)
yesturday = today - timedelta(days = 1)
print("yesturday date is:",yesturday)