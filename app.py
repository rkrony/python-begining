
print("Hello world!")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# different uses of string
phrase = "Giraffe academy"
print(phrase)
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(phrase.lower())
print(len(phrase))
print(phrase.index("G"))
print(phrase[6])
print(phrase.replace("Giraffe","Camel"))

# different uses of number
my_num = 5
print(my_num)
print(str(my_num) + " is my favourite number")
my_num = -5
print(abs(my_num))
print(pow(3 , 2))
print(max(6 , 4))
print(round(3.49))

# importing math library for more function
from math import *
print(sqrt(36))
print(floor(3.7))
print(ceil(3.2))

#getting input from user

name = input("Enter your name : ")
age = input("Enter your age : ")
print("Hello "+ name +"! and you are "+ age)

#creating a little calculator
num1 = input("Enter a number : ")
num2 = input("Enter another number : ")
result = float(num1) + float(num2)
print(result)

#Mad libs game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " +color)
print(plural_noun+" are blue")
print("I love " +celebrity)

#Lists
friends =["rabbi","himel","neymar","messi"]
print(friends)
friends[0] ="rasel"
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

#list function
friends =["rabbi","himel","neymar","messi"]
lucky_number =[7, 3, 7, 13]
friends.extend(lucky_number)
print(friends)
friends.append("ronaldinho")
print(friends)
friends.insert(2, "afridi")
print(friends)
friends.remove(3)
friends.pop()
print(friends)
# friends.clear()
print(friends.index("afridi"))
lucky_number =[5, 9, 2, 6, 15]
lucky_number.sort()
print(lucky_number)
lucky_number.reverse()
print(lucky_number)
print(friends.count(7))
print(len(friends))
friends2 = friends.copy()
print(friends2)


# tuples(a container where we can put different values and we can't modify its value after assigning value)
coordinates = (4, 6)
print(coordinates[0])
location = [(4, 6), (15, 20), (8, 6)]  # tuples inside list which we can't change
print(location[2])


# function
def say_hi(name, age):
    print("hello " + name + " you are " + str(age))
print("top")
say_hi("rony", 24)
print("bottom")



# return statement in python
def returnfunc(number):
    result = number * number * number
    return result


print(returnfunc(3))


def cube(num):
    return num * num


result = cube(4)
print(result)

# if statement
is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are tall but u are not a male")
else:
    print("you are neither a male nor a tall")

#if statement and comparisons