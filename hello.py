message = "Hello World!"
employed = False
print(message)

# name = input("What is your name? ")
# print("Hello " + name)

# birthYear = input("What year were you born? ")
# birthYear = int(birthYear)

# age = 2024 - birthYear
# print(name + " is " + str(age) + " years old")

# A = input("First number? ")
# B = input("Second number? ")
# C = float(A) + float(B)
# print("Sum: " + str(C))
A = 3 > 2
print("A: " + str(A))

price = 25

print(price > 10 and price < 30)
# ^^ above will return true only if expressions on both sides of "and" are true
salePrice = 15
print(salePrice > 10 or salePrice < 3)
# ^^ above will return true if either expression is true


# temperature = 25
# if temperature > 30:
#     # This indented code will only run if the condition above is met
#     print("It's hot outside! ")
# elif temperature > 20:
#     # elif is short for else if
#     print("It's a nice day")
# elif temperature > 10:
#     print("it's a bit cold") 
# else:
#     print("It's friggen cold out there! ")
# print("done")
# # ^ this always runs


# weight = float(input("What is your weight? "))
# unit = input("(K)g or (L)bs?").upper()
# if unit == "K":
#     result = str(weight * 2.2)
#     print("Your weight in lbs is: ")
#     print(result)
# elif unit == "L":
#     result = str(weight * .45)
#     print("Your weight in kgs is: ")
#     print(result)
# else:
#     print("Something went wrong")


i = 1
while i < 10:
    print (i * "*")
    i = i + 1