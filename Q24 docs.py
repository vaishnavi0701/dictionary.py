# Q14.Write a Python program to multiply all the items in a dictionary.


a=input("enter any word:")
i=0
c={}
for i in a:
    if i not in c:
        c[i]=1
    else:
        c[i]=c[i]+1
print(c)
multiply=1
for i in c:
    multiply=multiply*c[i]
print(multiply)






# d={ 'value1': 5,
#     'value2': 4,
#     'value3': 3,
#     'value4': 2,
#     'value5': 1,}
  
# answer = 1
# for i in d:
#     answer = answer*d[i]
# print(answer)