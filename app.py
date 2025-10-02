import streamlit as st
import pandas as pd
from PIL import Image

# --- Logo ---
logo = Image.open("hospital_logo.png")  # Make sure this image is in your project folder
st.image(logo, width=120)

# --- Title ---
st.title("📊 Hospital Daily Dashboard")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["📁 Department Overview", "📋 Patient Data", "⚙️ Adjustments"])

# --- Tab 1: Department Overview ---
with tab1:
    st.subheader("Department Metrics")

    # Sample data
    data = {
        'Department': ['ENT', 'PPT', 'TB'],
        'Patients Today': [12, 8, 5],
        'Avg Wait Time (min)': [30, 45, 25]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)
    st.bar_chart(df.set_index('Department')['Patients Today'])

# --- Tab 2: Patient Data Upload & Filter ---
with tab2:
    st.subheader("Upload and Filter Patient Data")

    uploaded_file = st.file_uploader("Upload patient CSV", type="csv")
    if uploaded_file:
        patient_df = pd.read_csv(uploaded_file)

        dept_filter = st.selectbox("Filter by Department", patient_df['Department'].unique())
        filtered_df = patient_df[patient_df['Department'] == dept_filter]

        st.write("Filtered Patient Records:")
        st.dataframe(filtered_df)

# --- Tab 3: Adjust Wait Times ---
with tab3:
    st.subheader("Adjust Wait Time")

    wait_adjust = st.slider("Adjust wait time (minutes)", -10, 10, 0)
    df['Adjusted Wait Time'] = df['Avg Wait Time (min)'] + wait_adjust

    st.write("Updated Wait Times:")
    st.dataframe(df[['Department', 'Adjusted Wait Time']])