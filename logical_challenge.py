import random


def display_sticks(n):
    print("Remaining sticks: " + "|" * n)


def player_removal(n):
    while True:
        try:
            removal = int(input("How many sticks would you like to remove (1, 2, 3)? "))
            if removal in [1,2,3] and removal <= n:
                return removal
            else:
                print(f"Please enter a valid number of sticks(1,2,or 3) that does not exceed {n}.")
        except ValueError:
            print("Invalid input. Please enter a valid number of sticks(1,2,or 3)")


def master_removal(n):
    if n % 4 == 0:
        return random.randint(1,3)
    else:
        return n % 4


def nim_game():
    n = 20
    player_turn = True

    while n>0:
        display_sticks(n)

        if player_turn:
            print("Player's turn.")
            removal = player_removal(n)
        else:
            print("The game master is taking its turn.")
            removal = master_removal(n)
            print(f"The game master removes {removal} sticks")

        n -= removal
        player_turn = not player_turn
    if not player_turn:
        print("The player removed the last stick. You lost!")
        return False
    else:
        print("The game master removed the last stick. You won")
        return True
