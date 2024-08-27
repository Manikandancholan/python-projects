import random

total_rounds = int(input("How many rounds would you like to play? "))

p1Score = cpuScore = current_round = 0

while current_round < total_rounds:
    p1 = input("Enter rock/paper/scissors: ")
    choices = ['rock', 'paper', 'scissors']
    print(f"p1 Choice: {p1.lower()}")
    if p1.lower() in choices:
        cpu = random.choice(choices)
        print(f"CPU Choice: {cpu}")

        if p1.lower() == cpu.lower():
            print('Tie!')
        elif p1 == 'rock' and cpu == 'scissors':
            p1Score += 1
        elif p1 == 'paper' and cpu == 'rock':
            p1Score += 1
        elif p1 =='scissors' and cpu == 'paper':
            p1Score += 1
        else:
            cpuScore += 1
    else:
        print("Invalid input!")
        
    print(f"Your Score: {p1Score}")
    print(f"CPU Score: {cpuScore}")

    current_round += 1

    # Display the current round and scores
    print(f"Round {current_round}/{total_rounds}")
    print(f"Your Score: {p1Score}, Computer's Score: {cpuScore}")
    print("-" * 20)

if p1Score > cpuScore:
    print("Congratulations! You are the overall winner!")
elif p1Score < cpuScore:
    print("The computer wins overall. Better luck next time!")
else:
    print("It's a tie overall!")
