#1
players=['ronaldo','neymar','messi','ronaldinho','del pierro','marco asensio']
print(players)



#2
players=['ronaldo','neymar','messi','ronaldinho','del pierro','marco asensio']
company=['apple','google','microsoft','facebook','tesla']
print(players+company)



#3
players=['ronaldo','neymar','messi','ronaldinho','del pierro','marco asensio','ronaldo']
print(players)
print(players.count('ronaldo'))



#4
number_list=[2,9,8,5,4,1,8,0,5,4,3,6,7]
print(number_list)
print(number_list.sort())
print(number_list)



#5
a=[0,1,2,3,4,5]
b=[6,7,8,9,10]
c=[a+b]
print (c)



#6

#stack
l1=[]
l1.append(2)
print(l1)
l1.append(3)
print(l1)
l1.append(5)
print(l1)
l1.pop(-1)
print(l1)
l1.pop(-1)
print(l1)
l1.pop(-1)
print(l1)

#queue

l2=['ronaldo','neymar','ronaldinho','zidane','marco','messi']
print(l2)
print(l2.pop(0))
print(l2)
print(l2.pop(0))
print(l2)



#7Optional
l1=[1,2,3,4,5,6,7,8,9,10]
countodd=0
counteven=0
for x in l1:
    if x%2==0:
        counteven+=1
    else:
        countodd+=1
print("even : ",counteven)
print("odd : ",countodd)
