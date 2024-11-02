import random


def function_A(min, max):
    """
    Generates a random integer between a specified minimum and mximum range.

    Args:
        min (int): Lower bound of the range
        max (int): Upper bound of the range
    
    Returns:
        int: A random integer between min and max.
    """
    return random.randint(min, max)


def function_B():
    """    
    Chooses a random arithmetic operator.

    Returns:
        str: A randomly selected arithmetic operator from '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    """
    Args:
        n1 (int): number 1 
        n2 (int): number 2
        o (str): operator

    Returns:
        p (str): The entire operation as a string e.g.,- '1 + 2' 
        a (int): Result of the operation
    """
    p = f"{n1} {o} {n2}"
    # addition
    if o == '+': a = n1 + n2
    # subtraction
    elif o == '-': a = n1 - n2
    # multiplication
    else: a = n1 * n2
    
    return p, a

def math_quiz():
    """
    A program for a math quiz where the user to answer mathematical questions. Each correct answer earns the
    user one point and the total points are shown at the end of the game.

    """
    score = 0
    num_ques = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_ques):
        n1 = function_A(1, 10); 
        n2 = function_A(1, 5); 
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")

        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid input! Please enter integers only!")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{num_ques}")

if __name__ == "__main__":
    math_quiz()
