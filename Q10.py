dict ={'Alex': ['subj1', 'subj2', 'subj3'], 

       'David': ['subj1', 'subj2']}

count=0
list=[]
for x in dict.values():
       list=list+x
print(list)
i=0
while i<len(list):
       count=count+1
       i=i+1
print(count)
       
