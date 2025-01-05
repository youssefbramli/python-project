import random


def factorial(n):
    if n < 0:
        return "Factorial cannot be negative"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def math_challenge_factorial():
    n = random.randint(1,10)
    print(f"Calculate the factorial of {n} : ")
    correct_answer = factorial(n)
    while True:
        try:
            user_answer = int(input("Your answer is: "))
            break

        except ValueError:
            print("Invalid choice. Try again.")

    if user_answer == correct_answer:
        print("Correct! You win a key.")
    else:
        print("Incorrect. The correct answer is: ",factorial(n))






def solve_linear_equation():

    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    x = -b / a
    return a, b, round(x, 2)


def math_challenge_equation():

    a, b, correct_solution = solve_linear_equation()
    print(f"Math Challenge: Solve the equation {a}x + {b} = 0.")
    while True:
        try:
            user_answer = float(input("What is the value of x: "))
            break

        except ValueError:
            print("Invalid choice. Try again.")


    if user_answer == correct_solution:
        print("Correct! You win a key.")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_solution}.")
        return False




def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nearest_prime(n):

    while not is_prime(n):
        n += 1
    return n


def math_challenge_prime():

    n = random.randint(10, 20)
    correct_answer = nearest_prime(n)
    print(f"Math Challenge: Find the nearest prime to {n}.")
    while True:
        try:
            user_answer = float(input("What is the value of n: "))
            break

        except ValueError:
            print("Invalid choice. Try again.")
    if user_answer == correct_answer:
        print("Correct! You win a key.")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return False




def math_roulette_challenge():

    numbers = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        correct_answer = sum(numbers)
        operation_str = "addition"
    elif operation == '-':
        correct_answer = numbers[0]
        for num in numbers[1:]:
            correct_answer -= num
        operation_str = "subtraction"
    else:
        correct_answer = 1
        for num in numbers:
            correct_answer *= num
        operation_str = "multiplication"

    print(f"Numbers on the roulette: {numbers}")
    print(f"Calculate the result by combining these numbers with {operation_str}.")
    while True:
        try:
            user_answer = float(input("What is the value of n: "))
            break

        except ValueError:
            print("Invalid choice. Try again.")

    if user_answer == correct_answer:
        print("Correct answer! thanks to your brilliant brain,You've won a key. you can be proud of yourself!")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return False



def math_challenge() :

    challenges = [
        math_challenge_factorial,
        math_challenge_equation,
        math_challenge_prime,
        math_roulette_challenge
    ]

    challenge = random.choice(challenges)
    return challenge()
