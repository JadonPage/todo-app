def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age


birth = int(input("What is your year of birth? "))
age = get_age(birth)
print(age)
