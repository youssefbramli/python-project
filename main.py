from maths_challenges import *
from logical_challenge import *
from chance_challenges import *
from père_fouras_challenges import *
from final_challenge import *
from utility_fonctions import *


def game():
    introduction()
    team = compose_team()

    keys_needed = 3
    total_keys = 0

    while total_keys < keys_needed:
        print(f"Total keys collected so far: {total_keys}")


        challenge_type = challenges_menu()
        if challenge_type not in [1, 2, 3, 4]:
            print("Invalid challenge type. Please select a valid challenge.")
            continue

        # Choose a player
        selected_player = choose_player(team)
        if not selected_player:
            print("No player selected. Please try again.")
            continue


        if 'keys_won' not in selected_player:
            selected_player['keys_won'] = 0


        challenge_result = False
        if challenge_type == 1:
            challenge_result = math_challenge()
        elif challenge_type == 2:
            challenge_result = nim_game()
        elif challenge_type == 3:
            challenge_result = chance_challenges()
        elif challenge_type == 4:
            challenge_result = pere_fouras_riddles()


        if challenge_result:
            selected_player['keys_won'] += 1
            total_keys += 1
            print(f"Great job, {selected_player['name']}! You’ve won a key.")
        else:
            print(f"Better luck next time, {selected_player['name']}!")

    print("🎉 Congratulations! You’ve collected all the keys! What an amazing team!")
    print("You can now access the final challenge in the treasure room!")
    treasure_room()

# Run the game
game()
