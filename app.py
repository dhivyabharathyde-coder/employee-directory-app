import streamlit as st

st.set_page_config(page_title="Employee Directory")

st.title("🚀 Employee Directory")

# Read employee table
df = spark.sql("SELECT * FROM demo.employee_master").toPandas()

employee = st.selectbox(
    "Select Employee",
    df["employee_name"]
)

if st.button("Search Employee"):

    emp = df[df["employee_name"] == employee].iloc[0]

    st.success("Employee Details")

    st.write(f"**Employee ID:** {emp['employee_id']}")
    st.write(f"**Employee Name:** {emp['employee_name']}")
    st.write(f"**Department:** {emp['department']}")
    st.write(f"**Location:** {emp['location']}")
    st.write(f"**Experience:** {emp['experience']} Years")
    st.write(f"**Project:** {emp['project']}")
    st.write(f"**Salary:** ₹{emp['salary']}")
