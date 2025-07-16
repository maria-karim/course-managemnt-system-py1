import streamlit as st
from course_management_system import Student, Teacher, Admin

# Dummy Data
students = [
    Student("Sara"),
    Student("Noor"),
    Student("Ali"),
    Student("Zain")
]

teachers = [
    Teacher("Mr. Ahmed", ["ML", "Cyber Security"]),
    Teacher("Ms. Fatima", ["Web Design", "Data Analysis"])
]

st.title("🎓 Course Management Dashboard")

role = st.selectbox("Login as:", ["Student", "Teacher", "Admin"])

if role == "Student":
    st.subheader("👩‍🎓 Student Portal")
    selected_name = st.selectbox("Select your name:", [s.name for s in students])
    selected_student = next((s for s in students if s.name == selected_name), None)

    courses = ["Data Analysis", "Web Design", "Cyber Security", "Digital Marketing", "ML"]
    chosen_course = st.selectbox("Select a course to enroll:", courses)

    if st.button("Enroll in course"):
        selected_student.select_course(chosen_course)
        st.success(f"{chosen_course} enrolled successfully!")

    st.write("📘 Your Courses:", selected_student.get_selected_courses())
    st.write("💰 Fee Status:", selected_student.get_fee_status())

elif role == "Teacher":
    st.subheader("👨‍🏫 Teacher Portal")
    selected_name = st.selectbox("Select your name:", [t.name for t in teachers])
    selected_teacher = next((t for t in teachers if t.name == selected_name), None)

    st.write("📚 Subjects Assigned:", selected_teacher.subjects)
    st.warning("Note: Fee details are not accessible to teachers.")

elif role == "Admin":
    st.subheader("🧑‍💼 Admin Portal")
    name = st.text_input("Enter admin name", "Principal")
    admin = Admin(name)

    st.write("📋 All Students Record:")
    for s in students:
        st.markdown(f"- **{s.name}** → Courses: {s.get_selected_courses()} | Fee: {s.get_fee_status()}")

    st.write("👩‍🏫 All Teachers Record:")
    for t in teachers:
        st.markdown(f"- **{t.name}** → Subjects: {t.subjects}")
   

st.title("🎓 Course Management System")

st.write("Welcome, this is your working app!")
