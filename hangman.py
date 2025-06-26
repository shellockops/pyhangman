def update_word(character, word, word_to_guess):
	for i in range(len(word)):
		if word[i] == character:
			word_to_guess[i] = character
