answer = 5
num1 = int(input("guess the number: "))
if num1 > 5:
    print("guess lower number")
elif num1 < 5:
    print("guess higher number")
else:
    print("you got the correct answer")
