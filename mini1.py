import requests
import random
import sys

response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital")

if response.status_code == 200:
    result = response.json()
    random.shuffle(result)
else:
    print("Failed to retrieve data")
    sys.exit()

correct = 0
incorrect = 0
print("Welcome to the game, type 'q' at any time to quit")

while True:
    print("\nCorrect: " + str(correct) + " - Incorrect: " + str(incorrect) + "\n")

    country = result.pop()
    name = country['name']['common']
    capital = country['capital'][0] if country['capital'] else 'No capital'

    guess = input("What is the capital of " + name + " \n (type 'h' for a hint or 'q' to quit): \n")
    if (guess.lower() == "h"):
        print(capital[0] + '_' * (len(capital) - 2) + capital[len(capital) - 1])
        guess = input("What is the capital of " + name + ": \n")

    if guess.lower() == "q":
        break
    elif guess.lower() == capital.lower():
        print("\nCorrect!")
        correct += 1
    else:
        print("\nIncorrect! The capital of " + name + " is - " + capital)
        incorrect += 1


print("\nThank you for playing!")

    

        