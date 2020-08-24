num =int(input("Enter a number: "))
test1 = num%3
test2 = num%5

if test1==0 and test2==0:
    print("FizzBuzz")
elif test1==0 or test2==0:
    if test1==0:
        print("Fizz")
    else:
        print("Buzz")
else:
    print(str(num))