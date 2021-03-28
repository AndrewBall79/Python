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


user = {
    'name': "Golem",
    'age': 5006,
    'can_swim': False,
}

for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)



is_magician = False
is_expert = True

if is_magician:
    if is_expert:
        print("You are a master")
    else:
        print("You're getting there")
else:
    print("You need magic powers")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for item in my_list:
    count = count + item
print(count)


# Create a list with range
for _ in range(3):
    print(list(range(10, 0, -1)))


for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')

