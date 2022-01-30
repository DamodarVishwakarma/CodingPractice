n = int(input("Enter any number"))
a = 0
b = 1
c = 1
count=1
while count <= n:
    count+=1
    print(a, end=" ")
    a = b
    b = c
    c = a + b

