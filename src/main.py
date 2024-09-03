import random


def main() -> None:
    """Main code"""
    name = input("Name: ")
    question = input("Question:")

    # Get answer
    random_number = random.randint(1, 10)

    # Print result
    if question == "":
        print("No question!")
    else:
        if name == "":
            print(f"Question: {question}")
        else:
            print(f"{name} asks: {question}")

        if random_number not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            print("Magic 8-Ball's answer: Error")
        else:
            answers = {
                1: "Yes - definitely",
                2: "It is decidedly so",
                3: "Without a doubt",
                4: "Reply hazy, try again",
                5: "Ask again later",
                6: "Better not tell you now",
                7: "My sources say no",
                8: "Outlook not so good",
                9: " Very doubtful",
                10: "Obviously",
            }
            print(f"Magic 8-Ball's answer: {answers.get(random_number)}")
