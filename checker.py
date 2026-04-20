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

# --- User Interface ---
print("--- Password Strength Evaluator ---")
user_pwd = input("Enter a password to test: ")
rating, tips = check_password_strength(user_pwd)

print(f"\nStrength Rating: {rating}")
if tips:
    print("Suggestions to improve:")
    for tip in tips:
        print(tip)
