list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list.sort()
list = [number for number in list if number != 1]
list.extend([7, 8])

print(list)
