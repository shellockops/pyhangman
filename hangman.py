import random

def update_word(character, word, word_to_guess):
	for i in range(len(word)):
		if word[i] == character:
			word_to_guess[i] = character

def clear_screen():
	print("\033[2J\033[H")

def take_random_word():
  words = []
  with open('wordlist.txt', 'r') as wordlist:
    for word in wordlist:
      words.append(word.strip())
  return random.choice(words)

def print_typed_chars(char_already_typed):
  print("Characters already typed: ", end="")
  for char in char_already_typed:
    print(f"{char} ", end="")
  print()

def final_screen(art, attempt, result):
  print(art[attempt])
  if result:
    print("Congratulations, you guessed the word.")
  else:
    print("You lose. It will be better the next time, byee.")

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
