
COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein", "qwerty", "abc123", "monkey", "1234567890"
]


def check_password(password: str):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["Password not allowed - change it"]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimum 8 characters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add atleast one number")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add one upper case letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add one lower case letter")

    if any(char in "!@#$%^&*()" for char in password):
        score += 1
    else:
        feedback.append("Add one special character")

    return score, feedback


def display_result(score, feedback):
    print(f"\nScore: {score}/5")
    if score <= 2:
        print("Too weak")
    elif score <= 4:
        print("Not strong enough")
    else:
        print("Strength strong")
    if feedback:
        print("\nHow to improve:")
        for tip in feedback:
            print(tip)


def main():
    print("=" * 40)
    print("      Password Strength Checker")
    print("=" * 40)
    while True:
        password = input("\nEnter a password (or 'quit' to exit): ")
        if password.lower() == "quit":
            print("Goodbye!")
            break
        score, feedback = check_password(password)
        display_result(score, feedback)


main()
