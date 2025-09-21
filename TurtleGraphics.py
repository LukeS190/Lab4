#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

import turtle

# Draw a polygon with a given number of sides
def drawPolygon(t, sides, size=100):
    for _ in range(sides):
        t.forward(size)
        t.right(360 / sides)

# Draw a square with one corner filled in (1=top-left, 2=top-right, 3=bottom-left, 4=bottom-right)
def fillCorner(t, corner, size=100):
    t.penup()
    t.goto(0, 0)  # start at center
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    
    if corner == 1:  # top-left
        t.goto(-size/2, size/2)
        t.goto(0, size/2)
        t.goto(0, 0)
    elif corner == 2:  # top-right
        t.goto(0, size/2)
        t.goto(size/2, size/2)
        t.goto(size/2, 0)
        t.goto(0, 0)
    elif corner == 3:  # bottom-left
        t.goto(-size/2, 0)
        t.goto(0, 0)
        t.goto(0, -size/2)
        t.goto(-size/2, -size/2)
    elif corner == 4:  # bottom-right
        t.goto(0, 0)
        t.goto(size/2, 0)
        t.goto(size/2, -size/2)
        t.goto(0, -size/2)
    
    t.end_fill()

# Draw multiple squares inside each other
def squaresInSquares(t, num, size=100):
    for i in range(num):
        for _ in range(4):
            t.forward(size - i*10)
            t.right(90)
        t.penup()
        t.goto(i*5, -i*5)  # shift for next square
        t.pendown()

# --- Main function to test your code ---
def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
  
    drawPolygon(t, 6)      # Example: hexagon
    fillCorner(t, 2)       # Example: top-right corner filled
    squaresInSquares(t, 5) # Example: 5 nested squares
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
