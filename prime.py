num=int(input("enter any number\n"))
count=0
if num%2==0:
    print("given number is not prime")
    for i in range (1,num ):
        num%i==0
        count+=i
        print("factor of the given number is", count)
else:
  print("given number is prime")

str="hello"
newStr='_'.join(str)

n1=[]
for x in range(1500,2701):
    if (n1%5==0) and (n1%7==0):
        n1.append(str(x))
print(','.join(n1))

Replacing first and last elements of the string
str = "vishwakarma"
s=str[-1]+str[1:-1]+str[0]
print(s)

