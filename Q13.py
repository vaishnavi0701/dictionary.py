dic = {

    'a':50, 

    'b':58,

    'c': 56,

    'd':40,

    'e':100, 

    'f':20 }

# ['e','b','c']

a=[]
for i in dic.values():
    a.append(i)
# print(a)
temp=0
vallist=[]
for i in range(3):
    for k in range(len(a)-i-1):
        if a[k]>a[k+1]:
            temp=a[k]
            a[k]=a[k+1]
            a[k+1]=temp
    # print(temp)
    vallist.append(temp)
final=[]
for s in vallist:
    for k in dic.keys():
        if dic[k]==s:
            # print(k)
            final.append(k)
print(final)
