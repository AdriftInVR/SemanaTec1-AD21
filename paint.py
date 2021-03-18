from turtle import up, goto, down, begin_fill, \
    forward, left, end_fill, setup, onscreenclick, \
    listen, onkey, undo, done, color, circle
from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        color("red")
        forward(end.x - start.x)
        left(90)

    end_fill()


def paint_circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    radius = end.x - start.x
    circle(radius)
    end_fill()


def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        color("blue")
        forward(end.x - start.x)
        left(90)
        forward(end.x - start.x)
        forward(end.x - start.x)
        left(90)

    end_fill()


def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        color("yellow")
        forward(end.x - start.x)
        left(60)

    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', paint_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
