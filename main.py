import hangman
import time

def main():
	word = list(hangman.take_random_word())
	word_to_guess = list("_"*len(word))
	attempts = 0
	char_already_typed = []

	print("Welcome in hangman game.")
	while word_to_guess != word and attempts < hangman.MAX_ATTEMPTS:
		print(f"{hangman.ART[attempts]}\n")
		print(f"The word to guess is: {"".join(word_to_guess)}")

		if attempts:
			print(f"Attempts: {attempts}")

		if char_already_typed:
			hangman.print_typed_chars(char_already_typed)

		character = input("Enter a character: ")

		if len(character) > 1:
			print("ERROR: multiple characters types")
			time.sleep(1)
			hangman.clear_screen()
			continue

		if not character.isalpha():
			print("ERROR: Invalid character")
			time.sleep(1)
			hangman.clear_screen()
			continue

		character = character.lower()

		if character not in char_already_typed:
			char_already_typed.append(character)
		else:
			print("ERROR: You've already typed this character")
			time.sleep(1)
			hangman.clear_screen()
			continue
		
		if character in word:
			hangman.update_word(character, word, word_to_guess)
		else:
			attempts += 1
			print("Try again")
		hangman.clear_screen()

	result = True
	if '_' in word_to_guess:
		result = False

	hangman.final_screen(attempts, result)

main()	
