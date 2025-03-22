# 🔐 Project 02: Password Strength Meter
# 📌 Objective
# Build a Password Strength Meter in Python that evaluates a user's password based on security rules. The program will:

# Analyze passwords based on length, character types, and patterns.
# Assign a strength score (Weak, Moderate, Strong).
# Provide feedback to improve weak passwords.
# Use control flow, type casting, strings, and functions.
# 🔹 Requirements
# 1. Password Strength Criteria
# A strong password should:
# ✅ Be at least 8 characters long
# ✅ Contain uppercase & lowercase letters
# ✅ Include at least one digit (0-9)
# ✅ Have one special character (!@#$%^&*)

# 2. Scoring System
# Weak (Score: 1-2) → Short, missing key elements
# Moderate (Score: 3-4) → Good but missing some security features
# Strong (Score: 5) → Meets all criteria
# 3. Feedback System
# If the password is weak, suggest improvements.
# If the password is strong, display a success message.

import re
import streamlit as st 

# Page Configuration
st.set_page_config(page_title="🔐 Password Strength Checker", page_icon="🔑", layout="centered")

# Custom CSS for Attractive UI
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            font-family: Arial, sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: white;
            color: black;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #FFD700;
        }
        .stButton button {
            background-color: #FFD700;
            color: black;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #FFA500;
            color: white;
        }
        .password-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 20px rgba(255, 255, 255, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a password to check its security level. 🚀</p>", unsafe_allow_html=True)

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Upper & Lower Case Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*<>]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*<>).**")

    # Display Strength
    st.markdown("<div class='password-card'>", unsafe_allow_html=True)

    if score == 4:
        st.success("🟢 **Strong Password** - Your password is secure! 🔥")
        st.progress(100)
    elif score == 3:
        st.info("🟡 **Moderate Password** - Consider improving security. 🔧")
        st.progress(70)
    else:
        st.error("🔴 **Weak Password** - Follow suggestions below to strengthen it. 🚨")
        st.progress(40)

    st.markdown("</div>", unsafe_allow_html=True)

    # Feedback
    if feedback:
        with st.expander("⚡ **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Password Input
password = st.text_input("Enter your password:", type="password", help="Make sure your password is strong. ✔")

# Check Strength Button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠ Please enter a password.")
