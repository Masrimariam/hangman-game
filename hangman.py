from faker import Faker
from AsciiHangman import HANGMANPICS

fake = Faker()
pc_word = fake.word()
print(f"I'm the secret word: {pc_word}")
correct_word = ["_"]* len(pc_word)
print(' '.join(correct_word))
print(fr"{HANGMANPICS[0]}")
already_guessed = []
nb_tries = 6
ascii_index = 0
while "_" in correct_word and nb_tries > 0:
    match = False
    user_guess = input("\nEnter a character to guess the word: ").lower()
    for i, ch in enumerate(pc_word):
        if user_guess == pc_word[i]:
            correct_word[i] = ch
            match = True
    print(' '.join(correct_word))   
    if not match:
        if user_guess not in already_guessed:
            nb_tries -= 1
            already_guessed.append(user_guess)
            print(f"you have {nb_tries} more tries")
            ascii_index += 1
            if ascii_index in range(len(HANGMANPICS)):
               print(fr"{HANGMANPICS[ascii_index]}")
            
        else :
            print(f"you have already entered {user_guess}, you have {nb_tries} more tries ")
    else:
        print(f"you have {nb_tries} more tries")
if nb_tries == 0:
    print("you lose!")
else:
    print("you win! ᕙ(⇀‸↼‶)ᕗ")

