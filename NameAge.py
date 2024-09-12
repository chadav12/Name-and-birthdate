from datetime import date

# input name and age
name = input("What is your name? ")
Age = int(input("How old are you? "))
# uses the current year as of today
current_year = date.today().year

# Calculates the difference between the age and current year
birth_year = current_year - Age
# Prints output

print(f"Hello {name}! You were born in {birth_year}.")