#1
year = int(input("enter the year : "))
if year==2016:
    print("%d is a leap year"%(year))



#2
length = int(input("enter the length"))
breadth = int(input("enter the breadth"))
if length==breadth:
    print("object is a square")
else :
    print("object is a rectangle")



#3
p1 = int(input("enter the age of p1 : "))
p2 = int(input("enter the age of p2 : "))
p3 = int(input("enter the age of p3 : "))
if p1>p2 and p1>p3 :
    print("p1 is oldest")
    if p2>p3:
        print("p3 is youngest")
    else :
        print("p2 is youngest")
elif p2>p1 and p2>p3 :
    print("p2 is oldest")
    if p1>p3:
        print("p3 is youngest")
    else :
        print("p1 is youngest")
else :
    print("p3 is oldest")
    if p1>p2 :
        print("p2 is youngest")
    else :
        print("p1 is youngest")



#4
pval = int(input("enter the value of points scored : "))
if (pval>=1 and pval<=50):
    print("Congratulations! you have won no prize")
elif pval>=51 and pval<=150 :
    print("congratulations ! you have won a wooden dog")
elif pval>=151 and pval<=180 :
    print("conrgatulations! you have won a book")
elif pval>=181 and pval<=200 :
    print("congratulations! you have won a chocolates")
else :
    print("sorry! no prize this time")



#5
quantity = int(input("enter the quantity purchased"))
cost = quantity*100
if cost>1000 :
    print("we get a 10% discount")
    discount=(cost*10)/100
    new_cost=cost-discount
    print("we need to pay %d"%(new_cost))
else :
    print("we need to pay %d"%(cost))
