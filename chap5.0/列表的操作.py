#列表名=[e1,e2,....]

#列表名=list[]

# lst1=['hello','world','China']
# lst2=list('hello world') #使用list（）不能在函数里面写多个，最多一个‘’ ，当超过一个时会报错。
# print(lst1)
# print(lst2)
# print(lst1+lst2)
#
# print(lst1*10)
# print(len(lst1))
# print(max(lst1))
# print(min(lst1))
# print(lst2.count('o'))

#列表的遍历 for循环遍历
# lst=['hello','world','c++']
# for item in lst:  # 验证此处，无论是item还是i都可以
#     print(item)
#

#for+range()+len() 遍历
# for i in range(len(lst)):
#     print(i,'--->',lst[i]) #这里i不能加上引号，加上引号变成了str，而不是int，改变了数据类型，所以会报错


#使用enumerate()函数
#
# for index,item in enumerate(lst,start=1):
#     print(index,item)  index是序号，而非引索注意，可以改变开始的序号
#这里的item与index仍然可以用别的来代替，并不是属于enumerate的关键字

##列表的特有操作：
#有如下写列表的方法：

# lst=[1,2,3,4,5,6,7,8,9]
# print("原列表：",lst)
#
# lst.sort()#在原列表的基础上排序，不会产生新的列表
# print(lst)#默认是升序
#
# lst.sort(reverse=True)
# print("降序排列L:",lst)
#
# print("-"*20)
#
# lst2=["apple","banana","cherry","Cat","Dog"]
# print(lst2)
#
# lst2.sort()
# print("升序：",lst2) #先排大写然后再小写
#
# print("-"*20)
# lst2.sort(reverse=True)
# print("降序：",lst2)
#
# lst2.sort(key=str.lower)#忽略大小写来进行升序排序
# print(lst2)


# lst=[1,2,3,-4,5,6,7,8,9,10,11,-1,-13,-14,1-5]
# print("原列表:",lst)
#
# lst_new1=sorted(lst)
# print("排序之后的列表：",lst_new1)
#
# lst_new2=sorted(lst,reverse=False)
# print("降序之后的别表：",lst_new2)
#revers=True 表示降序，因为默认是升序，反过来就是降序



