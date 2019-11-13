#Program for Palindrome
first_string=input("enter string:  ")
reverse_string=list(reversed(first_string))
if list(first_string)==reverse_string:
    print("string is Palindrome")
else:
    print("string is not Palindrome")