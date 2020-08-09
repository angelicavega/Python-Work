import math

def distance(x1,x2,y1,y2):
    d = math.sqrt((x2-x1))**2+(y2-y1)**2
    return d
def area(r):
        a = 2*math.pi*(r**2)
        return a
def circle_area(x1,x2,y1,y2):
    d = distance(x1,x2,y1,y2)
    circlearea = area(d)
    return circlearea

x1 = 3.0
x2 = 5.0
y1 = 4.0
y2 = 8.0

areavalue = circle_area(x1,x2,y1,y2)
