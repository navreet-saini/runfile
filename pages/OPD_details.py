import streamlit as st

st.set_page_config(page_title="OPD & Room Details", layout="centered")

st.title("🕒 OPD Timings & 🛏️ Room Information")
st.markdown("---")

st.header("🩺 OPD Timings")

st.markdown("""
| Department         | Doctor Name          | Days Available      | Time           |
|--------------------|----------------------|---------------------|----------------|
| General Medicine   | Dr. Raj. Sharma      | Mon–Sat             | 9:00 AM – 1:00 PM |
| Pediatrics         | Dr. Anil. Mehta      | Mon–Fri             | 10:00 AM – 2:00 PM |
| ENT                | Dr. Shivani. Kapoor  | Tue, Thu, Sat       | 11:00 AM – 1:00 PM |
| Orthopedics        | Dr. Vijay. Rao       | Mon–Sat             | 5:00 PM – 8:00 PM |
| Gynecology         | Dr. Neha. Bansal     | Mon–Fri             | 12:00 PM – 3:00 PM |
| Neurology          | Dr. Tilak. Verma     | Mon, Wed, Fri       | 4:00 PM – 6:00 PM |
| Cardiology         | Dr. Nitish Mehra     | Wed-Sat             | 11:00 AM - 1:00 PM |
""", unsafe_allow_html=True)

st.markdown("---")
st.header("🛏️ Room Categories & Facilities")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏨 General Ward")
    st.write("""
    - Shared beds (6–10 per room)  
    - Fan-cooled, basic amenities  
    - Affordable daily charges
            

    """)




    st.subheader("🛏️ Semi-Private Room")
    st.write("""
    - 2-3 beds per room  
    - A/C and attached bathroom  
    - Privacy curtains  
    """)

with col2:
    st.subheader("🛌 Private Room")
    st.write("""
    - Single patient room  
    - Fully air-conditioned  
    - TV, WiFi, and attached bathroom  
    - Sofa for attendant  
    """)

    st.subheader("👨‍⚕️ ICU / Critical Care")
    st.write("""
    - 24x7 monitoring  
    - Ventilator support  
    - Strict infection control  
    - Limited attendant access  
    """)

st.markdown("---")
st.info("📞 For OPD booking or room availability, call our helpdesk at +91-9876543210.")
