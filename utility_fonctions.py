def introduction():
    print("Somewhere in the heart of the ocean, standing tall against the tides, lies the legendary Fort Boyard. ")
    print("For centuries, this fortress has guarded its secrets and treasures, waiting for those brave enough to face its trials.")
    print("Today, a new team of adventurers will enter the fort. Their mission: to unlock the mysteries of the fort, ")
    print("confront its challenges,collect the keys and claim the treasure of the enigmatic Père Fouras.")
    print("But beware! The path to victory is fraught with danger, puzzles, and hard tasks. Will you succeed, ")
    print("or will the fort keep its treasure locked away for another day?")
    print("Welcome to... FORT BOYARD!")
    print("Good luck!:)")


def compose_team():
    team = []
    while True:
        try:
            num_players = int(input("How many players do you want to include in your team (1-3)? "))
            if num_players < 1 or num_players > 3:
                print("Error: The number of players must be between 1 and 3.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")

    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        profession = input(f"Enter the profession of player {i + 1}: ")
        is_leader = input(f"Is {name} the team leader? (yes/no): ").strip().lower() == 'yes'
        player = {
            'name': name,
            'profession': profession,
            'is_leader': is_leader,
            'keys_won': 0
        }
        team.append(player)

    if not any(player['is_leader'] for player in team):
        team[0]['is_leader'] = True

    return team


def challenges_menu():
    print("Choose a challenge type:")
    print("1. Mathematics challenge")
    print("2. Logic challenge")
    print("3. Chance challenge")
    print("4. Père Fouras' riddle")

    while True:
        try:
            choice = int(input("Enter the number corresponding to the challenge: "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Error: Please enter a valid number (1-4).")
        except ValueError:
            print("Error: Please enter a valid number.")


def choose_player(team):
    print("Select a player to take on the challenge:")
    for index, player in enumerate(team):
        role = "Leader" if player['is_leader'] else "Member"
        print(f"{index + 1}. {player['name']} ({player['profession']}) - {role}")

    while True:
        try:
            player_number = int(input("Enter the player's number: ")) - 1
            if 0 <= player_number < len(team):
                return team[player_number]
            else:
                print("Error: Please enter a valid player number.")
        except ValueError:
            print("Error: Please enter a valid number.")