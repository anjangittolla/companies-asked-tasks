input_string=input("Enter a string:  ")
second_string=input("Enter second string:  ")
d=int(input("Enter the value to rotate:  "))
left_rotate=input_string[d:]+input_string[:d]
right_string=input_string[len(input_string)-d:]+input_string[:len(input_string)-d]
print(left_rotate)
print(right_string)
def rotational():
    if second_string==left_rotate or second_string==right_string:
        return True
    else:
        return False
print(rotational())