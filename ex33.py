i = 0
numbers = []
limit  = 6

#while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)

def while_loop(i):
    if i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        while_loop(i)

while_loop(i)

print("The numbers: ")

for num in numbers:
    print(num)
