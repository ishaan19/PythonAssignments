#1
import re
li=["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
l2=[]
for i in li:
    l=re.split('[@./s]',i)
    l2.append(tuple(l))
print(l2)



#2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
lst=re.findall('[bB]\w*',text)
print(lst)



#3
import re
sentence =  "A, very very; irregular_sentence"
l=re.sub('[\W_]',' ',sentence)
for i in l :
    print(i,end="")
