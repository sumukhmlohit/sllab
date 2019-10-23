
class sentrev:

    def __init__(self,si):
        self.si=si
        self.sentreverse()
    
    def sentreverse(self):
        y=self.si.split(" ")
        print(y)

        li=[]

        for x in y:
            li.append(x)

        li.reverse()
        print(li)
        li1=[]
        for x in y:
            li1.append(x[::-1])

        print(li1)

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

        newdi1={(k,v) for(k,v) in sorted(di1.items())}
        print(newdi1)
        count.sort()
        print(count)
        print(di)
        newdi=sorted(di.items(),key=lambda z:z[1],reverse=True)
        print(newdi)

si=input('Enter a sentence')
o1=sentrev(si)
o1.sentreverse()
