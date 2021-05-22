import random
counter = [0, 0, 0, 0, 0, 0, 0]

for i in range(100):
    value = random.randint(1, 6)
    counter[value] = counter[value] + 1
    
for i in range(6):
    print(counter[i + 1])
