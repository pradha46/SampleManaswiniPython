import re

def validate_password(password):
    """
    Validates a password based on several criteria:
    - Minimum 8 characters, maximum 20 characters.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.
    - Contains at least one special character (e.g., !@#$%^&*).
    """
    if not (8 <= len(password) <= 20):
        return False, "Password must be between 8 and 20 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*]", password):
        return False, "Password must contain at least one special character (!@#$%^&*)."

    return True, "Password is valid."

# Testing the password validator
if __name__ == "__main__":
    test_passwords = [
        ("GoodPass1!", True),
        ("short", False),
        ("NOLOWERCASENUMBER!", False),
        ("nouppercasenumber!", False),
        ("NoNumbers!", False),
        ("NoSpecialChar123", False),
        ("TooLongPassword1234567890!", False),
        ("ValidPass!123", True),
    ]

    for password, expected_validity in test_passwords:
        is_valid, message = validate_password(password)
        print(f"Password: '{password}' -> Valid: {is_valid}, Message: {message}")
        assert is_valid == expected_validity, f"Test failed for password: '{password}'. Expected: {expected_validity}, Got: {is_valid}"

    print("\nAll tests passed!")
