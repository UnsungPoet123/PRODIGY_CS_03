import re  # Used for pattern matching (regex)

def check_password_strength(password):
    """
    This function checks the strength of a password based on:
    - Length
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special characters
    """

    score = 0
    feedback = []

    # 1. Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # 2. Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # 3. Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # 4. Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # 5. Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    # Get password input from user
    password = input("Enter your password: ")

    # Check strength
    strength, feedback = check_password_strength(password)

    # Display results
    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("Great! Your password meets all security criteria.")