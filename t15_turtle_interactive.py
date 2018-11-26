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
#   This code is adapted from:
#   http://openbookproject.net/thinkcs/python/english3e/events.html#mouse-events
#   by Dr. Mario Nakazawa
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


def h1(x, y):
    global tess
    tess.goto(x, y)


def main():
    global tess
    tess = turtle.Turtle()

    wn = turtle.Screen()
    wn.setup(400,500)
    wn.title("How to handle mouse clicks on the window!")
    wn.bgcolor("lightgreen")

    tess.color("purple")
    tess.pensize(3)
    tess.shape("circle")

    # NOTICE that the screen is responding to the click events!
    wn.onclick(h1)      # Wire up a click handler to the window.

    wn.mainloop()

main()
