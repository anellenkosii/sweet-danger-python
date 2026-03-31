import random
import os
import time

# Game settings
TOTAL_SWEETS = 20
POISON_COUNT = 3
LIVES = 3

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    title = """
██████╗  ██████╗ ██╗ ███████╗ ██████╗███████╗████████╗
██╔══██╗██╔═══██╗██║██╔════╝██╔════╝██╔════╝╚══██╔══╝
██████╔╝██║   ██║██║███████╗██║     █████╗     ██║   
██╔═══╝ ██║   ██║██║╚════██║██║     ██╔══╝     ██║   
██║     ╚██████╔╝██║███████║╚██████╗███████╗   ██║   
╚═╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝   ╚═╝   
    """
    print(title)
    print("🎮 Welcome to Sweet Danger! 🍬💀\n")

def choose_character(player_num):
    emojis = ["😎", "🤖", "🧙‍♂️", "👻", "🐱", "🐶"]
    print(f"Player {player_num}, choose your character:")
    for i, e in enumerate(emojis):
        print(f"{i+1}. {e}")
    while True:
        choice = input("Enter number of your character: ")
        if choice.isdigit() and 1 <= int(choice) <= len(emojis):
            return emojis[int(choice)-1]
        print("⚠️ Invalid choice.")

def pick_poison(player_num, sweets, player_is_computer=False):
    print(f"\n{player_num+1}'s turn to choose {POISON_COUNT} poisonous sweets secretly.")
    time.sleep(0.5)
    poison_indices = []
    if player_is_computer:
        poison_indices = random.sample(range(TOTAL_SWEETS), POISON_COUNT)
        print(f"🤖 Computer has selected its poisonous sweets.")
        time.sleep(1)
    else:
        while len(poison_indices) < POISON_COUNT:
            try:
                choice = int(input(f"Choose sweet #{len(poison_indices)+1} to poison (1-{TOTAL_SWEETS}): ")) - 1
                if choice < 0 or choice >= TOTAL_SWEETS or choice in poison_indices:
                    print("⚠️ Invalid or already chosen sweet.")
                    continue
                poison_indices.append(choice)
            except ValueError:
                print("⚠️ Enter a valid number.")
    return poison_indices

def initialize_game(player2_is_computer):
    sweets = ["🍬"] * TOTAL_SWEETS
    lives = [LIVES, LIVES]
    return sweets, lives

def display_board(sweets, lives, player_chars):
    print("\nSweets on the table:")
    for i, sweet in enumerate(sweets):
        print(f"{i+1}:{sweet}", end="  ")
    print("\n")
    print(f"{player_chars[0]} lives: {lives[0]} | {player_chars[1]} lives: {lives[1]}")

def take_turn(player_num, sweets, opponent_poison, lives, player_chars, player2_is_computer):
    print(f"\n{player_chars[player_num]}'s turn!")
    time.sleep(0.5)
    if player2_is_computer and player_num == 1:
        available = [i for i, s in enumerate(sweets) if s != "❌"]
        choice = random.choice(available)
        print(f"🤖 Computer chooses sweet #{choice+1}")
        time.sleep(1)
    else:
        while True:
            try:
                choice = int(input(f"Choose a sweet to eat (1-{len(sweets)}): ")) - 1
                if choice < 0 or choice >= len(sweets):
                    print("⚠️ Invalid choice.")
                    continue
                if sweets[choice] == "❌":
                    print("❌ Sweet already eaten.")
                    continue
                break
            except ValueError:
                print("⚠️ Enter a number.")

    # Check for poison from opponent
    if choice in opponent_poison:
        print("💀 Oh no! That sweet was poisoned!")
        lives[player_num] -= 1
    else:
        print("😋 Safe sweet!")
    sweets[choice] = "❌"
    time.sleep(1)
    return lives

def game():
    clear()
    display_title()
    input("Press Enter to Start Game...")
    clear()

    # Choose characters
    player1_char = choose_character(1)
    print("Do you want Player 2 to be human or computer?")
    while True:
        choice = input("Enter 'h' for human or 'c' for computer: ").lower()
        if choice in ["h", "c"]:
            player2_is_computer = choice == "c"
            break
        print("⚠️ Invalid choice.")
    player2_char = choose_character(2) if not player2_is_computer else "🤖"
    player_chars = [player1_char, player2_char]

    # Pick poisoned sweets
    sweets, lives = initialize_game(player2_is_computer)
    poison_player1 = pick_poison(0, sweets, player_is_computer=False)
    poison_player2 = pick_poison(1, sweets, player_is_computer=player2_is_computer)

    current_player = 0

    # Game loop
    while all(life > 0 for life in lives):
        clear()
        display_board(sweets, lives, player_chars)
        opponent_poison = poison_player2 if current_player == 0 else poison_player1
        lives = take_turn(current_player, sweets, opponent_poison, lives, player_chars, player2_is_computer)
        if lives[current_player] == 0:
            print(f"\n💥 {player_chars[current_player]} lost all lives!")
            winner = 1 - current_player
            print(f"🏆 {player_chars[winner]} wins the game!")
            break
        current_player = 1 - current_player

    # Replay option
    replay = input("\nDo you want to play again? (y/n): ").lower()
    if replay == "y":
        game()
    else:
        print("👋 Thanks for playing Sweet Danger!")

game()
