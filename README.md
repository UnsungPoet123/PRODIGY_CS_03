# Password Complexity Checker

A simple yet effective Python tool that evaluates the strength of a password based on common security standards. It provides feedback to help users create stronger, more secure passwords.

---

## Features

- Checks password length (minimum 8 characters)
- Detects uppercase and lowercase letters
- Verifies presence of numbers
- Ensures inclusion of special characters
- Provides real-time feedback for improvement
- Classifies password strength (Weak, Moderate, Very Strong)

---

## Technologies Used

- Python 3
- Regular Expressions (`re` module)

---

## How It Works

The program evaluates a password based on five key criteria:

1. Length (≥ 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character

Each satisfied condition increases the password score.

---

## Strength Classification

| Score | Strength        |
|------|----------------|
| 5    | Very Strong |
| 3–4  | Moderate  |
| 0–2  | Weak |

---

## Example
Enter your password: Pass123

Password Strength: Moderate 

Suggestions to improve your password:
- Include at least one special character.
