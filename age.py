from datetime import date
# request birth year
birth_year = int(input('what year were you born? '))
# create the date object
today_date = date.today()
# retrieve the year from the object
cur_year = today_date.year
# do the math for the year
age = cur_year - birth_year
# Print the users age
print(f"You are {age} years old")
