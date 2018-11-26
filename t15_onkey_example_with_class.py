######################################################################
# Author: Scott Heggen & Emily Lovell     TODO: Ela Jamali & Emely Alfaro
# Username: heggens & lovelle             TODO: Jamalie & Alfarozaalae
#
# T15: Events and GUIs
#
# Purpose: To demonstrate how turtle object responds to key press events.
#   the up arrow would move the turtle forward
#   the right arrow would turn the turtle right by 45 degrees
#   the left arrow would turn the turtle left by 45 degrees
#   the "q" key would quit the application
# ######################################################################
# Acknowledgements:
#
#   This code is adapted from http://openbookproject.net/thinkcs/python/english3e/events.html#mouse-events
#   by Dr. Mario Nakazawa
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


class DrivenTurtle:

    def __init__(self):
        self.turt = turtle.Turtle()    # Create our favorite turtle
        self.wn = turtle.Screen()      # Get a reference to the window

        self.wn.setup(400, 500)  # Determine the window size
        self.wn.title("Handling keypresses!")  # Change the window title
        self.wn.bgcolor("lightgreen")  # Set the background color

        # These lines "wire up" keypresses to the handlers we've defined.
        self.wn.onkey(self.h1, "Up")
        self.wn.onkey(self.h2, "Left")
        self.wn.onkey(self.h3, "Right")
        self.wn.onkey(self.h4, "q")

        # Now we need to tell the window to start listening for events,
        # If any of the keys that we're monitoring is pressed, its
        # handler will be called.
        self.wn.listen()
        self.wn.mainloop()

    def h1(self):
        self.turt.forward(30)

    def h2(self):
        self.turt.left(45)

    def h3(self):
        self.turt.right(45)

    def h4(self):
        self.wn.bye()                        # Close down the turtle window


def main():

    h = DrivenTurtle()  # Make an instance of the class DrivenTurtle


main()
