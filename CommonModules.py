#1
It may be an integer. or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).
The other representation is a tuple of 9 integers giving local time.
Index	Field	                Values
0	4-digit year	        2008
1	Month	                1 to 12
2	Day	                1 to 31
3	Hour	                0 to 23
4	Minute	                0 to 59
5	Second	                0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	        0 to 6 (0 is Monday)
7	Day of year	        1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1, -1 means library determines DST



#2
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d"))



#3
import datetime
x=datetime.datetime.now()
print(x.month)



#4
import datetime
x=datetime.datetime.now()
print(x.day)



#5
import datetime
d=datetime.datetime(2021,1,11)
print(d.year,d.month,d.day)



#6
import time
print(time.localtime())



#7
import math
x=int(input("enter the number : "))
print(math.factorial(x))



#8
import math
x = int(input("enter the first number : "))
y = int(input("enter the first number : "))
print(math.gcd(x,y))



#9
import os
print(os.getcwd())
print(os.environ)




