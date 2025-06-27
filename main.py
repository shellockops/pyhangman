from hangman import *

def main():
	word = list(take_random_word())
	word_to_guess = list("_"*len(word))
	attempts = 0
	char_already_typed = []

	print("Welcome in hangman game.")
	while word_to_guess != word and attempts < 6:
		print(f"{ART[attempts]}\n")
		print(f"The word to guess is: {"".join(word_to_guess)}")
		if attempts:
			print(f"Attempts: {attempts}")
		if char_already_typed:
			print_typed_chars(char_already_typed)
		character = input("Enter a character: ")
		if not character.isalpha():
			clear_screen()
			continue
		if character in word:
			update_word(character, word, word_to_guess)
		else:
			char_already_typed.append(character)
			attempts += 1
			print("Try again")
		clear_screen()

	result = True
	if '_' in word_to_guess:
		result = False

	final_screen(ART, attempts, result)

main()	
