num = int(input("Enter any number\n"))
rev = 0
temp=num
while num > 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10
print(rev)
if (temp == rev):
    print("Number is palindrom")
else:
    print("Number is not palindrom")
