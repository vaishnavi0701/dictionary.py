
# Q13.Write a Python program to sum all the items in a dictionary.


dic ={  'a':50,'b':58,'c':56,'d':40,'e':100, 'f':20}
sum=0
for x in dic:
    sum=sum+dic[x]
print(sum)
