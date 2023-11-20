import random

# Capital and lowercase letters used in password generator
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Numbers used in password generator
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Symbols used in password generator
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Asks the user for how many letters they want in their password
num_letters = int(input("How many letters would you like in your password?\n"))

# Asks the user how many symbols they want in their password
num_symbols = int(input("How many letters would you like in your password?\n"))

# Asks the user how many numbers they want in their password
num_numbers = int(input("How many numbers would you like?\n"))

# Password list
p_list = []

for char in range(1, num_letters + 1):
    p_list.append(random.choice(letters))

for char in range(1, num_symbols + 1):
    p_list.append(random.choice(numbers))

for char in range(1, num_numbers + 1):
    p_list.append(random.choice(symbols))

    # Randomly shuffles password list
    random.shuffle(p_list)

    password = ""
