
class sentrev:

    def __init__(self,si):
        self.si=si
       
    
    def sentreverse(self):
        y=self.si.split(" ")
        print(y)

        li=[]

        for x in y:
            li.append(x)
        
        li.reverse()
        print(li)

        str1=" "

        for i in li:
            str1+=i
        print(str1)
        
       

        vowel=['A','E','I','O','U','a','e','i','o','u']
        j=0
        count=[]
        di={}
        di1={}
        for z in li:
            
            k=0
            for i in z: 
                if i in vowel:
                    k=k+1
            di[z]=k
            di1[k]=z
            count.append(k)
        
        count.sort()
        print(count)
        print(di)
        newdi=sorted(di.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
        print(newdi)

        
        
        newdi2=sorted(di1.items(),key = lambda t:t[0],reverse=True)
        print(newdi2)
        
for i in range(3):
    si=input('Enter a sentence')
    o1=sentrev(si)
    o1.sentreverse()
