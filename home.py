import streamlit as st
from ai_engine import cursor,db
from PIL import Image


st.title("🏠 Adesh Hospital ")
st.header("Welcome to *My Hospital*.")
st.subheader("Select a page to explore our services.")

# Load the image using PIL
image = Image.open("images/hospital.jpeg")

# Display the image in Streamlit
st.image(image)



st.subheader("Appointments....")
col0,col1,col2,col3,col4,col5=st.columns(6)

with col1:
        st.write("Appointment no.")
with col2:
        st.write("Patient Name")
with col3:
        st.write("Department")
with col4:
        st.write("Doctor")
with col5:
     st.write("Delete Appointment")

st.write("____________________________________")

id,pname,dept,doc,dlt=st.columns(5)
cursor.execute(f"select  * from appointments;")
all_app=cursor.fetchall()

for id,name,dname,doc,done in all_app:
    todo_id,app_id,pname,dept,doctor,dlt=st.columns(6)
    with todo_id:
        checked= st.checkbox(" Done ",key={id},value=bool(done))

        if checked != bool(done):
            cursor.execute(f"update appointments set appointment_done = {checked} where id= {id}")
            db.commit()
    with app_id:
        st.write(f"{id}")
    with pname:
        st.write(f"{name}")
    with dept:
         st.write(f"{dname}")
    with doctor:
         st.write(f"{doc}")    
    with dlt:
        x=st.button(" ⛔ Delete ", key=f"{id}")
        if x:
            cursor.execute(f"delete from appointments where id={id}")
            db.commit()
            st.snow()
            st.rerun()
    st.write("____________________________________")

    

st.warning("For book an Appointment....")
st.markdown("[Go to  Hospital Assistant Page](./Hospital_Assistant)")
