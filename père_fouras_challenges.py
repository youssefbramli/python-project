import json
import random

def load_riddles(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            riddles = json.load(f)
        return riddles
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return []

def pere_fouras_riddles():

    file_path = r"/Users/youssefbramli/PycharmProjects/PythonProject/data/PFRiddles.json"
    riddles = load_riddles(file_path)

    if not riddles:
        print("No riddles available to play. Please check the data file.")
        return False

    selected_riddle = random.choice(riddles)
    question = selected_riddle.get('question', "No question provided.")
    correct_answer = selected_riddle.get('answer', "").strip().lower()
    attempts = 3

    print("Welcome to the Père Fouras Riddle Challenge!")
    print("You have 3 attempts to solve the riddle.")
    print(f"\nRiddle: {question}")

    while attempts > 0:
        player_answer = input("Your answer: ").strip().lower()
        if player_answer == correct_answer:
            print("Congratulations! You answered correctly and won a key!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect answer. You have {attempts} attempts remaining.")
            else:
                print(f"Sorry, you've used all your attempts. The correct answer was: {correct_answer}.")
                return False






