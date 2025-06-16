import turtle as t

SCREENWIDTH = 600
SCREENHEIGHT = 600

PROJECTILE_SPEED = 1
FORCE_FACTOR = 30

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 50

RESPONSE_POS = (0, 25)

# Set up pen for drawing target
targetPen = t.Turtle()
targetPen.hideturtle()

# Set up pen for writing result or response
resultPen = t.Turtle()
resultPen.hideturtle()
resultPen.speed(0)
resultPen.penup()
resultPen.goto(RESPONSE_POS[0], RESPONSE_POS[1])
resultPen.pendown()
resultPen.pencolor("red")

# Set up pen for marking
markPen = t.Turtle()
markPen.hideturtle()
markPen.speed(0)
markPen.penup()


def main():
    play_again = True
    clear_response()

    while play_again:
        into_the_game()

        ans = t.textinput("Play Again?", "Do you want to play again?")
        if not (ans.lower() == "yes" or ans.lower() == "y"):
            play_again = False

    write_response("Thanks for playing!")
    t.done()

def into_the_game():
    """The entire game Module"""

    create_target()
    t.penup()

    to_start_point()

    target_hit = False

    clear_mark()

    while not target_hit:

        t.pendown()
        t.showturtle()

        angle = get_angle()
        force = get_force()

        distance = force * FORCE_FACTOR

        shoot_the_arrow(angle, distance)

        currentX = t.xcor()
        currentY = t.ycor()

        inTargetX = currentX > TARGET_LLEFT_X and currentX < TARGET_LLEFT_X + TARGET_WIDTH
        inTargetY = currentY > TARGET_LLEFT_Y and currentY < TARGET_LLEFT_Y + TARGET_WIDTH

        if inTargetX and inTargetY:
            result = "You hit the target!"
            target_hit = True
        else:
            result = "Try again!"

        mark(currentX, currentY)

        write_response(result)

        t.penup()
        t.hideturtle()
        t.clear()
        to_start_point()

def create_target():
    """Create a box for target"""

    t.setup(SCREENWIDTH, SCREENHEIGHT)
    targetPen.hideturtle()
    targetPen.speed(0)
    targetPen.penup()
    targetPen.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    targetPen.pendown()
    targetPen.setheading(EAST)
    targetPen.forward(TARGET_WIDTH)
    targetPen.setheading(NORTH)
    targetPen.forward(TARGET_WIDTH)
    targetPen.setheading(WEST)
    targetPen.forward(TARGET_WIDTH)
    targetPen.setheading(SOUTH)
    targetPen.forward(TARGET_WIDTH)


def to_start_point():
    """Return the player arrow to starting position
    Use on starting game or when starting new try"""

    t.home()
    t.setheading(EAST)
    t.speed(PROJECTILE_SPEED)


def get_angle():
    """Pop up to get the angle for arrow"""

    angle = t.numinput(title="angle",
               prompt='Enter the angle for shooting (in degrees)',
               default=0,
               minval=0,
               maxval=360)

    return angle

def get_force():
    """Pop up to get the force for arrow"""

    force = t.numinput(title="force",
                       prompt='Enter the force for shooting (1-10)',
                       default=0,
                       minval=1,
                       maxval=10)

    return force

def shoot_the_arrow(angle, distance):
    """Shoot the arrow
    Use after player enter the angle and force"""

    t.setheading(angle)
    t.forward(distance)

def write_response(response):
    """Write the response text to the screen
    also clear the older response"""

    resultPen.pendown()
    clear_response()
    resultPen.write(arg=response,
                    align='center',
                    font=('Arial', 14, 'bold'),)
    resultPen.penup()

def clear_response():
    """Clear the current text on the screen"""

    resultPen.clear()

def mark(x, y):
    """Mark the previous position on the screen
    Use after shot the arrow"""

    markPen.penup()
    markPen.goto(x, y)
    markPen.pendown()
    markPen.dot(5)

def clear_mark():
    """Clear all the mark on the screen
    Use when starting new game"""

    markPen.clear()

if __name__ == '__main__':
    main()