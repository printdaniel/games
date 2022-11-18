import random
from aux import stages
from words import words

chosen_word = random.choice(words).lower()
display = []

word_length = len(chosen_word)
print(f"La palabra a adivinar contiene {word_length} letras")

for _ in range(word_length):
    display += "_"

print(display)

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Ingresa una letra: ").lower()

    if chosen_word == guess:
        print(f"Ganaste, la palabra es {chosen_word}")
        end_of_game = True

    if guess not in chosen_word:
        print(f"letra {guess} no está en la palabra ")
        lives -= 1
        print(stages[lives])

        if lives == 0:
            print(f"Perdiste, la palabra era {chosen_word}")
            end_of_game = True
            break

    for indice in range(word_length):
        if chosen_word[indice] == guess:
            display[indice] = guess
        
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print(f"Ganaste, la palabra es {chosen_word}")
