import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    # Define password policy criteria
    min_length = 8
    min_uppercase = 1
    min_lowercase = 1
    min_digits = 1
    min_special_chars = 1
    common_passwords = ['password', '123456', 'qwerty']  # Example list of common passwords
    
    # Check length
    if len(password) < min_length:
        return "Weak - Password should be at least {} characters long.".format(min_length)
    
    # Check uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak - Password should contain at least one uppercase letter."
    
    # Check lowercase letters
    if not any(char.islower() for char in password):
        return "Weak - Password should contain at least one lowercase letter."
    
    # Check digits
    if not any(char.isdigit() for char in password):
        return "Weak - Password should contain at least one digit."
    
    # Check special characters
    if not any(char in "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~" for char in password):
        return "Weak - Password should contain at least one special character."
    
    # Check for common passwords
    if password.lower() in common_passwords:
        return "Weak - Password is too common. Choose a stronger one."
    
    # Password passed all checks
    return "Strong - Password meets complexity requirements."

# Main function for Streamlit UI
def main():
    st.title("Password Strength Checker")
    st.write("Enter your password and we'll evaluate its strength.")

    # Input field for password
    password = st.text_input("Password", type="password")

    # Check password strength if input is not empty
    if password:
        strength = check_password_strength(password)
        st.write("Strength:", strength)
        st.write("---")
        st.write("Password Tips:")
        st.write("- Aim for a minimum length of 8 characters.")
        st.write("- Include a mix of uppercase and lowercase letters.")
        st.write("- Add numbers and special characters for extra security.")
        st.write("- Avoid common words and phrases as passwords.")

if __name__ == "__main__":
    main()
