import rtc
import time

r = rtc.RTC()
r.datetime = time.struct_time((2024, 5, 29, 15, 14, 15, 0, -1, -1))

print(time.time())