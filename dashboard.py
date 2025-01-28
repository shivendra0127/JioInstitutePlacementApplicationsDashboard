import pandas as pd
import streamlit as st
from streamlit_apexjs import st_apexcharts

# Load data
data = pd.read_excel('Processed_Student_Applications.xlsx')
company_counts = data.iloc[:, 2:].sum().sort_values(ascending=False)
# Title
st.set_page_config(page_title="Jio Institute")
st.image("Jio_Institue_Logo.png")
st.title('Placement Applications Dashboard')

# Filter by student (Move to top of the dashboard)
st.header('Student-specific Stats')
student_name = st.selectbox('Select a student', data['Student_Name'].unique())
student_data = data[data['Student_Name'] == student_name].iloc[:, 2:]
applied_companies = student_data.loc[:, (student_data == 1).any()].columns.tolist()

# Display student-specific stats
st.subheader(f"Companies applied by {student_name}")
st.write(f"Count of companies applied to: **{len(applied_companies)}**")
if applied_companies:
    st.write(", ".join(applied_companies))
else:
    st.write(f"{student_name} has not applied to any companies.")


# Top 5 Companies Donut Chart
st.header("Top 5 Companies with Most Applications")
top_companies = company_counts.head(5)

options_donut = {
    "chart": {},
    "labels": top_companies.index.tolist(),
    "legend": {
        "show": True,
        "position": "bottom",
    },
}

st_apexcharts(
    options=options_donut,
    series=top_companies.tolist(),
    types="donut",  # Corrected argument for chart type
    width="200%",
    title="Top 5 Companies with Most Applications",
)
# Company-wise Applications Bar Chart
st.header("Company-wise Applications")
company_counts = data.iloc[:, 2:].sum().sort_values(ascending=False)

options_bar = {
    "chart": {
        "toolbar": {"show": False},
    },
    "xaxis": {
        "categories": company_counts.index.tolist(),
        "title": {"text": "Company Names"},
    },
    "yaxis": {"title": {"text": "Number of Applications"}},
    "legend": {"show": False},
}

st_apexcharts(
    options=options_bar,
    series=[{"name": "Applications", "data": company_counts.tolist()}],
    types="bar",  # Corrected argument for chart type
    width="220%",
    title="Number of Applications per Company",
)

# Program-wise Distribution Pie Chart
st.header("Program-wise students Distribution")
program_counts = data['Program'].value_counts()

options_pie = {
    "chart": {},
    "labels": program_counts.index.tolist(),
    "legend": {
        "show": True,
        "position": "bottom",
    },
}

st_apexcharts(
    options=options_pie,
    series=program_counts.tolist(),
    types="pie",  # Corrected argument for chart type
    width="100%",
    title="Program-wise Distribution",
)