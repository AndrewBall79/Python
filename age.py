from datetime import date
# request birth year
from getpass import getpass

birth_year = int(input('what year were you born? '))
# create the date object
today_date = date.today()
# retrieve the year from the object
cur_year = today_date.year
# do the math for the year
age = cur_year - birth_year
# Print the users age
print(f"You are {age} years old")


user_name = input("What is your username? ")
password = getpass("What is your password? ")
password_length = len(password) * '*'
hidden_password = len(password)

print(f"{user_name}, your password {password_length}, is {hidden_password} characters long")

