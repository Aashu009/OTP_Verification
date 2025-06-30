# 1. import necessary libraries
import streamlit as st 

# smtp - simple mail transfer protocol library for sending emails
import smtplib
import random
import os 
# from dotenv import load_dotenv # pip install dotenv - for accessing the environment file 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# load_dotenv()
# 2. load environment variables from.env file

# EMAIL = os.getenv('EMAIL_USER')
# PASS = os.getenv('EMAIL_PASSWORD') # os.getenv('EMAIL_PASSWORD') is used to get the environment variable value from the .env file
EMAIL = st.secrets["EMAIL_USER"]
PASS = st.secrets["EMAIL_PASSWORD"]
# 3. start building the frontend

st.title('🔒 Email OTP Verification')

# intialize the session state 
if "otp" not in st.session_state:
    st.session_state.otp = None
    
# built the form 

with st.form('otp_form'):
    user_email = st.text_input('Enter your email address')
    send_clicked = st.form_submit_button('Send OTP')
    
    if send_clicked:
        if EMAIL is None or PASS is None:
            st.error("Email or Password is missing in .env file.")
        elif user_email == '':
            st.warning("Please enter valid email address.")
        
        else:
            st.session_state.otp = random.randint(1111, 9999) # generated otp is stored in this variable
            
            body =f"OTP for email verification is : {st.session_state.otp}" # this is the msg sent to the user email with the generated otp 
            
            msg = MIMEMultipart() # all parts in email are written like title subject body and attachments
            msg['From'] = EMAIL
            msg['To'] = user_email
            msg['Subject'] = 'Email OTP Verification'
            msg.attach(MIMEText(body, 'plain'))
            
            # we composed the email 
            
            # writing the code to send the email that we are composed
            try: 
                server = smtplib.SMTP("smtp.gmail.com", 587) # creating an SMTP server object - 587 is the port number to send the email 
                server.starttls() # secure the connection
                server.login(EMAIL, PASS) # login to the server with the provided email and password in .env file 
                server.send_message(msg) # sending the email
                
                server.quit() # closing the server connection
                st.success(f"OTP sent successfully to {user_email}")
            except:
                st.error("Authentication failed. Please check your email and password.")
# cross checking and verifying the otp entered by the user and sent by the server 

if st.session_state.otp:
    temp_otp = st.text_input('Enter the OTP sent to your email')
    if st.button('Verify OTP'):
        try:
            if int(temp_otp) == st.session_state.otp:
                st.success('OTP verified successfully!')
                st.session_state.otp = None # clearing the otp session state after successful verification - reseting the session otp to none so we cant reuse the same otp again and again 
                
            else:
                st.error('Invalid OTP. Please try again.')
                st.session_state.otp = None # clearing the otp session state if invalid otp is entered - reseting the session otp to none so we cant reuse the same otp again and again
        except ValueError:
            st.warning('Enter only 4 digits.')
            