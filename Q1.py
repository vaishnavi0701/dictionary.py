dic1={1:10, 2:20}

dic2={3:30,2:40}

dic3={5:50,6:60}

a={}
for i,j in dic1.items():
    for x,y in dic2.items():
        if i==x:
            a[i]=(j+y)
            print(a)

dic4={}
for k in (dic1,dic2,dic3,a):
    dic4.update(k)
print(dic4)











# dic2.update(dic3)
# dic1.update(dic2)
# print(dic1)


# i=0
# a={}
# b=[]
# while i<len(dic1):
#         a.update(dic1)
#         i=i+1
# # print(a)
# j=0
# while j<len(dic2):
#     a.update(dic2)
#     j=j+1
# # print(a)
# k=0
# while k<len(dic3):
#     a.update(dic3)
#     k=k+1
# print(a)

