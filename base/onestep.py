a,b = 0,1
while b<10:
    print(b)
    a,b = b,a+b

#keyword : end
# can make the results to print in same line

a,b = 0,1
while b<10000:
    print(b,end=',')
    a,b = b, a+b
