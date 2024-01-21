# A Bulls and Cows Game In Python
## Video Demo:  https://youtu.be/6qj5TugYtvM
### Description:
This was my final project for conclude the course [CS50P Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/).

In this project, I aimed to create a playable version of the pen and paper game called **Bulls and Cows**.

More information about the game can be found at [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) on Wikipedia.

### Explaining My Design Choices

Bulls and Cows is game played by two players using numbers as both codes and hints. Each of the players use a table to fill their guesses and hints.

In my project, I set my first requirement as the game having a single player. The program will create a code and the player will try to guess it.

My next consideration was about the use of digit zero. When I searched online, I couldn't find any rules that explicitly prevent the use of zeroes. However, I chose this usage as another of my design decisions.

My next consideration was about the difficulty. After some consideration, I concluded that there are three ways that I can provide a choice for difficulty:

1. **Code containing duplicate digits**: The player can choose to guess a code containing duplicate digits. The program can create the code according to the player's choice (yes or no).
2. **The length of the code**: The player can choose to guess a longer code. The program can create the code according to the player's choice (2, 3, 4 or 5).
3. **The number of rounds**: After the player chooses the length of the code, another level of difficulty can be added by limiting the number of rounds. The program lets the player enter a guess for different amount of rounds according to difficulty (6|9|12|15 rounds for 2|3|4|5 digits)

To make my version of the game stand out, I decided on two design elements:

1. **The use of emoji library for hints**: In the original game, the hints (bulls and cows) are presented with numbers. Instead of this, I decided to use colored circle emojis (from Mastermind version of the game). While selecting the colors, I considered if the player's terminal has a darker or lighter colored background. That's why I decided to use green and yello colored circle emojis. Because they can be comfortably displayed on a darker or lighter terminal window. Also, their similarity to traffic lights can be easily understood by the player.
2. **The use of tabulate library for creating the gameboard**: In the original game, the guesses and hints are organized nicely on a table. I wanted to implement this organization in my version, so I used the tabulate library to create the gameboard.

### Explaining My Coding Choices

My code contains a main function (**bulls_and_cows_game**) and three custom functions (**generate_secret_code, evaluate_guess and display_board**).

1. **generate_secret_code Custom Function**: In this function, the program generates a code according to the difficulty and duplicate choices made by the player.
2. **evaluate_guess Custom Function**: In this function, the program compares the user's guess against the code it created.
3. **display_board Custom Function**: In this function, the program creates the game board after getting user's answer and the resulting hints for that answer. Each previous guess and it's hints are displayed in order to provide the player more information about their past guesses.

My code contains **os, sys, random, emoji, tabulate, pyfiglet and inflect** external libraries.
1. **os External Library**: I use this library to clear the screen at certain point of the code. This helps the display to stay cleaner.
2. **sys External Library**: I use this library to handle when the player exits the program using a keyboard interrupt.
3. **random External Library**: I use this library to create a random code if the player chooses to allow duplicate digits.
4. **emoji External Library**: I use this library to display hints with emojis. I also use emojis in certain messages that are displayed.
5. **tabulate External Library**: I use this library to create an organized gameboard.
6. **pyfiglet External Library**: I use this library to create the splash screen at the start of the program.
7. **inflect External Library**: I use this library to display the number of remaining rounds information (depending it's plurality or singularity) correctly.

### Unique Issues I've Encountered During Development

After running my custom **display_board** function during some testing, I noticed that the right-most limiter for rows containing emojis were out of line compared to the headers' right-most limiter.

I figured that this had to be related to using emojis in tabulate's table but my Google searches returned no relevant information. Either I was using wrong keywords for the search, or I was the first person to encounter such an error.

After removing emojis from my search keywords and just searching for excessive width in tabulate library, I found some information regarding the use of East Asian Alphabet characters in tabulate. Since these characters sometime required more space compared to the Latin Alphabet characters, a special library (tabulate[widechars]) needed to be installed with tabulate. After installing this library with pip (in addition to the standard tabulate previously installed), I haven't encountered this behaviour again.

### About CS50

CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

**My sincerest thanks to everyone who contributed to the creation of this amazing source of learning.**
