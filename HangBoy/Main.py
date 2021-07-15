import random
from HangmanArt import logo, stages
from HangmanWords import word_list

print(logo)
print("Developed with <3")
game_is_Finished = False
lives = len(stages) - 1

MysteryWord = random.choice(word_list)
wordLength  = len(MysteryWord)
# cheat Code
# print(f"The Answer is {MysteryWord}")

display = []
for x in range(wordLength):
    display += "_"

while not game_is_Finished:
    guess = input(" Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(wordLength):
        letter = MysteryWord[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in MysteryWord:
        print(f"You guessed {guess} which is not in given Word")
        lives -= 1
        if lives == 0:
            game_is_Finished = True
            print("You have lost. ")

    if not '_' in display:
        game_is_Finished = True
        print("Hurrah! You won \n No one got hanged today!!!")
    print(stages[lives])
