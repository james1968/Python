def remove(s):
    if s == "!Hi":
        print("Hi!")
    elif s == "Hi":
        print("Hi!")
    else:
        count=s.count("!")-1
        s = s.replace('!','',count)
        print(s)


remove("Hi!")
remove("Hi!!!")
remove("Hi!!!")
remove("!Hi")
remove("!Hi!")
remove("Hi! Hi!")
remove("Hi")
