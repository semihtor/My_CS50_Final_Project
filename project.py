import os
import sys
import random
import emoji
from tabulate import tabulate
from pyfiglet import Figlet
import inflect

class AnswerNotAllDigitsException(Exception):
    "Raised when the input value is not all digits"
    pass

class AnswerNotCompatibleWithDifficultyException(Exception):
    "Raised when the input value is not compatible with difficulty"
    pass
class NoCheatCodeError(Exception):
    "Raised when the input value is Konami cheat code"
    pass

class IncorrectRuleAnswerError(Exception):
    "Raised when the user answers the rule question anything other than y or n"
    pass

def generate_secret_code(difficulty, duplicates_allowed_answer):
    # Generate a random 4-digit secret code with or without duplicate digits.
    # difficulty will be integer and duplicates_allowed_answer will be boolean
    # code will be generated as string
    code = ""

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if duplicates_allowed_answer:
        for _ in range(0, difficulty):
            random_integer = str(random.randint(1, 9))
            code += random_integer
    else:
        random.shuffle(numbers)
        for x in range(0, difficulty):
            code += str(numbers[x])
    return code

def evaluate_guess(code, answer):
    #code and answer will be 2,3,4 or 5 digit numbers turned to strings
    correct_digit = 0

    correct_placement = 0
    
    x = 0

    for x in range(0, len(code)):
        if answer[x] == code[x]:
            correct_placement += 1
        elif answer[x] in code:
            correct_digit += 1
    
    return correct_placement, correct_digit

def display_board(history):
    # Display the Bulls and Cows game board with emojis.
    headers = ["GUESS", "HINTS"]
    table = tabulate(history, headers, tablefmt="grid", colalign=("center", "center"))
    
    # clear screen before printing the board
    # posix is os name for Linux or mac
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')
    
    print(table)

