# 3. Digit check
if re.search(r"\d", password):
    strength_score += 1
else:
    feedback.append("- Include at least one number.")

# 4. Special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength_score += 1
else:
    feedback.append("- Include at least one special character (e.g., @, #, $).")

# --- User Interface ---
print("--- Password Strength Evaluator ---")
user_pwd = input("Enter a password to test: ")
rating, tips = check_password_strength(user_pwd)

print(f"\nStrength Rating: {rating}")
if tips:
    print("Suggestions to improve:")
    for tip in tips:
        print(tip)
