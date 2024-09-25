intgr=str(input("Enter an integer: "))
is_palindrome = ''.join(intgr.lower().split()) 
if is_palindrome == is_palindrome[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")