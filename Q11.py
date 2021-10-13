dic=   {'a':50, 
        'b':58, 
        'c':56,
        'd':40, 
        'e':100, 
        'f':20 }

# [58,56,100]


a=[]
for i in dic.values():
    a.append(i)
print(a)
temp=0
for i in range(3):
    for k in range(len(a)-i-1):
        if a[k]>a[k+1]:
            temp=a[k]
            a[k]=a[k+1]
            a[k+1]=temp
    print(temp)
