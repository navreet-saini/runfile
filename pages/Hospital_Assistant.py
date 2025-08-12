import streamlit as st
import google.generativeai as genai
from doctor_data import doctor_info
from ai_engine import cursor,db

genai.configure(api_key="AIzaSyAYE3L4uR9X7pwLWF-cOOCrv4lRj27J8Vg")  
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_reply(user_input):
    context = "You are a hospital assistant bot. Suggest departments and doctors and tell about diseases."
    for dept, data in doctor_info.items():
        context += f"\n\nDepartment: {dept}\nDescription: {data['description']}\nDoctors: {', '.join(data['doctors'])}"
    prompt = f"{context}\n\nUser: {user_input}\nAssistant:"
    response = model.generate_content(prompt)
    return response.text

def book_appointment(name, department, doctor):
    query = "INSERT INTO appointments (name, department, doctor) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, department, doctor))
    db.commit()

st.set_page_config(page_title="Healthcare Chatbot", layout="centered")
st.title("🤖 Healthcare Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_query = st.chat_input("Ask about doctors, departments, or appointments...")

if user_query:
    st.session_state.history.append(("You", user_query))
    reply = generate_reply(user_query)
    st.session_state.history.append(("Bot", reply))

for sender, message in st.session_state.history:
    with st.chat_message(sender.lower()):
        st.markdown(message)

# Optional: Book via chatbot
with st.expander("📅 Book Appointment"):
    name = st.text_input("Your Name")
    department = st.selectbox("Choose Department", ["Cardiology", "ENT", "Neurology","General Medicine","Pediatrics","Orthopedics","Gynecology"])
    doctor = st.text_input("Preferred Doctor")
    if st.button("Book Now"):
        if name and doctor:
            book_appointment(name, department, doctor)
            st.success("✅ Appointment Booked!")
        else:
            st.error("Please fill all fields.")




