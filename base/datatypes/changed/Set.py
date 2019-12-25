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
print(A - B)
print(A | B)
print(A & B)
print(A ^ B)

