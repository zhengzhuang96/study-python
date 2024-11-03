print(1)

num1 = 3

print(num1)

num2 = 2

num3 = 3

total = num1 + num2 + num3

print(total)

# 变量只有在被赋值之后才能被创建

# 首次使用变量会在内存中划分空间，并初始化值

# 再次使用变量不在划分空间，修改原空间的值

a = 666

b = a

b = 111

# 同一个变量可反复赋值，运行顺序从上往下

print(b)

# python关键字
import keyword
print('python关键字：', keyword.kwlist)
print('python关键字数量：', len(keyword.kwlist))

print(type('b'))

# complex复数型(了解)
# 固定写法：z = a + bj a：是实部 b：是虚部 j：是虚数单位

ma = 2 + 3j
mb = 3 + 5j
print(ma + mb)

# 字符串类型

str1 = '测试名称'
str2 = "测试2"
str3 = """测试333
print(111)
"""

print(str1)
print(str2)
print(str3)

# 占位符(%s, %d, %f )
# 占位符只是占据位置，并不会被输出

# %s 字符串占位符(常用)
name1 = "郑壮"
print("我的名字是：%s" % name1)

# %d 整数
age1 = 18
print("我的名字是：%s, 年龄是：%d" % (name1, age1))

# %3d 整数
print("测试整数：%d" % age1)
print("测试整数：%3d" % age1)
print("测试整数：%011d" % age1) # 表示输出的整数显示位数，不足的话用0补全，超出当前位数则原样输出

# %f 浮点数
a1 = 1.23456789
print("测试浮点数：%f" % a1) # 默认后6位小数，遵循四舍五入原则

# %.3f 浮点数
print("测试浮点数: %.3f" % a1)
print("测试浮点数: %.15f" % a1)

# %% 占位符
print("我是%%的1%%" % ())

# f格式化
print(f"我的名字是{name1}, 我的年龄是{age1}")










