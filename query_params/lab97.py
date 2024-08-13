#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html

URL= "https://opentdb.com/api.php"

def main():
    categories= {
    9:  "General Knowledge", 
    10: "Entertainment- Books", 
    11: "Entertainment- Film", 
    12: "Entertainment- Music", 
    13: "Entertainment- Musicals & Theater", 
    14: "Entertainment- Television", 
    15: "Entertainment- Video Games", 
    16: "Entertainment- Board Games", 
    17: "Science- Nature", 
    18: "Science- Computers", 
    19: "Science- Mathematics", 
    20: "Mythology", 
    21: "Sports", 
    22: "Geography", 
    23: "History", 
    24: "Politics", 
    25: "Art", 
    26: "Celebrities", 
    27: "Animals", 
    28: "Vehicles", 
    29: "Entertainment- Comics", 
    30: "Science- Gadgets", 
    31: "Entertainment- - Japanese Anime & Manga", 
    32: "Entertainment- - Cartoon Animations"
    }

    quantity = input("Enter the number of questions: ")
    difficulty = input("Enter the difficulty (easy, medium, hard): ")

    for category in categories:
        print(f"{category}: {categories[category]}")
    print('\n')
    category = input("Enter the category ID (e.g, 9 for General Knowledge): ")

    params = {
        "amount": quantity,
        "category": category,
        "difficulty": difficulty
    }

    data = requests.get(URL, params).json()

    # data will be a python dictionary rendered from your API link's JSON!
    questions = data["results"]
    random.shuffle(questions)

    while questions:
        question = questions.pop()
        question_text = html.unescape(question["question"])

        formatted_incorrect = [html.unescape(item) for item in question["incorrect_answers"]]
        answers = [html.unescape(question["correct_answer"])] + formatted_incorrect
        random.shuffle(answers)

        print(question_text)

        for i in range(len(answers)):
            print(f"{i + 1}: {answers[i]}")

        guess_index = int(input("Choose your answer - ")) - 1

        if answers[guess_index] in answers:
            if answers[guess_index] == question["correct_answer"]:
                print("Correct!\n")
            else:
                print("Incorrect! The correct answers was - " + question["correct_answer"] + "\n")
        else:
            print("Invalid input\n")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
