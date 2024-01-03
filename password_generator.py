#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Randomised order of characters :
chosen_letters = ''
for letter in range(nr_letters):
    randomized_letter = random.choice(letters)
    chosen_letters += randomized_letter

chosen_symbols = ''
for symbol in range(nr_symbols):
    randomized_symbol = random.choice(symbols)
    chosen_symbols += randomized_symbol
    
chosen_numbers = ''
for number in range(nr_numbers):
    randomized_number = random.choice(numbers)
    chosen_numbers += randomized_number
    
my_password = chosen_letters + chosen_symbols + chosen_numbers
print(''.join(random.sample(my_password,len(my_password))))