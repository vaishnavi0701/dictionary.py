
# Q6.
# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dic={0: 10, 1: 20}
dic1={ 2:30 }


dic2={}
for k in (dic,dic1):
    dic2.update(k)
print(dic2)
