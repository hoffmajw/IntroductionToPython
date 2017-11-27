"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jaxon Hoffman.
"""
########################################################################
# Done
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done
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

jax = rg.SimpleTurtle()
george = rg.SimpleTurtle()

jax.pen = rg.Pen('purple', 10)
george.pen = rg.Pen('dark green', 10)

jax.speed = 20
george.speed = 10

radius = 300
size = 600

jax.pen_up()
jax.forward(300)
jax.left(90)
jax.pen_down()

for k in range(3):

    jax.draw_circle(radius)

    jax.pen_up()
    jax.left(90)
    jax.forward(100)
    jax.right(90)
    jax.pen_down()

    radius = radius - 100

george.pen_up()
george.forward(300)
george.right(90)
george.forward(300)
george.right(180)
george.pen_down()

for k in range(3):
    george.draw_square(size)

    george.pen_up()
    george.forward(300)
    george.left(90)
    george.forward(100)
    george.left(90)
    george.forward(200)
    george.left(180)
    george.pen_down()

    size = size - 200

window.close_on_mouse_click()