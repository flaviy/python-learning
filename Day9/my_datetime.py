import datetime

# Get the current date and time
now = datetime.datetime.now()
print(now)

my_date = datetime.date(2021, 12, 31)
print(my_date)  # 2021-12-31
my_time = datetime.time(23, 59, 59)
print(my_time)  # 23:59:59

print(my_date.year)  # 2021
print(my_date.month)  # 12
print(my_date.day)  # 31

print(my_time.hour)  # 23
print(my_time.minute)  # 59

print(my_date.ctime())

print(my_date.today())  # will return today date

my_date = datetime.datetime(2021, 12, 31, 23, 59, 59)
print(my_date)

my_date = my_date.replace(month=10)
print(my_date)  # 2021-10-31 23:59:59

birthday = datetime.date(1984, 8, 7)
today = datetime.date.today()
age = today.year - birthday.year
print(age)  # 34
age_days = (today - birthday).days
print(age_days)  # 14578

age_hours = age_days * 24
print(age_hours)  # 349872

wokup = datetime.datetime(2024, 12, 31, 7, 15)
went_to_bed = datetime.datetime(2024, 12, 31, 23, 59)
wakefullness = went_to_bed - wokup
print(wakefullness)  # 16:44:00


today_date = datetime.date.today()
print(today_date)

now_time = datetime.datetime.now()
current_minutes = now_time.minute

print(current_minutes)


