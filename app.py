import streamlit as st
import pandas as pd
from databricks import sql

# -----------------------------
# Databricks Connection
# -----------------------------
connection = sql.connect(
    server_hostname="dbc-c6ae1a55-0fea.cloud.databricks.com",
    http_path="/sql/1.0/warehouses/6f44597591149c56",
    access_token="dapib6fdbda421fec8fc77abc08eff6fdbaa"
)

cursor = connection.cursor()

cursor.execute("""
SELECT
    employee_id,
    employee_name,
    department,
    location,
    experience,
    project,
    salary
FROM demo.employee_master
""")

rows = cursor.fetchall()

columns = [
    "employee_id",
    "employee_name",
    "department",
    "location",
    "experience",
    "project",
    "salary"
]

df = pd.DataFrame(rows, columns=columns)

cursor.close()
connection.close()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Employee Directory")

st.title("🚀 Employee Directory")

employee = st.selectbox(
    "Select Employee ID",
    df["employee_id"]
)

if st.button("Search Employee"):

    emp = df[df["employee_id"] == employee].iloc[0]

    st.success("Employee Details")

    st.write(f"### 👤 Employee Information")

    st.write(f"**Employee ID:** {emp['employee_id']}")
    st.write(f"**Employee Name:** {emp['employee_name']}")
    st.write(f"**Department:** {emp['department']}")
    st.write(f"**Location:** {emp['location']}")
    st.write(f"**Experience:** {emp['experience']} Years")
    st.write(f"**Project:** {emp['project']}")
    st.write(f"**Salary:** ₹{emp['salary']}")
