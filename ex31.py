print("""You enter a dark room with two doors.
        Do you go through door #1 or #2?""")

door = input("> ")

if door == "1":
    print("There a giant bear here eating cheese cake")
    print("WHat do you want to do?")
    print("1 Scream")
    print("2 Take the cake?")

    bear = input("> ")
    if bear == "1":
        print("The bear eats you")
    elif bear == "2":
        print("The bear eats your legs")
    else:
        print(f"Well, doing {bear} is probably better")
