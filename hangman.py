import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel", "elephant", "flamingo", "zebra", "crocodile"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(len(chosen_word)):
    display += "_"

lives = 6
finish = False
while finish == False:
    
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")
    
#     to check guess letter apakah ada di setiap letter di chosen word atau engga
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}. That's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            finish = True
            print("You Lose.")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        finish = True
        print("You've won!")
        
    print(stages[lives])