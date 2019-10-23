from collections import Counter
import functools

di={}

file=open("fill.txt","r")

di=Counter(file.read().split(" "))
newdi=sorted(di.items(),key=lambda z:z[1],reverse=True)

for i in range(3):
    print(newdi[i])

print(newdi)
print(di)

li=list(di.values())
li.sort()
print(li)

li1=functools.reduce(lambda x,y :(x+y)/2,li)
print(li1)

li2=[i*i for i in li if i%2!=0]
print(sum(li2))

