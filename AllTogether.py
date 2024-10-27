import random
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Original list:", random_numbers)

for number in random_numbers[:]: 
    while number % 2 == 0 and number in random_numbers:
        random_numbers.remove(number)

print("Remaining odd numbers:", random_numbers)
