import psutil
import time
import datetime

for proc in psutil.process_iter():
    a = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S")
    print(a)



a = [1,2,3,4,5,6]
b= [5,6,7,8,9,10]
for x in a:
    for y in b:
        if x == y:
            print(x,"=",y)



time.sleep(100)