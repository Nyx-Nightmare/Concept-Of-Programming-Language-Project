from graphics import *


def main():
    window = GraphWin("My Window", 500,500)
    window.setBackground(color_rgb(0,0,0))

    
    pt = Point(250,250)
    cir = Circle(pt, 50)
    cir.setFill(color_rgb(255,0,0))
    cir.draw(window)
    
    GLpoint1 = Point(0,400)
    GLpoint2 = Point(100,500)
    greenLand = Rectangle(GLpoint1,GLpoint2)
    greenLand.setFill(color_rgb(0,255,0))
    greenLand.draw(window)

    Lpoint1 = Point(100,420)
    Lpoint2 = Point(500,500)
    sea = Rectangle(Lpoint1,Lpoint2)
    sea.setFill('Cyan')
    sea.draw(window)
    
    window.getMouse()
    window.close()

main()