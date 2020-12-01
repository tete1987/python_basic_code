#1."+" 号的使用：
# a = "ddddd0"
# b = "bbbbb"
# print(a+b)

#2.空格的使用
# print("hhhh" "dddd")

# 3.引用语法
#用法1
# a = "aaaaaa"
# b = f"ddddd{a}"
# print(b)

#用法2
# a = "aaaaa"
# b = "bbbbb{}"
# print(b.format(a))

#3)多个引用
# a="aaaaa"
# b="bbbbb"
# c="ccccc"
# d=f"ddddd{}{}{}"
# print(d.format(a,b,c))

#4)多个引用中加入变量
a="aaaaa"
b="bbbbb"
c="ccccc"
d="ddddd{x}{y}{z}"
print(d.format(x=a,y=b,z=c))