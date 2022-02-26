#Question 5:
#We have the names of six countries given below. Write a Python function to print all the countries that start with the letter 'A.'
test_list = 'Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran'

# initializing check letter
check = 'A'

country_A = [idx for idx in test_list if idx[0].lower() == check.lower()]

print(country_A)