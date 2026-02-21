print ("Password Checker starting...")
password = input("Enter your password: ")
print ("You entered: " , password)

if len(password) < 8:
    print("Too short - needs at least 8 charcter")
else:
    print("Length is OK")

password = input("Enter a password to check: ")

has_number = any(char.isdigit() for char in password)

if has_number:
    print("Contains a number")
else:
    print("No number found")

password = input("Enter a password to check: ")

score = 0
if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password) :
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any (char.islower() for char in password):
    score+= 1

if any (char in "!@#$%^&*()" for char in password):
    score += 1

if score <=2:
    print("Weak password")
elif score <=4:
    print("medium password")
else:
    print("Strong password")    

