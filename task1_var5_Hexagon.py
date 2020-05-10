import turtle

hexagon = turtle.Turtle()
hexagon.speed(100)

def draw(length):
    for i in range(6):
        hexagon.left(-30)
        hexagon.fd(length)
        hexagon.left(-30)

def hex(num):
    for _ in range(num):
        draw(30)
        hexagon.up()
        hexagon.fd(52)
        hexagon.down()

koordX = -300
koordY = 0
for j in range(9, 4, -1):
    koordX += 26
    koordY += 45
    hexagon.up()
    hexagon.setpos(koordX, koordY)
    hexagon.down()
    hex(j)

koordX1 = -248
koordY1 = 0
hexagon.up()
hexagon.setpos(koordX1, koordY1)
hexagon.down()

for k in range(8, 4, -1):
    hex(k)
    koordX1 += 26
    koordY1 -= 45
    hexagon.up()
    hexagon.setpos(koordX1, koordY1)
    hexagon.down()

input()
