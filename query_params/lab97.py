#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html

URL= "https://opentdb.com/api.php?amount=10"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    questions = data["results"]
    random.shuffle(questions)

    while True:
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



if __name__ == "__main__":
    main()
