dic={'ball':'red',

    'bat':4,

    'wickets':8,

    'ball': 'green' ,

    'bat':3}

#  {“ball”:”red”,”bat”:4,”wickets”:8}

i=0
for i,j in dic.items():
    j=i
    if i==j:
        print(dic)
        break