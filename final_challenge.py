import json
import random

def load_clues(file: str) -> dict:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return {}
    except json.decoder.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{file}'.")
        return {}

def treasure_room():
    file_path = "data/TRClues.json"

    tv_game = load_clues(file_path)

    if not tv_game:
        return

    try:
        years = list(tv_game['Fort Boyard'].keys())
        year = random.choice(years)

        shows = tv_game['Fort Boyard'][year]
        show = random.choice(list(shows.values()))

        clues = show['Clues']
        code_word = show['CODE-WORD']
    except KeyError as e:
        print(f"Error: Missing key - {e}")
        return

    print("Welcome to the treasure room challenge!")
    print("Here are the first three clues:")
    for clue in clues[:3]:
        print(f"- {clue}")

    attempts = 3
    answer_correct = False

    while attempts > 0:
        player_answer = input("Enter your guess for the code word: ").strip()

        if player_answer.lower() == code_word.lower():
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts remaining.")
                if 3 - attempts < len(clues):
                    print(f"Additional clue: {clues[attempts+3]}")
            else:
                print(f"Sorry, you've used all your attempts. The correct code word was: {code_word}")

    if answer_correct:
        print("Congratulations! You've guessed the correct code word and accessed the treasure!")
        print("The adventure comes to an end, but the memories of this day will live on. your bravery, your teamwork, ")
        print("and your spirit  have been tested against the trials of Fort Boyard.you came, you saw, and you conquered!")
        print("Against all odds, you have unlocked the secrets of the fort and faced its toughest trials. And now, ")
        print("you leave victorious, with the treasure of Fort Boyard in their hands!")
    else:
        print("Unfortunately, you failed to guess the code word. The adventure comes to an end, but the memories of this ")
        print("day will live on. your bravery, your teamwork, and your spirit  have been tested against the trials of ")
        print("Fort Boyard. But the fort remains, standing tall against the tides, waiting for the next team of ")
        print("adventurers to step forward and take on the challenge.")
