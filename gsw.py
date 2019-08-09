import random

# A list of words that

word_bank = ["daisy", "rose", "lily", "sunflower", "lilac"]

word = random.choice(word_bank)

correct = word
# Use to test your code:
#print(word){key: value for key, value in variable}

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = []
for w in range(len(word)):
	current_word.append("_")
print(current_word)
 # TIP: the number of letters should match the word

# Some useful variables
guess = []
maxfails = 3
fails = 0
count = 0
letter_guess = ''
word_guess = ''
store_letter = ''

#you should make a loop where it checks the amount of letters inputted

while fails < maxfails:
	guess = input("Guess a letter: ")

#while count < fails:

if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

if letter_guess not in word:
        print('no!')
        count += 1

print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
print('These letters are: ', store_letter)

#you don't need this because o fyour previous while loop. The one above
	#will only run until the user runs out of guesses
while fails > maxfails:
	word_guess = input('Guess the whole word: ')
while word_guess:
    if word_guess.lower() == correct:
        print('Congrats!')
        break

    elif word_guess.lower() != correct:
        print('Unlucky! The answer was,', word)
        break




	#check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

print(current_word)

	#fails = fails+1
	#print("You have " + str(maxfails - fails) + " tries left!")
