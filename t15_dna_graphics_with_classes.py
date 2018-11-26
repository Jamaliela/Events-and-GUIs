######################################################################
# Author: Scott Heggen & Emily Lovell    TODO: Ela Jamali & Emely Alfaro
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


class DNADraw:
    # Class variables which will be used throughout the program.
    nucleotides = {"A": "pink", "T": "green", "C": "magenta", "G": "yellow"}
    complement = {"T": "A", "A": "T", "G": "C", "C": "G"}
    max_bases = 4
    
    def __init__(self):
        self.letter_turtle = turtle.Turtle()
        self.letter_turtle.hideturtle()
        self.letter_turtle.penup()
    
        self.draw_scaffold()
    
        self.current_base = 1
        self.current_letter = random.choice(list(self.nucleotides.keys()))        # Picks a random letter from the dictionary keys
        self.base_turtle = turtle.Turtle()
    
        self.draw_random_DNA()      # Draws a random DNA
    
        self.base_turtle.onclick(self.base_handler)       # Binds the first turtle to the base_handler event handler

        self.wn = turtle.Screen()
        self.wn.onkey(self.quit_program, "q")     # Binds to the quit_program event handler above
        self.wn.listen()                          # Needed to capture events
        self.wn.mainloop()                        # Keeps the program running

    def quit_program(self):
            """
            Event handler for quitting the program

            :return: None
            """
            self.wn.bye()

    def draw_scaffold(self):
        """
        Create the top and bottom scaffold for the nucleotides to be added
        afterwards.
    
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

    def draw_random_DNA(self):
        """
        Draw a random sequence to be used later to create he complementary base pair

        :return: None
        """
        self.base_turtle.penup()
        self.base_turtle.right(90)
        self.base_turtle.setpos(-250 + 95 * self.current_base, 230)
        self.base_turtle.pendown()
        self.base_turtle.shape("square")
        self.base_turtle.pensize(10)
        self.base_turtle.forward(50)
        self.base_turtle.color(self.nucleotides[self.current_letter])
        self.base_turtle.pensize(30)
        self.base_turtle.forward(70)
        self.base_turtle.backward(40)
        self.base_turtle.color("black")
    
        # draw out the letters for the base_turtles and return back to the center.
        (xpos, ypos) = self.base_turtle.pos()
        self.letter_turtle.setpos(xpos, ypos+5)
        self.letter_turtle.write(self.current_letter, move=False, align='center', font=("Arial", 25, ("bold", "normal")))
        self.letter_turtle.setpos(0,0)

    def draw_complement(self, x, y):
            """
            Draws the complement strand for a given letter at the correct location
    
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
            pair_turtle.color(self.nucleotides[self.complement[self.current_letter]])          # sets the color to the complement's color
            pair_turtle.pensize(30)
    
            (x_pos, y_pos) = pair_turtle.pos()
    
            pair_turtle.back(70)
            pair_turtle.penup()
    
            # draw the letter for that base
            self.letter_turtle.setpos(x_pos, y_pos - 10)
            self.letter_turtle.write(self.complement[self.current_letter], move=False, align='center', font=("Arial", 25, ("bold", "normal")))
            self.letter_turtle.setpos(0, 0)
    
            # Resets stuff
            pair_turtle.back(70)
            pair_turtle.showturtle()
            pair_turtle.color("black")

    def base_handler(self, x, y):
        """
        Event handler for clicks on turtles.
        Draws the complement strand.
        Each turtle reuses this handler.
    
        :param x: x-coordinate of the mouse
        :param y: y-coordinate of the mouse
        :return: None
        """

        self.draw_complement(x, y)           # Draw the complement strand
        self.current_base += 1
        if self.current_base <= self.max_bases:
            # Repeat the program up to four times. Creates a new letter, new turtle, and reuses the click handler base_handler
            self.current_letter = random.choice(list(self.nucleotides.keys()))
            self.base_turtle = turtle.Turtle()
            self.draw_random_DNA()
            self.base_turtle.onclick(self.base_handler)


def main():
    """
    Interactive DNA sequence drawing program.

    :return: None
    """

    dna = DNADraw()     # Yup. that's it!
    # DNADraw()           # Technically, this would work also. Why?


main()
