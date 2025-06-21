# Here its a game with  chat gpt touches

import random

def print_welcome(name):
    print("+" + "=" * 80 + "+")
    print(f"Welcome, {name}! 👋")
    print("This is the Rock, Paper, Scissors Game 🎮")
    print("How to play:")
    print("- Type [r] for Rock 🪨")
    print("- Type [p] for Paper 📄")
    print("- Type [s] for Scissors ✂️")
    print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("Each win gives 1 point. Let’s start! 💪")
    print("+" + "=" * 80 + "+")

def get_user_choice():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        user_input = input("\nYour choice? [r]ock, [p]aper, [s]cissors: ").lower()
        if user_input in choices:
            return user_input, choices[user_input]
        else:
            print("❌ Invalid input. Please try again.")

def get_pc_choice():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    pc_input = random.choice(['r', 'p', 's'])
    return pc_input, choices[pc_input]

def determine_winner(user, pc):
    if user == pc:
        return "It's a tie! 🤝", 0
    elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        return "You win this round! 🎉", 1
    else:
        return "PC wins this round! 😢", -1

def play_again():
    again = input("\nDo you want to play again? (y/n): ").lower()
    return again == 'y'

def main():
    print("+" + "=" * 80 + "+")
    name = input("Enter your name: ")
    print("+" + "=" * 80 + "+")

    print_welcome(name)

    user_score = 0
    pc_score = 0

    while True:
        user_code, user_word = get_user_choice()
        pc_code, pc_word = get_pc_choice()

        print(f"\n🧍 {name} chose: {user_word}")
        print(f"🤖 PC chose: {pc_word}")

        result_text, score = determine_winner(user_code, pc_code)
        print(f"\nResult: {result_text}")

        if score == 1:
            user_score += 1
        elif score == -1:
            pc_score += 1

        print(f"\n📊 Current Score: {name} {user_score} - {pc_score} PC")

        if not play_again():
            print("\nThanks for playing! ❤️")
            if user_score > pc_score:
                print("🏆 Congratulations, you won the game!")
            elif user_score < pc_score:
                print("🙁 PC won the game. Better luck next time!")
            else:
                print("😅 It's a draw overall!")
            print("+" + "=" * 80 + "+")
            break

if __name__ == "__main__":
    main()
