from capitals import states
import random
correct = 0
incorrect = 0

print("Hello! Would you like to play a game? Type yes to begin playing guess that state capital")
answer = str(input())
if answer == "yes":
    random.shuffle(states)
    for x in states:
        print(f"What is the capital of {x['name']}?")
        answer2 = str(input())
        if answer2 == x['capital']:
                correct = correct +1
                print(f"Correct! Your current score is {correct} correct answers and {incorrect} incorrect answers")
        else:
            incorrect = incorrect +1
            print(f"Sorry, that wasn't right. The answer was {x['capital']}. Your current score is {correct} correct answers and {incorrect} incorrect answers")
else: 
    print("Maybe next time")
