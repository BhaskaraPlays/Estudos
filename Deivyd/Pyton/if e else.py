first_number = int(input('Type first number: '))
second_number = int(input('type second number: '))
third_number = int(input('type third number: '))
#print("the sum is: ", first_number + second_number)
a = first_number
b = second_number
c = third_number
# test expression
if a < b:
    # statement to be run
    print(b)
if a >= b:
    print(a)
else: print(b)

if a <= b :
    print ('a is less than or equal b')
elif a > b:
    print('a is greater than b')
else: 
    print('a is equal to b')

if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")
if a == 32 or b == 32:
    print(a + b)
if a == 68 and b == 32:
    print (a - b)
print("sumon all number is: ", a + b + c)
print("subtraction all numbers is: ", a - -b - c)
print("mutipli all number is: ", a * b * c)
print("division all number is: ", a / b / c)