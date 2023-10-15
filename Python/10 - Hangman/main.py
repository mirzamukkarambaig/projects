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

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_"] * word_length

chances = 6

while "_" in display:
    if chances == 0:
        print(stages[0])  # Print the last stage which represents the fully hanged man
        print("You Lose!")
        break

    guess = input("Guess a letter: ").lower()

    correct_guess = False
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess
            correct_guess = True
    
    if not correct_guess:
        print(stages[chances])
        chances -= 1

    print(f"{' '.join(display)}")

if "_" not in display:
    print("You Win!")

