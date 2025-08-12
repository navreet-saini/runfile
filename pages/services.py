import streamlit as st

st.set_page_config(page_title="Our Services - CityCare Hospital", layout="wide")

st.title("🏥 Our Medical Services")
st.markdown("Welcome to **CityCare Hospital**, where your health is our top priority. We offer a comprehensive range of medical services led by experienced doctors and supported by state-of-the-art facilities.")

st.header("🌟 Key Departments & Services")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🫀 Cardiology")
    st.write("""
    - ECG, Echocardiography, TMT
    - Heart Attack & Stroke Management
    - Hypertension & Arrhythmia Treatments
    """)

    st.subheader("🧠 Neurology")
    st.write("""
    - Epilepsy, Stroke & Headache Clinic
    - Neurodiagnostic Services
    - Parkinson’s & Multiple Sclerosis Care
    """)

    st.subheader("🧒 Pediatrics")
    st.write("""
    - Child Vaccinations
    - Newborn Care
    - Growth & Nutrition Clinic
    """)

    st.subheader("🦴 Orthopedics")
    st.write("""
    - Fracture & Trauma Management
    - Joint Replacement Surgeries
    - Physiotherapy & Rehabilitation
    """)

with col2:
    st.subheader("🧬 General Medicine")
    st.write("""
    - Diabetes & Hypertension Care
    - Routine Check-ups
    - Infectious Disease Management
    """)

    st.subheader("👩‍⚕️ Gynecology & Obstetrics")
    st.write("""
    - Antenatal & Postnatal Care
    - Infertility Consultation
    - Laparoscopic Surgeries
    """)

    st.subheader("🧪 Diagnostic Lab & Imaging")
    st.write("""
    - Blood Tests, Urine Tests
    - X-Ray, Ultrasound, CT Scan
    - 24x7 Emergency Lab Support
    """)
    st.subheader("👂 ENT (Ear, Nose & Throat)")
    st.markdown("""
    - Ear, nose, and throat infection treatment  
    - Hearing tests and speech therapy  
    - Sinus, snoring, and allergy care  
    """)


st.subheader("🆘 24x7 Emergency & ICU")
st.write("""
    - Ambulance Services
    - Advanced ICU Facilities
    - Trauma & Critical Care
    """)

st.markdown("---")
st.info("📞 **Need Help?** Call our 24x7 helpline at **+91-9876543210** or visit our [Hospital Assistant](#) page to book an appointment.")
