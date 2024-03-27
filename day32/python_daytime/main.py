import datetime as dt

now = dt.datetime.now()  # returns a datetime object with this 2023-08-25 13:39:56.496262
print(now)
year = now.year  # returns just the year as an int
print(year)
month = now.month
day = now.day
weekday = now.weekday()  # returns number day of the week (counted from 0)
print(weekday)

# we can create our custom datetime object. By default it includes the hour parameter. If we don't provide an hour parameters it defaults to 00:00:00
date_of_birth = dt.datetime(year=1989, month=3, day=22)
print(date_of_birth)

new_date_of_birth = dt.datetime(year=1989, month=3, day=22, hour=20, minute=15)
print(new_date_of_birth)
