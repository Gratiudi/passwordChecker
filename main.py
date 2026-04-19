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
