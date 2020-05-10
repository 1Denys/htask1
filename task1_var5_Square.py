import turtle

square = turtle.Turtle()
square.speed(10)

def draw(length):
    for i in range(4):
        square.fd(length)
        square.left(90)
draw(200)
x = 40
def line():
    square.fd(x)
    square.left(90)
    square.fd(200)
    square.up()
    square.home()
    square.down()

for j in range(4):
    line()
    x += 40

input()
