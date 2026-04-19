import re

def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        strength_score += 1
    else:
        feedback.append("- Password should be at least 12 characters long.")