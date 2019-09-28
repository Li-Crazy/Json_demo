'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/27 20:51
@Software: PyCharm
@File    : main.py
'''
import json

# 将python对象转换为json字符串
persons = [
    {
        'username': "lixiaoxiao",
        'age': 18,
        'country': "china"
    },
    {
        "username": "王晓晓",
        "age": 18,
        "country": "china"
    }
]
json_str = json.dumps(persons)
print(type(json_str))
print(json_str)
with open('persons.json', 'w') as fp:
    fp.write(json_str)

# 将json数据直接dump到文件，只有基本类型才能被转换成JSON格式的字符串，int,float,str,list,tuple,dict
with open('persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f,
              ensure_ascii=False)  # ensure_ascii=False关闭ASCII编码，显示中文

# class Person(object):
#     country = "china"
#
# a = {
#     'person': Person()
# }
# json.dumps(a)

# 将json字符串load成python对象
json_str1 = '[{"username": "lixiaoxiao", "age": 18, "country": "china"},' \
            '{"username": "王晓晓", "age": 18, "country": "china"}]'
persons = json.loads(json_str1)#loads直接将json字符串load成python对象
print(type(persons))
for person in persons:
    print(person)

with open('persons.json','r',encoding='utf-8') as fp:
    persons = json.load(fp)#load将文件中的json字符串load成python对象
    print(type(persons))
    for person in persons:
        print(person)

