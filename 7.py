from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz

today = JalaliDate.today()

# x = JalaliDateTime(today.year, today.month, today.day, 0, 0, 0, 0, pytz.utc).strftime("%B")
# print(x)

x = JalaliDateTime(today.year, today.month, today.day, 0, 0, 0, 0, pytz.utc).strftime("%A")
print(x)
