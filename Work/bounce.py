# bounce.py
#
# Exercise 1.5

height = 100
bounce_efficiency = 3/5

for bounce in range(1, 11):
    height = height * bounce_efficiency
    print(bounce, round(height, 4))
