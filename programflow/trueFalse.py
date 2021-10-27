if 0:
    print("true")
else:
    print("false")

name = input("Please enter your name: ")

# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are the person without name")