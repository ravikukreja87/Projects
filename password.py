
import random
import string

def generate_password(length=12):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    # Combine all characters
    all_chars = lower + upper + digits
    
    # Ensure the password has at least one of each for better security
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    
    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 3)
    
    # Shuffle the list to ensure the first three aren't predictable
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

# Generate and print a 16-character password
print(f"Your new password is: {generate_password(16)}")