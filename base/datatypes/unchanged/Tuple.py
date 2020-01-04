'''
tip1
the differences between tuple and list
one:the element of tuple cannot be changed , like string
two:list use [] , but tuple use () also cannot use ()
'''
#example:
mytuple = "1","2","3"
print(type(mytuple))

'''
tip2
string can be regarded as a special tuple
'''

'''
tip3:special rule
'''
#create an empty tuple ;
tuple1 = ()
print(tuple1)

#creat a new tuple: tuple_a = tuple_b + tuple_c ;

#When you  create a tuple including one element , you need add "," after the element ;
tuple2 = (12,)
tuple3 = (12)
print(tuple2)
print(tuple3)

#delate tuple : del tuple_X ;

'''
tip4
string , list and tuple all belong to sequence , can transfer each other
'''
string = "famliy"
list = [1,2,3]
print(tuple(string))
print(tuple(list))

len((1, 2, 3)) #count
(1, 2, 3) + (4, 5, 6) #connect
('Hi!',) * 4   #copy
3 in (1, 2, 3)  #exist or not
for x in (1, 2, 3):
    print (x,)


tuple_l = ("love","response","home")
print(tuple_l[2])
print(tuple_l[-2])
print(tuple_l[:])




