from collections import Counter

file=open("freq.txt","r")
print(Counter(file.read().split()))
