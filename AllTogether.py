import random
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Original list:", random_numbers)

for i in range(len(random_numbers) - 1, -1, -1):
    if random_numbers[i] % 2 == 0:
        random_numbers.pop(i)

print("Remaining odd numbers:", random_numbers)
