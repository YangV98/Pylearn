string0 = ["a","b","c","d"]
string1 = ["a", "grab", "dodo", "bug", "ka"]
list0 = [1, 2, 3, 4, 5, 6]
list1 = [2, 4, 3, 1, 4, 5]
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#join对元组也成立
"""
print("string0", "=", string0)
test0 = ".".join(string0)
print("test0 = \".\".join(string0)", "=\n", test0)
_ = ".".join(["www","google","com"])
print("_ = \".\".join([\"www\",\"google\",\"com\"])", "=\n", _)
"""
#format
"""
_ = "{0}{1}{2}{3}".format("lable", "grain", "klab", "yolo")
print(_)
_ = "{0}{0}{0}{0}".format("lable", "grain", "klab", "yolo")
print(_)
_ = "{}{}{}{}".format("lable", "grain", "klab", "yolo")
print(_)
"""
#对齐及精度
"""
_ = "{:}".format(123)
print(_)
#左对齐和右对齐
_ = "{:1>10}{:0<10}".format(123, 456)
print(_)
#中间对齐
_ = "{:^20}".format(123)
print(_)
#仅符号可作为千分符
_ = "{:,}".format(123456789)
print(_)
#指定浮点数精度
_ = "{:.2f}".format(3.1415926)
print(_)
#指定总共数字精度
_ = "{:.2g}".format(3.1415926)
print(_)
#不可用于指定整数精度
_ = "{:.6}".format("abcdefghijklmn")
print(_)
#输出十六进制数
_ = "{:#x}".format(80)
print(_)
_ = "{:x}".format(80)
print(_)
"""

#f字符串的使用
"""
_ = ".".join(string0)
test0 = "this {} is".format(_)
print(test0)
test0 = f"this {_} is"
print(test0)

_ = "{:{a}{b}{c}.{d}{e}}".format(3.1415, a='+', b='>', c='10', d='4', e='g')
print(_)
_ = f"{3.1415:+>10.4g}"
print(_)
"""
#sort直接修改原字符串，sorted返回一个新字符串
"""
string0.sort(reverse=True)
print(string0)
_ = sorted("graghic")
print(_)
_ = sorted(string1, key=len)
print(_)
_ = sorted(string1, reverse=True)
print(_)
_ = sorted(string1[2])
print(_)
"""
#
"""
_ = [x for x in string1[1]]
print(_)
_ = list(string1[2])
print(_)
#zip函数选取矩阵同列元素，取最短
_ = list(zip(list2[0], list2[1], list2[2]))
print(_)
#map函数选取可迭代对象每个元素进行计算，返回运算结果的迭代器
_ = list(map(max, list2[0], list2[1], list2[2]))
print(_)
#filter函数返回运算结果为True的结果，以迭代器形式返回
_ = list(filter(str.islower, "FghyHjuYU"))
print(_)
"""
