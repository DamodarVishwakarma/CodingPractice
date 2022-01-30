l = [3, 5, 6, 7, 8, 85, 4, 443, 33, 2]
n = len(l)
for i in range(n):
    min_value = min(l[i:])
    min_index = l.index(min_value)
    l[i], l[min_index] = l[min_index], l[i]
print(l)
