# This is a very simple code. We are going to hide our treasure.

# Write 3 variables that assign 3 lists. Each list stores 3 squares
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

# Merge theree lists so we can easily map the square
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

# Input the spot we want to put the treasure
position = input() 

# ABC for the column, 123 for the row (Type letter then number, eg: A1, C3, B2 etc)

# the letter should be the first character of the position (remember that the position consists a letter a the front, and a number at the latter), so letter should be at index 0 of the position
letter = position[0].lower()

# create a new list to get the index for the letter, later
abc = ["a", "b", "c"]

# get the index for the letter. we fetch it from the list abc. if the letter is "a", the program will find the index for item "a" inside the list. letter "a" is at the index 0. letter_index will be 0, 1, or 2 as the value depending on the letter
letter_index = abc.index(letter)

# get the index for the number. number is at the second place in the position, which is at the index 1. so we'll fetch it by position[1]. number should be subtracted by 1, so we get the actual index for the map, later.
number_index = int(position[1]) - 1

# replace the inputs into "X"
# from the map, we need to find the row first, then the column. number_index represents the row, letter_index represents the column. and here's the code:
map[number_index][letter_index] = "X"

# let's print out the initial map. this line of code below doen's have anything to do with the indexing code, and the map. this is just an initial code to show to the player.
print(f"{line1}\n{line2}\n{line3}")