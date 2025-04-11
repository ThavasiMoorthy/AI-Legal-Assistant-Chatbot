import streamlit as st
from twilio.rest import Client
# Twilio credentials (Replace with your actual credentials)
TWILIO_SID = "ACcb6f19ace56db44d5264360a4576e9ce"
TWILIO_AUTH_TOKEN = "87281ae02aca42b39969a3666aa36668"
TWILIO_PHONE = "+18283581231"
RECEIVER_PHONE  = "+918015766955"   
 # Replace with the police complaint number
# Replace with the court complaint number

def send_sms(complaint):
    try:    
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f"Complaint Received: {complaint}",
            from_=TWILIO_PHONE,
            to=RECEIVER_PHONE
        )
        return f"SMS sent successfully! Message SID: {message.sid}"
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("📩 Police Complaint SMS System")

# Input field for complaint
complaint_text = st.text_area("Describe your complaint in detail:")

# Send SMS when the button is clicked
if st.button("Submit Complaint & Send SMS"):
    if complaint_text:
        response = send_sms(complaint_text)
        st.success(response)
    else:
        st.error("Please enter a complaint before submitting.")

##ok