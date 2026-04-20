import re

def check_password_strength(password):
    strength_score = 0
    feedback = []

    if len(password) >= 12:
        strength_score += 1
    else:
        feedback.append("- Password should be at least 12 characters long.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("- Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("- Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("- Include at least one special character (e.g., @, #, $).")

    common_patterns = ["123", "password", "qwerty", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        strength_score -= 1
        feedback.append("- Avoid common patterns like '123' or 'password'.")

    # Final Evaluation
    if strength_score <= 1:
        result = "VERY WEAK"
    elif strength_score == 2:
        result = "WEAK"
    elif strength_score == 3:
        result = "MEDIUM"
    else:
        result = "STRONG"

    return result, feedback


# --- User Interface ---
print("--- Password Strength Evaluator ---")
user_pwd = input("Enter a password to test: ")
rating, tips = check_password_strength(user_pwd)

print(f"\nStrength Rating: {rating}")
if tips:
    print("Suggestions to improve:")
    for tip in tips:
        print(tip)