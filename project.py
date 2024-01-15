import random
import emoji
from tabulate import tabulate

class AnswerNotAllDigitsException(Exception):
    "Raised when the input value is not all digits"
    pass

class AnswerNotCompatibleWithDifficultyException(Exception):
    "Raised when the input value is not compatible with difficulty"
    pass
class NoCheatCodeError(Exception):
    "Raised when the input value is Konami cheat code"
    pass


def generate_code(difficulty, duplicates_allowed):
    # duplicates_allowed will be 1 or 0
    code = ""

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if duplicates_allowed == 1:
        for _ in range(0, difficulty):
            random_integer = str(random.randint(1, 9))
            code += random_integer
    else:
        random.shuffle(numbers)
        for x in range(0, difficulty):
            code += str(numbers[x])
    return code

def create_game_board(difficulty):
    
    headers = ["GUESS", "RESPONSE"]

    #round count according to difficulty
    round_count = {2: 6, 3: 9, 4: 12, 5: 15}

    guess_placeholder = " G " * difficulty

    red_circle = emoji.emojize(":red_circle:")

    white_cricle = emoji.emojize(":white_circle:")

    response_placeholder = (red_circle + white_cricle) * 2

    rounds_placeholder = [guess_placeholder, response_placeholder]

    rounds_table = []

    for x in range(0, round_count[difficulty]):
        rounds_table.insert(x, rounds_placeholder)

    # print(rounds_table)
    
    print(tabulate(rounds_table, headers, tablefmt = "grid", colalign=("center", "center")))

def compare_answer_to_generated_code(code, answer, difficulty):
    #code answer will be 2,3,4 or 5 digit numbers turned to strings
    correct_digit = 0

    correct_placement = 0
    
    x = 0

    for x in range(0, difficulty):
        if answer[x] == code[x]:
            correct_placement += 1
        elif answer[x] in code:
            correct_digit += 1
    
    return correct_placement, correct_digit
    
def check_user_guess_for_game_compatibility(difficulty):
    
    while True:
        
        try:
            user_guess = input("Please enter your guess: ")

            if user_guess == "up up down down left right left right b a start" or user_guess == "up up down down left right left right b a select":
                raise NoCheatCodeError
            else:
                user_guess = user_guess.replace(" ", "")
            
            if not user_guess.isdigit():
                raise AnswerNotAllDigitsException
            elif len(user_guess) != difficulty:
                raise AnswerNotCompatibleWithDifficultyException
            else:
                return user_guess
        
        except AnswerNotCompatibleWithDifficultyException:
            print(f"Please enter an answer containing {difficulty} digits")

        except AnswerNotAllDigitsException:
            print("Please enter an answer containing only digits")
        
        except NoCheatCodeError:
            print(emoji.emojize("Sorry, this game doesn't support the iconic KONAMI code :disappointed_face:"))


def main():
    
    print("Welcome to Bulls and Cows game in Python.")
    duplicate_preference = False

    #round count according to difficulty
    round_count_per_difficulty = {2: 6, 3: 9, 4: 12, 5: 15}

    # Ask to display the rules or not
    while True:

        try:
            rule_display = input("Would you like to know the rules? (y/n) ")

            if rule_display == "y":
                print("Bulls and Cows is a code-breaking game for two players.\n" + 
                      "Two opponents who aim to decipher the other's 4-digit secret code by trial and error in turns.\n" + 
                      "For each correct digit in a correct place guessed by the guesser, the other player declares 'Bull'.\n" + 
                      "For each correct digit in an incorrect place guessed by the guesser, the other player declares 'Cows'.\n" + 
                      "Whichever player deciphers the other player's code first, that player wins.\n" + 
                      "In this Python version, there is only one player (you). The program generates the code and the player tries to decipher it.\n" + 
                      "As an added difficulty, the player is asked if duplicate numbers are allowed or not.\n" + 
                      "The player chooses a difficulty (2, 3, 4 or 5 + . This determines the digits in the code and the number of rounds.\n" + 
                      emoji.emojize("A correct digit in a correct place is indicated with a :green_circle:.\n")  + 
                      emoji.emojize("A correct digit in an incorrect place is indicated with a :yellow_circle:.\n") + 
                      "If the player isn't able to guess the code before the number of rounds are up, the game is lost.")
                input("Press ENTER when you're ready to play.")
                # Finish displaying the rules and start the game
                break
            elif rule_display == "n":
                # Skip displaying the rules and start the game
                break
            else:
                # Ask again for an appropriate input
                raise IncorrectRuleAnswerError
        
        except IncorrectRuleAnswerError:
            print(f"Please answer only using " + "\033[1m" + "y" + "\033[0m" + " or " + "\033[1m" + "n" + "\033[0m" + " characters")
        
        except (KeyboardInterrupt):
            # User terminated program
            print("\nProgram terminated by the user.")
            sys.exit()
    
    # Ask if duplicates are allowed or not
    while True:

        try:
            duplicates_allowed = input("Would you like to allow duplicate digits in the code to increase the difficulty? (y/n) ")

            if duplicates_allowed == "y":
                print("Duplicate digits may be present in the code.")
                duplicate_preference = True
                break
            elif duplicates_allowed == "n":
                print("Duplicate digits will not be present in the code.")
                duplicate_preference = False
                break
            else:
                # Ask again for an appropriate input
                raise IncorrectRuleAnswerError
        
        except IncorrectRuleAnswerError:
            print(f"Please answer only using " + "\033[1m" + "y" + "\033[0m" + " or " + "\033[1m" + "n" + "\033[0m" + " characters")
        
        except KeyboardInterrupt:
            # User terminated program
            print("\nProgram terminated by the user.")
            sys.exit()

    # Ask to enter the difficulty
    while True:

        try:
            chosen_difficulty = input("Enter difficulty (2, 3, 4 or 5): ")

            if int(chosen_difficulty) in range (1, 5):
                print(f"The code will have {chosen_difficulty} digits.")
                break
            elif int(chosen_difficulty) not in range (1, 5):
                # Entered difficulty not a number between 
                print("Please enter the difficulty between 2 and 5 (inclusive).")
            else:
                # Entered difficulty contains a non-number
                raise ValueError
        
        except (ValueError):
            print("Please enter the difficulty as numbers between 2 and 5 (inclusive).")
        
        except (KeyboardInterrupt):
            # User terminated program
            print("\nProgram terminated by the user.")
            sys.exit()

    ...
    # duplicate_preference is True or False
    generated_code = generate_code(int(chosen_difficulty), duplicate_preference)

    headers = ["GUESS", "RESPONSE"]

    while True:

        try:
            if ...:
                ...
            elif ...:
                ...
            else:
                ...
        except:
            ...
    


if __name__ == "__main__":
    main()
