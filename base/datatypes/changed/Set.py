'''
tip:
set()
means create an empty set
cannot use {}
{} be used to create an empty dictionary 
'''

student = {'tom','peter','jerry','joy','tom'}
print(student) #repetitive elemets will be removed
A = set('abcdefadf')
B = set('fhau')

print(A)  #'a' 'b' 'c' 'd' 'e' 'f'
print(B)  #'f' 'h' 'a' 'u'
print(A - B)  # 集合A中包含而集合B中不包含的元素
print(A | B)  # 集合A或B中包含的所有元素
print(A & B)  # 集合A和B中都包含了的元素
print(A ^ B)  # 不同时包含于A和B的元素

myset = set({"taobao","facebook"})
myset.add("wechat")
print(myset)

myset.update([1,3])
print(myset)
myset.update([1,4],[7,9])
print(myset)

myset.remove("taobao")
print(myset)
'''
myset.remove("twitter")
print(myset)  #keyerror 不存在会发生错误
'''
myset.discard("twitter")
print(myset)

myset.pop()
print(myset)

s = {"a","b","c"}
s.clear() #clear the set
print(s)
