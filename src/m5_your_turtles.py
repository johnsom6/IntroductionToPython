"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Madi Johnson.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()


# first SimpleTurtle
geoff = rg.SimpleTurtle('turtle')
geoff.speed = 10
size = 50

for k in range(0,5):

    # change color with each loop
    if k == 0:
        geoff.pen = rg.Pen('purple','5')
    if k == 1:
         geoff.pen = rg.Pen('blue','5')
    if k == 2:
        geoff.pen = rg.Pen('red', '5')
    if k == 3:
         geoff.pen = rg.Pen('green','5')
    if k == 4:
         geoff.pen = rg.Pen('yellow','5')

# drawing the circle
    geoff.draw_circle(size)

    geoff.pen_down()
    size = size + 10


# second SimpleTurtle
marvin = rg.SimpleTurtle()
marvin.speed = 10

size2 = 200

for k in range(0,5):

# change color with each loop
    if k == 0:
        marvin.pen = rg.Pen('orange','3')
    if k == 1:
         marvin.pen = rg.Pen('blue violet','3')
    if k == 2:
        marvin.pen = rg.Pen('coral', '3')
    if k == 3:
         marvin.pen = rg.Pen('cyan','3')
    if k == 4:
         marvin.pen = rg.Pen('dark gray','3')

# drawing the square
    marvin.draw_square(size2)
    marvin.pen_up()
    marvin.left(45)
    marvin.forward(10)
    marvin.right(45)

    marvin.pen_down()
    size2 = size2 - 10
#-------------------------------------------------------------------------------------------------------



