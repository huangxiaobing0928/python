# use "break" to stop "for"
alist = ["taobao","twitter","facebook","wechat"]
for site in alist:
    if site == "facebook":
        print("facebook")
        break
    print("for "+site)
else:
    print("nofor")
print("for end")


# range()
for i in range(5):
    print(i)

for i in range(5,9):
    print(i)

for i in range(5,9,2):
    print(i)

mylist = ["taobao","twitter","facebook","wechat","instgram"]
for i in range(len(mylist)):
    print(i,mylist[i])


newlist = list(range(5))
print(newlist)

# continue 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print(var)
print("the end")

# pass 是空语句，是为了保持程序结构的完整性;pass 不做任何事情，一般用做占位语句
























































































































































































































































































































































































































































































































































































































































































































































































