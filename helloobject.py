#!/usr/bin/env python

from lesobjets import Ligne, Point, Point3D

def MainObject():
    p1 = Point(1,2) # création d'une instance de point
    p1.x = 100
    p2 = Point() # création d'une instance de point
    p2.y = 500
    p3 = Point(5) # création d'une instance de point

    pl1 = Ligne(p1,p2)
    pl1.display()

    p1.move(100,200) # nouvelles coord pour newX et newY
    p1.display()
    pl1.display()

    p2.display()
    p3.display()

    tabDePoint = []

    tabDePoint.append(Point(1,2))
    tabDePoint.append(Point(3,4))
    tabDePoint.append(Point(5,6))
    tabDePoint.append(Point3D(15,25,35))


    for pt in tabDePoint:
        pt.display()
        pt.x = 654
    
    for pt in tabDePoint:
        pt.display()


if __name__ == "__main__":
    MainObject()