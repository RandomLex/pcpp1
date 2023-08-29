import random


class Apple:
    count = 0
    total_weight = 0

    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        Apple.total_weight += self.weight
        Apple.count += 1


while True:
    Apple()
    if Apple.count >= 1000 or Apple.total_weight >= 300:
        break

print(f'Apples: {Apple.count}')
print(f"Apples' weight: {Apple.total_weight:.2f}")
