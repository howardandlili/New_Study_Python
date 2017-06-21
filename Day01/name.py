#!/user/bin/env python
__author__ = 'Howie'

name = input('输入你的名字：')
age = input('输入你的年龄：')
job = input('输入你的工作：')
city = input('输入你住的城市：')

info = '''
---------------%s的信息-------------
年龄是：%s
工作是：%s
住的城市：%s
''' % (name, age, job, city)

print(info)