def bulls_and_cows_game():

    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')

    p = inflect.engine()
    
    f = Figlet(font='doom', justify="center", width = 100)
    print("-" * 100, f.renderText('COWS   AND   BULLS'), "-" * 100, sep="\n")
    print("A CS50P FINAL PROJECT BY SEMİH TOR\n\n".center(100))
    
    #round count according to difficulty
    round_count_per_difficulty = {2: 6, 3: 9, 4: 12, 5: 15}
    
    # Ask to display the rules or not
    while True:

        try:
            rule_display = input("Would you like to know the rules? (y/n) ".center(100))

            if(os.name == 'posix'):
                os.system('clear')
            # else screen will be cleared for windows
            else:
                os.system('cls')

            if rule_display == "y":
                print("\nBulls and Cows is a code-breaking game for two players.\n" + 
                      "Two opponents who aim to decipher the other's 4-digit secret code by trial and error in turns.\n" + 
                      "For each correct digit in a correct place guessed by the guesser, the other player declares 'Bull'.\n" + 
                      "For each correct digit in an incorrect place guessed by the guesser, the other player declares 'Cows'.\n" + 
                      "Whichever player deciphers the other player's code first, that player wins.\n" + 
                      "In this Python version, there is only one player (you).\n" + 
                      "The program generates the code and the player tries to decipher it.\n" + 
                      "As an added difficulty, the player is asked if duplicate numbers are allowed or not.\n" + 
                      "The player chooses a difficulty (2, 3, 4 or 5).\n" +
                      "This determines the digits in the code and the number of rounds.\n" + 
                      emoji.emojize("Presence of a correct digit in a correct place is indicated with a :green_circle:.\n")  + 
                      emoji.emojize("Presence of a correct digit in an incorrect place is indicated with a :yellow_circle:.\n") + 
                      "Note that these indications can be for any digit of the code.\n" + 
                      "If the player isn't able to guess the code before the number of rounds are up, the game is lost.\n")
                input("Press ENTER when you're ready to play.".center(100))
                # Finish displaying the rules and start the game
                break
            elif rule_display == "n":
                # Skip displaying the rules and start the game
                break
            else:
                # Ask again for an appropriate input
                raise IncorrectRuleAnswerError
        
        except IncorrectRuleAnswerError:
            print(f"\nPlease answer only using " + "\033[1m" + "y" + "\033[0m" + " or " + "\033[1m" + "n" + "\033[0m" + " characters")
        
        except (KeyboardInterrupt):
            # User terminated program
            print("\n\nProgram terminated by the player.\n\n")
            sys.exit()
    
    duplicate_preference = False

    # Ask if duplicates are allowed or not
    while True:

        try:
            if(os.name == 'posix'):
                os.system('clear')
            # else screen will be cleared for windows
            else:
                os.system('cls')

            duplicates_allowed = input("\nAllow duplicate digits in the code to increase the difficulty? (y/n) ")
            
            if(os.name == 'posix'):
                os.system('clear')
            # else screen will be cleared for windows
            else:
                os.system('cls')

            if duplicates_allowed == "y":
                print("\nDuplicate digits may be present in the code.")
                duplicate_preference = True
                break
            elif duplicates_allowed == "n":
                print("\nDuplicate digits will not be present in the code.")
                duplicate_preference = False
                break
            else:
                # Ask again for an appropriate input
                raise IncorrectRuleAnswerError
        
        except IncorrectRuleAnswerError:
            print(f"Please answer only using " + "\033[1m" + "y" + "\033[0m" + " or " + "\033[1m" + "n" + "\033[0m" + " characters")
        
        except KeyboardInterrupt:
            # User terminated program
            print("\nProgram terminated by the player.\n\n")
            sys.exit()

    # Ask to enter the difficulty
    while True:

        try:
            chosen_difficulty = int(input("\nEnter difficulty (2, 3, 4 or 5): "))

            if(os.name == 'posix'):
                os.system('clear')
            # else screen will be cleared for windows
            else:
                os.system('cls')

            if chosen_difficulty in range (1, 5):
                print(f"\nThe code will have {chosen_difficulty} digits and you will have {round_count_per_difficulty[chosen_difficulty]} rounds to solve it.")
                break
            elif chosen_difficulty not in range (1, 5):
                # Entered difficulty not a number between 
                print("\nPlease enter the difficulty between 2 and 5 (inclusive).")
            else:
                # Entered difficulty contains a non-number
                raise ValueError
        
        except (ValueError):
            print("\nPlease enter the difficulty as numbers between 2 and 5 (inclusive).")
        
        except (KeyboardInterrupt):
            # User terminated program
            print("\n\nProgram terminated by the player.\n\n")
            sys.exit()

    round_count = 0

    try:
        generated_code = str(generate_secret_code(chosen_difficulty, duplicate_preference))
        # print("the code is", generated_code)
        # generated code is string
        history = []

        while round_count < round_count_per_difficulty[chosen_difficulty]:
            guess = str(input(f"Enter your guess ({chosen_difficulty} digits): "))

            if not guess.isdigit() or len(guess) != chosen_difficulty:
                print(f"Invalid input. Please enter a {chosen_difficulty}-digit number.")
                continue

            bulls, cows = evaluate_guess(generated_code, guess)
            green_circle = emoji.emojize(":green_circle:")
            yellow_circle = emoji.emojize(":yellow_circle:")
            hints = (green_circle * bulls) + (yellow_circle * cows)
            
            history.append([guess, hints])
            display_board(history)
            round_count += 1
            remaining_guess = round_count_per_difficulty[chosen_difficulty] - round_count

            if remaining_guess != 0:
                print("You have", remaining_guess, p.plural("guess", remaining_guess), "remaining.")

            if bulls == len(generated_code):
                print(emoji.emojize("Congratulations! You've guessed the secret code :party_popper: :party_popper:"))
                break
            
            if round_count == round_count_per_difficulty[chosen_difficulty]:
                print(f"Sorry, you weren't able to guess the secret code in {round_count_per_difficulty[chosen_difficulty]} rounds. It was {generated_code}.")
                print(emoji.emojize("Better luck next time :disappointed_face:"))


    except KeyboardInterrupt:
        print("\nProgram terminated by the player.\n\n")
    


if __name__ == "__main__":
    bulls_and_cows_game()
