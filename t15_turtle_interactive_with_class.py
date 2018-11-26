######################################################################
# Author: Scott Heggen & Emily Lovell     TODO: Ela Jamali & Emely Alfaro
# Username: heggens & lovelle             TODO: Jamalie & Alfarozaalae
#
# T15: Events and GUIs
#
# Purpose: To demonstrate how turtle object responds to mouse click events.
# ######################################################################
# Acknowledgements:
#
#   This code is adapted from http://openbookproject.net/thinkcs/python/english3e/events.html#mouse-events
#   by Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


class ClickyTurtle:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(400,500)
        self.wn.title("How to handle mouse clicks on the window!")
        self.wn.bgcolor("lightgreen")
        self.tess = turtle.Turtle()
        self.tess.color("purple")
        self.tess.pensize(3)
        self.tess.shape("circle")

                        # NOTICE that the screen is responding to the click events!
        self.wn.onclick(self.h1)      # Wire up a click handler to the window.

        self.wn.mainloop()

    def h1(self, x, y):
        self.tess.goto(x, y)


def main():
    c = ClickyTurtle()


main()
