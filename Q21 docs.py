# Q11.Write a Python script to merge two Python dictionaries

dic={"name":"vaishu","age":20,"class":12}
dic1={"food":"maggi","mob":"mi"}

dic2={}
for k in (dic,dic1):
    dic2.update(k)
print(dic2)


