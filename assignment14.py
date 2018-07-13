#q1. write a program to read last n lines

with open("abc.txt",'r') as f:
    data=f.readlines()
    for line in data:
        print(line)
    l = len(data)
    n= int(input("enter the value of n to print last n lines"))
    if (n<=l):
        print(data[n:])
    else:
        print("n is not in range")

#q2.count the frequency of words:
        
l=[]
with open('f1.txt','r') as f:
    data = f.readlines()
    word=[]
    for line in data:
        word+=line.split()

    d={}
    for k in word:
        if k in d:
            d[k]+=1
        else:
            d[k]=1
    print(d)

#q3.copy the contents from one file to another.
with open('xyz.txt','r') as d:
    with open('copy.txt', 'w') as d1:
        for line in d:
            d1.write(line)

#q4.Write a Python program to combine each line from first file with the corresponding

 line in second file.
'''
a.txt
hi how are you!!
hope you are doing good!!

b.txt
i m fine!!
what about you?
'''
with open('a.txt','r') as f1, open('b.txt','r')as f2, open('c.txt','w') as f3:
    a=f1.readlines()
    b=f2.readlines()
    for line1,line2 in zip(a,b):
        line4=line1+line2
        f3.write(line4)

f4=open('c.txt','r')
print(f4.read())
f4.close()

#q5.enter 10 random numbers in a file and sort them and store them in a new file.

with open('f4.txt','w') as f:
   for i in range(5):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('f4.txt','r') as f:
   data=f.readlines()
  
   for no in data:
      l=no.split()
   l.sort()

with open('f5.txt','w') as f:
   for i in l:         
      f.write("%s "%(i))


        

