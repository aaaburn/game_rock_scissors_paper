import random
from colorama import Fore

# Default params
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
# Formatting params
i = ["\033[3m", "\033[0m"] # italic formatting
b = ["\033[1m", "\033[22m"] # strong formatting
u = ["\033[4m", "\033[24m"] # underline formatting



# Player move
player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move.lower() == "r" or player_move == '1':
    player_move = rock
elif player_move.lower() == "p" or player_move == '2':
    player_move = paper
elif player_move.lower() == "s" or player_move == '3':
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again...")


# Computer move - version 1)
computer_random_number = random.randint(1, 3)
computer_move = ""
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

# # Computer move - version 2)
# possible_moves = ["rock", "paper", "scissors"]
# computer_move = random.choice(possible_moves)




print(Fore.BLUE + f"{i[0]}The computer chose {computer_move}.{i[1]}")

if (player_move == rock and computer_move == scissors) or \
    (player_move == paper and computer_move == rock) or \
    (player_move == scissors and computer_move == paper):
    print(Fore.GREEN + f"{b[0]}{i[0]}You {u[0]}win{u[1]}{i[1]}!{b[1]}")
elif player_move == computer_move:
    print(Fore.YELLOW + f"{b[0]}{i[0]}Draw!{i[1]}{b[1]}")
else:
    print(Fore.MAGENTA + f"{b[0]}{i[0]}You lose!{i[1]}{b[1]}")




