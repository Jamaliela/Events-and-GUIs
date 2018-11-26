######################################################################
# Author: Scott Heggen & Emily Lovell     TODO: Ela Jamali & Emely Alfaro
# Username: heggens & lovelle             TODO: Jamalie & Alfarozaalae
#
# T15: Events and GUIs
#
# Purpose: Show interactive DNA strand copying using the turtle library.
#  This program also uses both mouse click and keypress event handling.
#  The mouse click causes the complementary nucleotides to appear under
#  the base that the user clicks on in the DNA strand.
# ######################################################################
# Acknowledgements:
#
# Original code written by Dr. Mario Nakazawa
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import random

# Global variables which will be used throughout the program.
global nucleotides
nucleotides = {"A": "pink", "T": "green", "C": "magenta", "G": "yellow"}

global complement
complement = {"T": "A", "A": "T", "G": "C", "C": "G"}

global max_bases                # We'll be using this variable inside an event handler, so it needs global scope
max_bases = 4


def draw_scaffold():
    """
    Create the top and bottom scaffold for the nucleotides
    to be added afterwards.

    :return: None
    """

    dna_protein = turtle.Turtle()
    dna_protein.hideturtle()
    dna_protein.shape("square")
    dna_protein.penup()
    dna_protein.setpos(-260,230)
    dna_protein.pendown()
    dna_protein.pensize(20)
    dna_protein.forward(500)

    dna_protein.penup()
    dna_protein.setpos(-260,-42)
    dna_protein.pendown()
    dna_protein.pensize(20)
    dna_protein.forward(500)

    dna_protein.penup()
    dna_protein.setpos(0,-170)
    dna_protein.write("Click on the black square for each nucleotide \nin the DNA strand created at the top\nto get the complement in the strand at the bottom!\n\nPress 'q' to quit.", move=False,align='center',font=("Arial",15,("bold","normal")))


def draw_random_DNA(current_base_turtle, base_index, letter):
    """
    Draw a random sequence to be used later to create the complementary base pair

    :param current_base_turtle: a turtle object
    :param base_index: an index, to help position the turtle
    :param letter: the letter being drawn
    :return: None
    """
    current_base_turtle.penup()
    current_base_turtle.right(90)
    current_base_turtle.setpos(-250 + 95*base_index, 230)       # Moves the turtle right the appropriate amount
    current_base_turtle.pendown()
    current_base_turtle.shape("square")
    current_base_turtle.pensize(10)
    current_base_turtle.forward(50)
    current_base_turtle.color(nucleotides[letter])
    current_base_turtle.pensize(30)
    current_base_turtle.forward(70)
    current_base_turtle.backward(40)
    current_base_turtle.color("black")

    # draw out the letters for the base_turtles and return back to the center.
    (xpos, ypos) = current_base_turtle.pos()
    letter_turtle.setpos(xpos, ypos+5 )
    letter_turtle.write(letter,move=False,align='center',font=("Arial",25,("bold","normal")))
    letter_turtle.setpos(0,0)


def draw_complement(letter, x, y):
        """
        Draws the complement strand for a given letter at the correct location.

        :param letter: the base letter
        :param x: the mouse x-coordinate
        :param y: the mouse y-coordinate
        :return: None
        """
        pair_turtle = turtle.Turtle()
        pair_turtle.hideturtle()
        pair_turtle.penup()
        pair_turtle.goto(x, y)
        pair_turtle.right(90)
        pair_turtle.forward(190)
        pair_turtle.pendown()
        pair_turtle.color("black")
        pair_turtle.pensize(10)
        pair_turtle.back(50)
        pair_turtle.color(nucleotides[complement[letter]])          # sets the color to the complement's color
        pair_turtle.pensize(30)

        (x_pos, y_pos) = pair_turtle.pos()

        pair_turtle.back(70)
        pair_turtle.penup()

        # draw the letter for that base
        letter_turtle.setpos(x_pos, y_pos - 10)
        letter_turtle.write(complement[letter], move=False, align='center', font=("Arial", 25, ("bold", "normal")))
        letter_turtle.setpos(0, 0)

        # Resets stuff
        pair_turtle.back(70)
        pair_turtle.showturtle()
        pair_turtle.color("black")


def base_handler(x, y):
    """
    Event handler for clicks on turtles.
    Draws the complement strand.
    Each turtle reuses this handler.

    :param x: x-coordinate of the mouse
    :param y: y-coordinate of the mouse
    :return: None
    """
    global current_letter
    global current_base

    draw_complement(current_letter, x, y)           # Draw the complement strand
    current_base += 1
    if current_base <= max_bases:
        # Repeat the program up to four times. Creates a new letter, new turtle, and reuses the click handler base_handler
        current_letter = random.choice(list(nucleotides.keys()))
        base_turtle = turtle.Turtle()
        draw_random_DNA(base_turtle, current_base, current_letter)
        base_turtle.onclick(base_handler)


def main():
    """
    Interactive DNA sequence drawing program.

    :return: None
    """
    global letter_turtle            # We'll be using this variable inside an event handler, so it needs global scope
    global current_base             # We'll be using this variable inside an event handler, so it needs global scope
    global current_letter           # We'll be using this variable inside an event handler, so it needs global scope

    letter_turtle = turtle.Turtle()
    letter_turtle.hideturtle()
    letter_turtle.penup()

    draw_scaffold()

    current_base = 1
    current_letter = random.choice(list(nucleotides.keys()))        # Picks a random letter from the dictionary keys
    base_turtle = turtle.Turtle()

    draw_random_DNA(base_turtle, current_base, current_letter)      # Draws a random DNA

    base_turtle.onclick(base_handler)       # Binds the first turtle to the base_handler event handler

    # It's not common, but sometimes useful to define functions within other functions.
    def quit_program():
        """
        Event handler for quitting the program

        :return: None
        """
        wn.bye()

    wn = turtle.Screen()
    wn.onkey(quit_program, "q")     # Binds to the quit_program event handler above
    wn.listen()                     # Needed to capture events
    wn.mainloop()                   # Keeps the program running


main()
