n=int(input('Enter no of elements'))
lis=[]
for i in range (1,n+1):
    x=int(input('Enter no'))
    lis.append(x)

def fimax(lis,n):
    if(n==1):
        return lis[0]
    return max(lis[n-1],fimax(lis,n-1))
print(fimax(lis,n))
