import psutil
import time
import datetime
a = "Ford"
thisdict = {
  "brand": a,
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])



a = [1,2,3,4,5,6]
b= [5,6,7,8,9,10]
for x in a:
    for y in b:
        if x == y:
            print(x,"=",y)

            



time.sleep(100)