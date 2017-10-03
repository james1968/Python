the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of foor-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as the above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to a list.")
    elements.append(i)

for i in elements:
    print(f"Element was {i}")

