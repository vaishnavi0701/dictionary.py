dic=int(input("enter number"))
a={}
i=1
while i<=dic:
    a.update({i:i*i})
    i=i+1
print(a)



num=int(input("enter number:"))
dic={}
i=1
while i<=num:
    b=i*i
    dic[i]=b
    i=i+1
print(dic)

    




# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# list1=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
# # dic={}
# for key in list:
#     for value in list1:
#         dic[key]=value
#         list1.remove(value)
#         break
# print(dic)

