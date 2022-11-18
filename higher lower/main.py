import random
from os import system
from art import *
from game_data import *


def printer(p,s):
    print(f"{p['name']},  {p['description']} {p['country']}")
    print(vs)
    print(f"{s['name']}, {s['description']} {s['country']}")
    print(f"\n{s['name']} tiene más o menos followers que {p['name']}")



def play_game():
    in_game = True
    primero = random.choice(data)
    siguiente = random.choice(data)
    if primero == siguiente:
        siguiente = random.choice(data)
    score = 0

    while in_game: 
        printer(primero,siguiente)
        user_prespuesta = input("\nmas o menos: ").lower()
        if user_prespuesta == "mas":
            if siguiente['follower_count'] > primero['follower_count']:
                primero = siguiente
                system("clear")
            else:
                print(f'Tu puntaje {score}')
                in_game = False
        if user_prespuesta == "menos":
            if siguiente['follower_count'] < primero['follower_count']:
                primero = siguiente
                system("clear")
            else:
                print(f'Tu puntaje {score}')
                in_game = False

        if in_game:
            score += 1
            siguiente = random.choice(data)
            printer(primero,siguiente)


if __name__ == '__main__':
    print(logo)
    if input("Listo para jugar (y/n): ") == "y":
            play_game()

