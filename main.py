num = int(input("Enter a number: "))
binary=[]

while num>0:
    if num%2>0:
        binary.insert(len(binary)+1, 1)
    else:
        binary.insert(len(binary)+1, 0)
    num = num//2

newline = ''

for i in binary:
    newline = newline+str(i)
print(newline[::-1])



