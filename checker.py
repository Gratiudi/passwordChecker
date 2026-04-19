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
