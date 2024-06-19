import random

from hangmanwordlist import word_list
chosen_word=random.choice(word_list)
wordlen=len(chosen_word)
display=[]
for _ in range(wordlen):
    display+="_"

end_of_game=False
lives=6

from hangmanart import logo
print(logo)

while not end_of_game:
    guess=input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(wordlen):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess

    if guess not in chosen_word:
        print(f"You guessed {guess}.It's not the letter in the word.Hence, you lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("Alas! You lose.")
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("Hurrah! You win.")

    from hangmanart import stages
    print(stages[lives])







