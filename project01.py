#project 01.py, Yifan Qian
import turtle
import random

def drawRectangle(t,width,height,tilt,penColor,fillColor):
    t.color(penColor,fillColor)
    t.seth(tilt)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    
    t.forward(height)
    t.left(90)
    
    t.forward(width)
    t.left(90)
    
    t.forward(height)
    t.left(90)
    
    t.end_fill()

def drawTriangle(t,side,penColor,fillColor):
    t.color(penColor,fillColor)
    t.seth(0)
    t.begin_fill()
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.seth(0)
    t.end_fill()

def drawTree(t,height,color):
    drawRectangle(a,(height/6),height,0,"brown","brown")
    t.up()
    t.left(90)
    t.forward(height)
    t.seth(0)
    t.backward(height/2.5)
    t.down()
    drawTriangle(t,height,color,color)
    t.up()
    t.left(90)
    t.forward(height/3)
    t.seth(0)
    t.down()
    drawTriangle(t,height,color,color)
    t.up()
    t.left(90)
    t.forward(height/3)
    t.seth(0)
    t.down()
    drawTriangle(t,height,color,color)
    t.up()
    t.right(90)
    t.forward(height*1.68)
    t.seth(0)
    t.forward(height/3)
    
    
shadesOfGreen =["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"] 
def drawForest(t):
    for i in range(15):
        z=random.choice(shadesOfGreen)
        x=random.randrange(-400,400)
        y=random.randrange(30)
        t.up()
        t.seth(0)
        t.goto(x,y)
        t.down()
        drawTree(t,random.randrange(50,100),z)


def drawHut(t,x,y):
    t.up()
    t.goto(x,y)
    t.down()

    drawRectangle(t,8,40,0,"black","brown")
    t.up()
    t.forward(8)
    t.down()
    drawRectangle(t,8,40,0,"black","brown")
    t.up()
    t.forward(8)
    t.down()
    drawRectangle(t,8,40,0,"black","brown")
    t.up()
    t.forward(8)
    t.down()
    drawRectangle(t,8,40,0,"black","brown")
    t.up()
    t.forward(8)
    t.down()
    drawRectangle(t,8,40,0,"black","brown")
    t.up()
    t.forward(8)
    t.down()
    drawRectangle(t,8,40,0,"black","brown")
    
    t.up()
    t.forward(8)
    t.left(180)
    t.forward(24)
    t.right(90)
    t.forward(40)
    t.forward(24)
    t.right(90)
    t.right(25)

    for i in range(1,13):
        t.up()
        r=45
        t.seth(-25-i*10)
        t.forward(45)
        t.down()
        drawRectangle(t,5,45,65-i*10,"black","brown")
        t.up()
        t.goto(x+24,y+65)



def drawVillage(t):
    for i in range(5):
        x=random.randrange(-400,400)
        y=random.randrange(-100,-30)
        t.up()
        t.seth(0)
        t.goto(x,y)
        t.down()
        drawHut(t,x,y)

def drawScene(t):
    drawForest(t)

    drawVillage(t)

if __name__=="__main__":
    a=turtle.Turtle()
    
    a.shape("turtle")
    
    drawScene(a)
