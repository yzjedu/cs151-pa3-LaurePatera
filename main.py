# Programmers:  Laure Patera
# Course:  CS151, Dr. Zee
# Due Date: 11/7/24
# Programming Assignment:  PA 3
# Problem Statement: allows the user to pick between options that each output ASCII art
# Data In: option (string, allows the user to pick which ASCII art option they would like), line_character (string, determines character that will be used to create a line), character_number (integer, determines how many of the character will create the line), line_number (integer, determines how many lines will be outputted)
# Data Out:  an ASCII art circle, a line or series of lines in ASCII, or a random one of three ASCII art images
# Credits: https://stackoverflow.com/questions/23623288/print-full-ascii-art
import random
#Purpose: Simulates rolling two dice and finding the sum
#Name: calc_dice_sum
#Params: none
#Return: dice_sum as an integer, represents the sum of dice from one simulated roll
def output_circle():
    print('    *  *')
    print(' *        *')
    print('*          *')
    print('*          *')
    print(' *        *')
    print('    *  *')

def output_line(line_character, character_number, line_number):
    line_count = 0
    while line_count < line_number:
        line = line_character * character_number
        print(line)
        line_count += 1

def random_art():
    art_option = random.randint(1, 3)
    if art_option == 1:
        print(r"""

                                           ._ o o
                                           \_`-)|_
                                        ,""       \ 
                                      ,"  ## |   ಠ ಠ. 
                                    ," ##   ,-\__    `.
                                  ,"       /     `--._;)
                                ,"     ## /
                              ,"   ##    /


                        """)

    elif art_option == 2:
        output_circle()
        print(r"    /__\ ")
        string_count = 0
        while string_count < 6:
            print('      )')
            print('      (')
            string_count += 1

    elif art_option == 3:
        output_line('~', 5, 1)
        print('|    |')
        output_line('~', 13, 1)
        print('|            |')
        output_line('~', 21, 1)
        print('|                    |')
        output_line('~', 29, 1)
        print('|                            |')
        output_line('~', 37, 1)
        print('|                                    |')
        output_line('~', 37, 1)

def main():
    print('Welcome to the ASCII Art Program!')
    option = input('What ASCII art would you like to display? \nTo display a circle, enter 1.\nTo display line(s), enter 2.\nTo display a random picture, enter 3.')
    while option != '1' and option != '2' and option != '3':
        option = input('What ASCII art would you like to display? \nTo display a circle, enter 1.\nTo display line(s), enter 2.\n To display a random picture, enter 3.')
    if option == '1':
        output_circle()
    if option == '2':
        line_character = str(input('What character would you like to use?'))
        character_number = int(input('How many characters long should your line be?'))
        while character_number <= 0:
            character_number = int(input('How many characters long should your line be?'))
        line_number = int(input('How many lines would you like to output as an integer?'))
        while line_number <= 0:
            line_number = int(input('How many lines would you like to output as an integer?'))
        output_line(line_character, character_number, line_number)
    if option == '3':
        random_art()
    print('Thank you for using this program!')

main()
