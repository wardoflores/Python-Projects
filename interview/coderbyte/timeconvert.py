# Time convert from Meridian to Military
# Source: https://stackoverflow.com/questions/39184198/converting-time-from-am-pm-format-to-military-time-in-python

time = input("put Meridian time here: ")
print("\n")

hour = int(time[:2])
meridian = time[8:]
# Special-case '12AM' -> 0, '12PM' -> 12 (not 24)
if (hour == 12):
    hour = 0
if (meridian == 'PM'):
    hour += 12
print("%02d" % hour + time[2:8])
