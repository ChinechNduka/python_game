import random
while True:

    print("\n-------------------------")
    print("Rock, Paper, Scissors - Shoot!")

    userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")

    if not userChoice in ['r','R','p','P','s','S']:
        print("Please choose a letter!")
        continue
    if userChoice != "exit":
        print("Your choice: " + userChoice)
        choices = ['R','P','S']
        opChoice = random.choice(choices)
        print("Oppenent choice: " + opChoice)

        if opChoice == str.upper(userChoice):
            print("Tie!")
        elif opChoice == 'R' and userChoice.upper() == 'S':
            print("Rock beats Scissor,I win!")
            continue
        elif opChoice == 'S' and userChoice.upper() == 'P':
            print("Scissor beats Paper,I win!")
            continue
        elif opChoice == 'P' and userChoice.upper() == 'R':
            print("Paper beats Rock, I win!")
            continue
        else:
            print("You win!")