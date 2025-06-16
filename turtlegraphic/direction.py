import turtle as t

t.setup(600, 600)
t.pensize(2)

NORTH_POSITION = (0, 200)
EAST_POSITION = (200, 0)
SOUTH_POSITION = (0, -200)
WEST_POSITION = (-200, 0)
CIRCLE_BASE = (0, -30)

t.penup()
t.goto(NORTH_POSITION)
t.pendown()
t.goto(SOUTH_POSITION)
t.penup()

t.goto(EAST_POSITION)
t.pendown()
t.goto(WEST_POSITION)
t.penup()

t.goto(NORTH_POSITION)
t.write('North', align='center', font=('Arial', 16))

t.goto(EAST_POSITION)
t.setx(EAST_POSITION[0]+30) #move a little for space
t.write('East', align='center', font=('Arial', 16))

t.goto(SOUTH_POSITION)
t.sety(SOUTH_POSITION[1]-30) #move a little for space
t.write('South', align='center', font=('Arial', 16))

t.goto(WEST_POSITION)
t.setx(WEST_POSITION[0]-30) #move a little for space
t.write('West', align='center', font=('Arial', 16))

t.goto(CIRCLE_BASE)
t.pendown()
t.circle(30)


t.done()