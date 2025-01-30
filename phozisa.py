import random

def run_quiz():
    # Quiz questions and answers
    questions = [
        {"question": "What is the capital of South Africa?", "options": ["1) East London", "2) Pretoria", "3) Cape Town"], "answer": 2},
        {"question": "When was Mr Nelson Mandela released outh of prison?", "options": ["1) 1994", "2) 1991", "3) 1990"], "answer": 3},
        {"question": "What is the largest ocean on Earth?", "options": ["1) Atlantic", "2) Indian", "3) Pacific"], "answer": 3},
        {"question": "When did Jan Van Riebeeck arrive at the Cape?", "options":["1) 1652", "2) 1918", "3) 1800"], "answer": 1},
        {"question": "Who composed the first part of the national anthem of South Africa?", "options": ["1) William Shakespeare", "2) Robert Sobukwe", "3) Enoch Sontonga"], "answer": 3}
    ]

    score = 0

    # Shuffle questions to make it fun
    random.shuffle(questions)

    print("Welcome to the Quiz Game!\n")

    for index, q in enumerate(questions):
        print(f"Question {index + 1}: {q['question']}")
        for option in q["options"]:
            print(option)

        while True:
            try:
                answer = int(input("\nEnter the number of your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the options.")


        # Get user input(you get the number a user guesses then return correct if the answer is corrector give the correct number should the user guesses wrong)
        answer = int(input("\nEnter the number of your answer: "))

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")

    print(f"Quiz complete! Your final score is {score}/{len(questions)}")
    
    # Restart option(you restart the game if you want to play again)
    restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if restart == 'yes':
        run_quiz()
    else:
        print("Thanks for playing!")

# Run the quiz game(this is where you run the game)
run_quiz()


