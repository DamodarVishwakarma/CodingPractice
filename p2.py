def max(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        return n1
    elif (n2 > n3) and (n2 > n1):
        return n2
    else:
        return n3


print("maximum of three number is :")

M = max(15, 4, 34)
print(M)
