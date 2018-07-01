#Q1. find and handle the excepetion:
'''
a=3
 if a<4:
    a=a/(a-3)
     print(a)
#Error is ZeroDivisionError(divison by zero)
'''
error is ZeroDivisionError(divison by zero)
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as e:
    print("error is",e)

#Q2. find the error and handle it.
#Error occured is IndexError(list index out of range)
'''
l=[1,2,3]
print(l[3])
#Error occured is IndexError(list index out of range)
'''
l=[1,2,3]
try:
    print(l[3])
except IndexError as e:
    print("error is",e)

#Q3.What will be the output of the following program:
# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
'''
An exception
Traceback (most recent call last):
  File "C:/Users/Sakshi/Desktop/python/op.py", line 2, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there
'''


#Q4.find the output of the following program:
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
'''
Output:
-5.0
a/b result in 0 
'''

#Q5.Write a prorgam to show and handle the 
#1.Import Error
try:
    from threading import XY
    print("hi")
except ImportError as e:
    print("error is",e)

#2.Value Error
try:
  n=int(input("enter a valid number"))
  print(n)

except ValueError as e:
    print("value is wrong",e)

#3.Index Error
l=[1,2,3]
try:
    print(l[3])
except IndexError as e:
    print("error is",e)

#Q6. User defined exception to check the validity of age
class Error(Exception):
  
  def ageTooSmall(self, warning):
     print(warning)

x=True
while x:
  try:
     age=int(input("Enter a valid age"))
     if age<18:
         raise Error()

  except Error as e:
     e.ageTooSmall("Age is invalid")
   
  else:
     x=False
