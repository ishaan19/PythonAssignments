#1
tuple1 = ('ishaan','bharti','aryan')
print(tuple1)
print(len(tuple1))



#2
tuple1=('ishaan','55','coder')
tuple2=('geek','1','python')
print(max(tuple1))
print(min(tuple1))
print(max(tuple2))
print(min(tuple2))



#3
tuple1=(1,2,3,4,5)
product=1
for x in tuple1:
    product *= x
print(product)



#4
#difference
set1= set([9,8,7,6])
set2= set([9,4,8,2])
set3=set1&set2
print(set3)
set4=set1-set3
print(set4)
set5=set2-set3
print(set5)


#intersection
setx=set3&set5
print(setx)

#compare
sety=set1 | set2
print(sety)

#compare
setz=set1<=set2
print(setz)





#5
dict = {}
for x in range(3):
    name=input('name')
    marks=int(input('marks'))
    dict[name]= marks

print(dict)



#6 sir said to leave



#7
dict ={}
str="MISSISSIPI"
m = str.count('M')
i = str.count('I')
s = str.count('S')
p = str.count('P')
dict['M'] = m
dict['I'] = i
dict['S'] = s
dict['P'] = p
print(dict)
