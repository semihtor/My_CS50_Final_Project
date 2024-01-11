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
            print(emoji.emojize("Sorry, this game doesn't support any cheats :disappointed_face:"))

def main():
    check_user_guess_for_game_compatibility(4)

if __name__ == "__main__":
    main()
