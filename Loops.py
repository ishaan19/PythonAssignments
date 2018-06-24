#1
num = int(input("enter the number"))
while num>0:
    print("%d"%(num))
    num=num-1



#2
num = int(input("enter the number"))
while num>0:
    print("%d"%(num))



#3
element_list = [2,3,4,5,6]
print("list of elements")
for x in element_list :
    print(x)
print("list of square of elements of previous list")
for x in element_list :
    print(x**2)



#4
lisst = [2,5,5.6,3.2,'ronaldo','neymar']
intlist=[]
floatlist=[]
strlist=[]
for x in lisst :
    if type(x) == int :
        intlist.append(x)
    elif type(x) == float :
        floatlist.append(x)
    else :
        strlist.append(x)
print(intlist)
print(floatlist)
print(strlist)



#5
x = range(1,101)
odd_num=[]
even_num=[]
for x in range(1,101):
    if x%2==0 :
        even_num.append(x)
    else :
        odd_num.append(x)
print("list of odd numbers : ",(odd_num))
print("list of even numbers : ",even_num)



#6
star = 1
while (star<=4):
    print("*"*star)
    star=star+1



#7
di ={'one':1,'two':2,'three':3,'four':4}
for x in di.keys():
    print(x,di[x])



#8
l1=[]
ele = int(input("enter the size of list : "))
for x in range(ele):
    y = int(input("enter value : "))
    l1.append(y)
d = int(input("enter the element to be deleted : "))
for x in l1:
    if x == d:
        l1.remove(x)
    else :
        print("element is not in the list")
print("the list is : ",l1)


