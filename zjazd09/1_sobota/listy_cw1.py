from functools import reduce

a = [2, 543, 3, 43, 2]

# suma
print(sum(a))

# mnożenie
result = 1
for x in a:
    # x == 2, 543, 3, 43, 2
    result *= x
print(result)


# rozwiązanie typu nerd
print(reduce(lambda x, y: x*y, a))
