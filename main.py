# Import the random module for generating random values
import random

# Lists of possible characters to include in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '/', '=', '?']
# Print a welcome message
print("Welcome to the Python console password generator!")

# Get user input for the number of letters, numbers, and symbols in the password
num_letters = int(input("How many letters would like in your password?\n"))
num_numbers = int(input("How many numbers do you want in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

# Create an empty list to store characters of the password
password_list = []

# Generate letters for the password
for char in range(1, num_letters + 1):
    password_list += random.choice(letters)

# Generate numbers for the password
for char in range(1, num_numbers + 1):
    password_list += random.choice(str(numbers))

# Generate symbols for the password
for char in range(1, num_symbols + 1):
    password_list += random.choice(symbols)

# Shuffle the order of characters in the password list
random.shuffle(password_list)

# Convert the password list to a string
password = ""
for char in password_list:
    password += char

# Display the generated password
print(f"Your password is: {password}")
