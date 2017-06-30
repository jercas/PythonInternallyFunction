# coding="utf-8"
# By JerCas
# 2017-6-30
# Python中几种字符串格式化输出方式比较

# c中的%占位符形式的格式化字符串
print("%s\n%s\n%s"%(10,2.3,['one','two']))

# 测试string.format()的各种用法和对输出形式的优化
# 通过位置
print('\n{},{}'.format('jer', 18))
print('{0},{1}'.format('jer', 18))
print('{1},{0}'.format('jer', 18))
print('{1},{0},{1}'.format('jer', 18))

# 通过关键字参数
print('\n{name},{age}'.format(age=18,name='jer'))

# 通过对象属性
class Person:
  def __init__(self,name,age):
    self.name,self.age = name,age
  def str(self):
      return 'This guy is {self.name},is {self.age} old'.format(self=self)
a=Person('jer',18)
print('\n%s'%a.str())
print('\n{}'.format(a.str()))

# 通过数组/列表下标
b=['jer',18]
c=('jer',18)
print('\n{0[0]},{0[1]}'.format(b))
print('\n{0[0]},{0[1]}'.format(c))

# 填充与对齐
print('{:>8}'.format('189'))
print('{:0>4}'.format('189'))
print('{:x>10}'.format('189'))

# 精度与类型
print('{:.2f}'.format(123.456789))
print('{:.4f}'.format(123.456789))

# 进制
print('{:b}'.format(2))
print('{:o}'.format(8))
print('{:d}'.format(10))
print('{:x}'.format(16))

# 千分位分隔符
print('{:,}'.format(1234567890))

