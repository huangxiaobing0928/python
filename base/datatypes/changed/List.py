list1 = ['abc',3.3,24,5+2j]
list2 = ['I','LOVE','YOU']

print(list1[0:5])
print(list1[1:])
print(list2[1])
print(list2 * 2)
print(list1 + list2)

list1[0:1] =['def','999']
list2[2] = 'YOU TOO'
list1[2:] = []

print(list1)
print(list2)

print(list2[0::2])

#delete some elements of the list
mylist = ["love","family","life","work"]
del mylist[3]
print(mylist)

print(len([1,2,3]))
print([1,2,3] + [4,5,6])
print(["hello","world"] * 4)
print(2 in [1,2,3])

for x in [1,2,3]:
    print(x,end="")




