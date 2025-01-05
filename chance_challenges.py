import random

def shell_game() -> bool:
    shells = ['A', 'B', 'C']
    max_attempts = 2
    attempts = 0

    key_shell = random.choice(shells)

    print("Welcome to Shell Game!")
    print("You have 2 attempts to find the key.")

    while attempts < max_attempts:
        print(f"\nRemaining attempts: {max_attempts - attempts}")
        player_choice = input("Which shell would you like to choose? (A, B, C): ").upper()

        if player_choice in shells:
            if player_choice == key_shell:
                print(f"Congratulations! You found the key under the shell {player_choice}.")
                return True
            else:
                print(f"Sorry, the key is not under the shell: {player_choice}.")
        else:
            print("Invalid choice. Please choose A, B, or C.")

        attempts += 1

    print(f"You lost! The key was under the shell {key_shell}.")
    return False


def roll_dice_game() -> bool:
    max_attempts = 3

    print("Welcome to Roll Dice Game!")
    print("You have 3 attempts to roll a 6. If you do it before the game master, you win.")

    for attempt in range(max_attempts):
        print(f"\nRemaining attempts: {max_attempts - attempt}")
        input("Press 'ENTER' to roll the dice...")

        player_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"You rolled: {player_dice}")

        if 6 in player_dice:
            print("Congratulations! You rolled a 6 and won the game!")
            return True

        game_master_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"The game master rolled: {game_master_dice}")

        if 6 in game_master_dice:
            print("The game master rolled a 6 and won the game!")
            return False

        print("No one rolled a 6. Moving on to the next attempt.")

    print("After 3 attempts, no one rolled a 6. It's a draw!")
    return False


def chance_challenges():
    print("Welcome to Chance Challenges!")
    challenges = [
            shell_game,
            roll_dice_game,
        ]

    challenge = random.choice(challenges)
    return challenge()

