'''{key:value}
the elements in dictionary be added or received by the key 
'''

dict = {'name':'yuantong','gender':'female'}
print(dict['name'])
print(dict.keys())
print(dict.values())

'''
add or delate key / value
'''
dict['name'] = "xiaobing"
dict['age'] = 26
del dict['gender']
print(dict)  # print(str(dict))

'''
the key must be unchanged
can use string or number or tuple , but cannot use list
'''





