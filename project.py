import random
import emoji
from tabulate import tabulate

# duplicates_allowed will be 1 or 0

def generate_code(difficulty, duplicates_allowed):

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

    print(tabulate(rounds_table, headers, tablefmt = "grid", colalign=("center", "center")))

