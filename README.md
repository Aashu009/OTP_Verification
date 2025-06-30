# OTP Email Verification App using Python & Streamlit

This is a simple web application built using Python and Streamlit to perform email-based OTP (One-Time Password) verification. The app generates a 4-digit OTP, sends it to the user's email address, and verifies the entered OTP.

## Features

- OTP generation and email delivery using SMTP
- One-time verification logic using session state
- Secure handling of credentials using Streamlit secrets
- Simple and user-friendly interface
- Basic error and input handling

## Technologies Used

- Python 3.x
- Streamlit
- smtplib and email.mime (for email functionality)
- streamlit.secrets (for secure deployment credentials)
