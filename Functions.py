#1
rad = int(input("enter the radius of circle : "))
def area(rad) :
     ar = 3.14*rad*rad
     print("area of circle : ",ar)
     
area(rad)



#2
def Perfect(n):
    summ=1
    i=2
    while(i*i<=n):
        if n%i==0:
            summ = summ + i + n/i
        i+=1
        return(True if summ == n and n!=1 else False)
print("below are all perfect numbers")
n=2
for n in range(1000):
    if Perfect(n):
        print(n)


#3
def mul(n,i=1):
    print(n*i)
    if(i==10):
        return 1
    else :
        mul(n,i+1)
n=12
mul(n)



#4
def pow(a,b):
    if(b==0):
        return 1
    else:
        return(a**b)
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
print("answer : ",pow(a,b))



#5
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
d={}
n=int(input("enter the number : "))
a=fact(n)
print("factorial : ",a)
d={n:a}
print("dictionary is : ",d)
