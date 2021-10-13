# Q16.Write a Python program to map two lists into a dictionary.

keys =['one','two','three','four','five']

values=[1,2,3,4,5,] 

dict= {} 
for x in keys: 
    for y in values: 
        dict[x] = y
        values.remove(y) 
        break  

print ("dict : " +  str(dict)) 


