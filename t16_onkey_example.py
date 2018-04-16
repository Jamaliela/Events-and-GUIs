######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# T16: Events
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


# The next four functions are our "event handlers".
def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    wn.bye()                        # Close down the turtle window


def main():
    global wn
    global tess

    wn = turtle.Screen()                 # Get a reference to the window
    wn.setup(400,500)                    # Determine the window size
    wn.title("Handling keypresses!")     # Change the window title
    wn.bgcolor("lightgreen")             # Set the background color

    tess = turtle.Turtle()               # Create our favorite turtle

    # These lines "wire up" keypresses to the handlers we've defined.
    wn.onkey(h1, "Up")
    wn.onkey(h2, "Left")
    wn.onkey(h3, "Right")
    wn.onkey(h4, "q")

    # Now we need to tell the window to start listening for events,
    # If any of the keys that we're monitoring is pressed, its
    # handler will be called.
    wn.listen()

    wn.mainloop()


main()
