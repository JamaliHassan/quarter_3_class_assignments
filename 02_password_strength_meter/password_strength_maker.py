import streamlit as st 
import random
import string
import re

blacklist = ["password", "123456", "password123", "admin", "qwerty"]

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))
def check_password_strength(password):
    score = 0
    message = []
    if password.lower() in blacklist:
        message.append("❌ This password is too common.")
        return 0 , message
    if len(password) >= 8:
        score += 2
    else: 
        message.append("❌ At least 8 characters long.")
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]', password):
        score += 1
    else:
        message.append("❌ Include both uppercase and lowercase letters.")
    if re.search(r'\d', password):
        score += 1
    else:
        message.append("❌ Add at least one number.")
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        message.append("❌ Include a special character (!@#$%^&*).")
     
    return score , message

st.title("🔐 Password Strength Checker & Generator")

password = st.text_input("Enter your password:")

if st.button('Check Strength'):
    score , feed_back = check_password_strength(password)

    if score >= 5:
        st.success("✅ Strong Password!")
    elif score >= 3:
        st.warning("⚠️ Moderate Password")
    else:
        st.error("❌ Weak Password")
    
    for msg in feed_back:
        st.write(msg)

if st.button("Generate Strong Password"):
    new_password = generate_password()
    st.write("Suggested Password:", f'<span style="color: green; font-weight: bold;">{new_password}</span>', unsafe_allow_html=True)

