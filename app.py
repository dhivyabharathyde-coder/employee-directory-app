# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Employee Directory",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("🚀 Employee Directory")
st.markdown("### Search Employee Information")

employee = st.selectbox(
    "Select Employee ID",
    df["employee_id"]
)

if st.button("🔍 Search Employee"):

    emp = df[df["employee_id"] == employee].iloc[0]

    st.success("Employee Details Found")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.info("👤 Employee Profile")

        st.write(f"**Employee ID**")
        st.write(emp["employee_id"])

        st.write(f"**Employee Name**")
        st.write(emp["employee_name"])

        st.write(f"**Experience**")
        st.write(f"{emp['experience']} Years")

    with col2:
        st.info("🏢 Employment Details")

        st.write(f"**Department**")
        st.write(emp["department"])

        st.write(f"**Location**")
        st.write(emp["location"])

        st.write(f"**Project**")
        st.write(emp["project"])

        st.write(f"**Salary**")
        st.write(f"₹ {emp['salary']:,}")

    st.divider()

    st.success("✅ Employee information retrieved successfully from Databricks Delta Table.")
