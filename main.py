# Programmers:  Laure Patera
# Course:  CS151, Dr. Zee
# Due Date: 11/7/24
# Programming Assignment:  PA 3
# Problem Statement: allows the user to pick between options that each output ASCII art
# Data In: option (string, allows the user to pick which ASCII art option they would like), line_character (string, determines character that will be used to create a line), character_number (integer, determines how many of the character will create the line), line_number (integer, determines how many lines will be outputted)
# Data Out:  either an ASCII art circle, a line or series of lines using ASCII, or a random one of three options of ASCII art images
# Credits: https://stackoverflow.com/questions/23623288/print-full-ascii-art

import random

#Purpose: outputs an ASCII art circle
#Name: output_circle
#Params: none
#Return: none
def output_circle():
    print('    *  *')
    print(' *        *')
    print('*          *')
    print('*          *')
    print(' *        *')
    print('    *  *')


#Purpose: outputs a line or series of lines with characteristics defined by user input
#Name: output_line
#Params: line_character (string, character used to create line), character_number (integer, number of characters used to determine how long the line is), line_number (integer, number of lines outputted)
#Return: none
def output_line(line_character, character_number, line_number):

    #prints each line repeated by a certain number of times as defined by the value of line_number
    line_count = 0
    while line_count < line_number:

       #prints each character repeated a certain number of times as defined by the value of character_number
        line = line_character * character_number
        print(line)
        line_count += 1


#Purpose: picks a random ASCII art image from three options given and outputs it to the user
#Name: random_art
#Params: none
#Return: none
def random_art():

    #randomizes which image will be displayed of the three
    art_option = random.randint(1, 3)

    #creates the first image
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


    #Creates the second image
    elif art_option == 2:

       #call function output_circle
        output_circle()
        print(r"    /__\ ")

       #prints the given characters 6 times
        string_count = 0
        while string_count < 6:
            print('      )')
            print('      (')
            string_count += 1


    #creates the third image
    elif art_option == 3:
        #call function output_line with arguments line_character, character_number, and line_number, multiple times in different lengths to create an ASCII image of steps
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



#Purpose: main function
#Name: main
#Params: none
#Return: none
def main():

    #output purpose to the user
    print('Welcome to the ASCII Art Program! This program outputs various ASCII art images and allows you to choose which you would like to display.')
    option = input('What ASCII art would you like to display? \nTo display a circle, enter 1.\nTo display line(s), enter 2.\nTo display a random picture, enter 3.')

    #error checking to make sure that user input is either 1, 2, or 3
    while option != '1' and option != '2' and option != '3':
        option = input('What ASCII art would you like to display? \nTo display a circle, enter 1.\nTo display line(s), enter 2.\n To display a random picture, enter 3.')

    #displays circle if user picks option 1
    if option == '1':
       #call function output_circle
        output_circle()

    #displays line(s) if user picks option 2
    if option == '2':

       #asks user the characteristics they want for the line(s)
        line_character = str(input('What character would you like to use?'))
        character_number = int(input('How many characters long should your line be?'))

        #error checking to make sure that user inputs a positive number
        while character_number <= 0:
            character_number = int(input('How many characters long should your line be?'))
        line_number = int(input('How many lines would you like to output as an integer?'))

        #error checking to make sure that user inputs a positive number
        while line_number <= 0:
            line_number = int(input('How many lines would you like to output as an integer?'))

       #call function output_line with arguments line_character, character_number, and line_number
        output_line(line_character, character_number, line_number)

    #displays random ASCII art if user picks option 3
    if option == '3':

       #call function random_art
        random_art()

    #Output exit message
    print('Thank you for using this program!')


#Calls main function
main()
