
#get the value of perimeter
def getPerimeter(perimeter):
    p = int(input("Enter the perimeter: "))
    return p
p=0
finalPerimeter=getPerimeter(p)

#get the value of L

def getLength(length):
    l = length/2
    return l

l = getLength(finalPerimeter)


#get the value of w

def getWidth(width):
    w = (-1*(width))/(-2)
    return w

width = getWidth(l)

#getting the value of area

def getArea(length, w):
    a = ((length*w)-(w*w))
    return "The maximum area is: "+str(a)
    
getArea(l, width)

def rewritePerimeter(x,y):
    l = (y-(2*x))/2
    return "The length is "+str(l)
    

rewritePerimeter(width, finalPerimeter)

print(getArea(l, width))
print(rewritePerimeter(width, finalPerimeter))
print("The width is: "+str(width))