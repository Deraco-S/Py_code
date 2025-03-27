import random
lst0=[item for item in range(1,7)]
print(lst0)

lst1=[item**4 for item in range(6)]
print(lst1)

lst2=[random.randint(1,100) for _ in range(6)]
print(lst2)

#从列表中选择符合的元素构成新的列表
lst3=[random.randint(1,100) for _ in range(6) if random.randint(0,100)%2==0]
print(lst3)

#二维列表：先考虑行 ，然后再考虑行里面的每个元素
#for row in 二维列表：
#       for item in row:
#           paint()


#创建一个二维列表
lst=[
    ['城市',"环比","同比"],
    ['北京',300,303],
    ['上海',200,202],
    ['广州',100,101]
]
print(lst)

#遍历二维列表 使用双层for循环
for row in lst:
    for item in row:
        print(item,end='\t')
    print()#用来换行

