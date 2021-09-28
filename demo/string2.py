parrot = "Norwegian Blue"

print(parrot[0:6]) #Norweg
print(parrot[-14:-8])

#Bl
print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2])
print(parrot[0:6:3])

numbers = "9,223;372:036 854,775;807"
seperators = numbers[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in numbers).split()
print([int(val) for val in values])