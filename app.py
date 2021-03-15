from math import *
import useful_tools

# character_name = "Hugo"
# character_age = 35
# is_male = True
#
# print("There once was a man named "+character_name+", ")
# print("he was " + str(character_age) + " years old. ")
#
# character_name = "Doogie"
#
# print("He really liked the name "+character_name+", ")
# print("but he didn't like being "+f'{character_age}'+".")
# print("")
#
# phrase = "Giraffe Academy"
# print("Strings are \"Fun\"")
# print("")
# print(phrase + "is NOT cool, hahaha.")
# print("is" + phrase.lower() + " " + phrase.upper() + " cool?")
# print(phrase.isupper())
# print("")
# print("is" + phrase.lower() + " " + phrase.upper() + " cool?")
# print(phrase.upper().isupper())
# print("")
# phrase_length = len(phrase)
# print("The phrase is " + str(phrase_length) + " characters long")
# print("")
# print(phrase.replace("Giraffe", "Fat Cats"))
# print("")
# my_num = -2
# print("The absolute value of my_num is: " + str(abs(my_num)))
# print()
# print(pow(4, 6))
# print()
# print(max(484, 829))
# print(max(484, 829))
# print(sqrt(36))
# math. floor, round, max, min, sqrt, ceil,

# name = input("Enter your name: ")
# num1 = input("Enter the year you were born: ")
# num2 = input("Enter the current year: ")
# result = float(num2) - float(num1)
# print("Hello " + name + "!")
# print("You are " + str(result.__round__()) + " years old.")

# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)
# lucky_numbers = [4, 89, 1, 2123, 412]
# friends = ["joe", "tom", "steve", "Food", "glomb", "sven"]

# print(friends[1:5])
# lucky_numbers.sort()
# print(lucky_numbers)
# friends[4] = "tobias"
# friends.insert(1, "Francois")
# print(friends)
# friends.remove("Food")
# print(friends)
# friends.append("Clory")
# print(friends)
# friends.extend(lucky_numbers)
# print(friends)
# friends.index("steve")
# print(len(friends))

# tuples are immutable
# coordinates = (4, 5)
# print(coordinates[1])

# Say hello function
# def say_hi(name, age):
#     print("Hi " + name + ", you are " +age)
#
#
# say_hi("Chobie", "35")
# say_hi("Cornine", "34")


# def cube(num):
#     return num*num*num
#
#
# result = input("Enter a number: ")
# print(cube(int(result)))


# If statements
# is_male = False
# is_tall = True
#
# if is_male and is_tall:
#     print("You can fight in the pit")
# elif is_male and not is_tall:
#     print("You are a short man")
# elif not is_male and not is_tall:
#     print("You are a short female")
# else:
#     print("You can fight in the clouds")


# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num(4, 5, 5))

# The Most Amazing calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
#
# print(monthConversions["Mar"])
# print(monthConversions.get(input("Enter a month: "), "Not a valid key"))

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with loop")


# Guessing game
# secret_word = "albino"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses, You Lose!")
# else:
#     print("You Win!")

# Guessing Game Simplified
# secret_word = "albino"
# guess = ""
# guess_count = 0
#
# while guess != secret_word and guess_count < 3:
#     guess = input("Enter guess: ")
#     guess_count += 1
#
# if guess == secret_word:
#     print("You Win")
# else:
#     print("You Lose")

# friends = ["joe", "tom", "steve", "Food", "glomb", "sven"]
# # print(len(friends))
# for friend in friends:
#     print(friend)
#
# for index in range(3, 10):
#     print(index)
#
# for letter in "Academy":
#     print(letter)
#
# for index in range(5):
#     if index == 0:
#         print("first Iteration")
#     else:
#         print(index)

# def raise_to_power(base_number, pow_number):
#     result = 1
#     for index in range(pow_number):
#         result = result * base_number
#     return result
#
#
# print(raise_to_power(3, 4))
#
#
# def raise_to_power2(base_number, pow_number):
#     return base_number**pow_number
#
#
# print(raise_to_power2(3, 4))

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# for row in number_grid:
#     # print(row)
#     for col in row:
#         col
#
# Translator app
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
#
# print(translate(input("Enter a phrase: ")))

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Invalid Input")
# except ZeroDivisionError as err:
#     print(err)


# employee_file = open("index.html", "w")
# employee_file.write("<h1>This is HTML</h1><div><p>No Joking around here</p><p>HTMLLLLLL!</p></div>")

# for employee in employee_file.readlines():
# print(employee)
# print(employee_file.readable())
# print("")
# print(employee_file.readline())
# print(employee_file.readline())
# print("")
# print(employee_file.readlines()[1])

# employee_file.close()


# print(useful_tools.roll_dice(10))

from student import Student
student1 = Student("Joe", "Science", 3.8, False)
student2 = Student("Sally", "Art", 2.8, True)


# print("Student " + student2.name + " " + student2.on_honor_roll())



# from Question import Question
#
# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
#
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]


# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.question_prompt)
#         if answer == question.answer:
#             print("Correct\n")
#             score += 1
#         else:
#             print("Incorrect\n")
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct")
#
#
# run_test(questions)


from Chef import Chef

myChef = Chef()
myChef.make_salad()

from ChineseChef import ChineseChef
myChineseChef = ChineseChef()

myChineseChef.make_special_dish()
