
import mysql.connector

# # Gemini API setup
# genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace this

# model = genai.GenerativeModel("gemini-2.5-flash")

# MySQL connection
db = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12793830",
    password="eunM8QMpPz",   
    database="sql12793830"
)
cursor = db.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS appointments (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(100),
#         department VARCHAR(100),
#         doctor VARCHAR(100)
#     )
# """)
db.commit()

# def generate_reply(user_input):
#     context = "You are a hospital assistant bot. Suggest departments and doctors."
#     for dept, data in doctor_info.items():
#         context += f"\n\nDepartment: {dept}\nDescription: {data['description']}\nDoctors: {', '.join(data['doctors'])}"
#     prompt = f"{context}\n\nUser: {user_input}\nAssistant:"
#     response = model.generate_content(prompt)
#     return response.text

# def book_appointment(name, department, doctor):
#     query = "INSERT INTO appointments (name, department, doctor) VALUES (%s, %s, %s)"
#     cursor.execute(query, (name, department, doctor))
#     db.commit()