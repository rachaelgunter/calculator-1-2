"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# while true loop
while True:
    input = input('Enter your equation > ')

#     if there is input
#         split words into 3 var is input
    input = input.split(" ")
    operator = input[0]
    num1 = input[1]
    num2 = input[2]
#             if first word is 'q'
    if operator == "q":
#                 quit
        break
#             if first word is add
    if operator == "+":
#                 arthimetic.add(input 2, input 3)
        result = add(float(num1), float(num2))
#             if first word is subtract
    if input[0] == "-":
#                 arithmetic.subtract(input2, input3)
        result = subtract(float(num1), float(num2))
#             if first word is multiply
    if input[0] == "*":
#                 arithmetic.multiply(input2, input3)
        result = multiply(float(num1), float(num2))
#             if first word is divide
    if input[0] == "/":
#                 arithmetic.divide(input2, input3)
        result = divide(float(num1), float(num2))
#             if first word is square
    if input[0] == "square":
#                 arithmetic.square(input2)
        result = square(float(num1))
#             if first word is cube
    if input[0] == "cube":
#                 arithmetic.cube(input2, input3)
        result = cube(float(num1))
#             if first word is power
    if input[0] == "pow":
#                 arithmetic.power(input2, input3)
        result = power(float(num1), float(num2))
#             if first word is mod
    if input[0] == "mod":
#                 arithmetic.mod(input2, input3)
       result = mod(input[1], input[3])
    if input[0] == "add_multi":
        result =  add_multi(input[1], input[2], input[3])
    if input[0] == "add_cubes":
        result = add_cubes(input[1], input[2])

    else:
        print("not enough information!")

    print(result)

