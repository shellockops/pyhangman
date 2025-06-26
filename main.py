from hangman import *

def main():
	word = list("redhat")
	word_to_guess = list("_"*len(word))
	attempts = 0

	print("Welcome in hangman game.\n\n\n")
	while word_to_guess != word and attempts < 5:
		print(f"The word to guess is: {"".join(word_to_guess)}")
		character = input("Enter a character: ")
		if character in word:
			update_word(character, word, word_to_guess)
		else:
			attempts += 1
			print("Try again")
		clear_screen()

main()	
