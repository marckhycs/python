i=0
co1 = []
print("Enter the first coordinates:")
while i<2:
    x1 = int(input())
    co1.append(x1)
    i+=1

j=0
co2 = []
print("Enter the second coordinates:")
while j<2:
    x2 = int(input())
    co2.append(x2)
    j+=1

slopey = co2[1]-co1[1]
slopex = co2[0]-co1[0]
slope = slopey/slopex

slopetest = slope*co1[0]
yint = co1[1]-slopetest

m = str(slope)
b = str(yint)

z1 = str(co1[0])
y1 = str(co1[1])
z2 = str(co2[0])
y2 = str(co2[1])


print("The linear equation of the given points is y = "+m+"x"+"+"+"("+b+")")