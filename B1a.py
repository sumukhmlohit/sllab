lis=[]
n=int(input('Enter no of elements'))
for i in range (1,n+1):
    x=int(input('Enter no'))
    lis.append(x)
duples=[]

def newli(lis,duples):
    for num in lis:
        if num not in duples:
            duples.append(num)
    print(duples)

newli(lis,duples)
evelis=[i for i in duples if i%2==0]
print(evelis)

duples.reverse()
print(duples)




    
