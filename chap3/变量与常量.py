luck_number=8
my_name='Mario'
print(my_name +"的幸运数字是:",luck_number)

#定义常量的时候 与C语言一样，只不过多了=
PI = 3.141592653589793  #这里PI就是常量

print('luck_number的数据类型是：',type(luck_number))
print('my_name的数据类型是：',type(my_name))

#在python允许多个变量指向同一个值。

no=number=100
print(id(no)) #id()用于查看对象的内存地址
print(id(number))

x=10
y=3
x/=y
print(x,type(x))