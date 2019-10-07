from capitals import states
import random
correct = 0
incorrect = 0

def game_play():
    correct = 0
    incorrect = 0
    random.shuffle(states)
    for x in states:
        print(f"What is the capital of {x['name']}?")
        answer2 = str(input())
        if answer2 == x['capital']:
            correct = correct + 1
            incorrect = incorrect
            print(
                f"Correct! Your current score is {correct} correct answers and {incorrect} incorrect answers")
        else:
            correct = correct
            incorrect = incorrect + 1
            print(
                f"Sorry, that wasn't right. The answer was {x['capital']}. Your current score is {correct} correct answers and {incorrect} incorrect answers")
        if incorrect + correct == 50:
            print("Game over, try again?")
            answer3 = str(input())
            if answer3 == "yes":
                game_play()
                print("Let's do it!")
            else:
                print("Thanks for playing!")
game_play()