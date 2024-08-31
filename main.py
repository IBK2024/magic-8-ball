import random

name = input("Name: ")
question = input("Question:")

# Get answer
random_number = random.randint(1, 10)

# Print result
if question == "":
    print("No question!")
else:
    if name == "":
        print("Question:", question)
    else:
        print(name, "asks:", question)
    if random_number == 1:
        print("Magic 8-Ball's answer: Yes - definitely")
    elif random_number == 2:
        print("Magic 8-Ball's answer: It is decidedly so")
    elif random_number == 3:
        print("Magic 8-Ball's answer: Without a doubt")
    elif random_number == 4:
        print("Magic 8-Ball's answer: Reply hazy, try again")
    elif random_number == 5:
        print("Magic 8-Ball's answer: Ask again later")
    elif random_number == 6:
        print("Magic 8-Ball's answer: Better not tell you now")
    elif random_number == 7:
        print("Magic 8-Ball's answer: My sources say no")
    elif random_number == 8:
        print("Magic 8-Ball's answer: Outlook not so good")
    elif random_number == 9:
        print("Magic 8-Ball's answer: Very doubtful")
    elif random_number == 10:
        print("Magic 8-Ball's answer: Obviously")
    else:
        print("Magic 8-Ball's answer: Error")
