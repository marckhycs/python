myList = [1,2,3,4,5,6,7,8,9]
cEven=0
cOdd=0

for i in myList:
    if i%2==0:
        cEven = cEven + 1
    else:
        cOdd = cOdd + 1
print(cEven)
print(cOdd)