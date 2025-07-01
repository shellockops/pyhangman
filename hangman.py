import random

def update_word(character, word, word_to_guess):
  for i in range(len(word)):
    if word[i] == character:
      word_to_guess[i] = character

def clear_screen():
	print("\033[2J\033[H")

def take_random_word():
  words = []
  try:
    with open('wordlist.txt', 'r') as wordlist:
      for word in wordlist:
        if not word.strip().isalpha():
          print("ERRROR: Invalid wordlist\nYour wordlist contains invalid words or empty lines.")
          exit(1)
        words.append(word.strip())
  
  except FileNotFoundError:
    print("ERROR: File not found\nMake sure to have a file named: 'wordlist.txt' in this directory.")
    exit(1)

  return random.choice(words).lower()

def print_typed_chars(char_already_typed):
  print("Characters already typed: ", end="")
  for char in char_already_typed:
    print(f"{char} ", end="")
  print()

def final_screen(attempt, result):
  print(ART[attempt])
  if result:
    print("Congratulations, you guessed the word.")
  else:
    print("You lose. It will be better the next time, byee.")

MAX_ATTEMPTS = 6

ART = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
