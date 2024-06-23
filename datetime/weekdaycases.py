import time
import datetime
from datetime import datetime

hour_now_format = datetime.now().isoformat(timespec='hours')   
hour_now = str(hour_now_format[11:13])
print("Hour now is: " + hour_now)

min_now_format = datetime.now().isoformat(timespec='minutes')   
min_now = str(min_now_format[14:16])
print("min now is: " + min_now)

# if datetime.weekday(0) and datetime.hour(7): 

def first_mon_sub():
    if datetime.today().weekday() == 0: # Monday
        if hour_now == "08": # 8am
            print("test1")

def first_tue_sub():
    if datetime.today().weekday() == 1: # Thursday
         if hour_now == "08": # 8am
            print("test1")

def first_wed_sub():
    if datetime.today().weekday() == 2: # Wednesday
         if hour_now == "09": # 8am
            print("test1")

def first_thur_sub():
    if datetime.today().weekday() == 3: # Thursday
         if hour_now == "08": # 8am
            print("test1")

def first_fri_sub():
    if datetime.today().weekday() == 4: # Friday
         if hour_now == "08": # 8am
            print("test1")

first_mon_sub()
first_tue_sub()
first_wed_sub()
first_thur_sub()
first_fri_sub()
