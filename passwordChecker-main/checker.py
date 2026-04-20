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