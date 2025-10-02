import streamlit as st
import pandas as pd

# Sample data
data = {
    'Department': ['ENT', 'PPT', 'TB'],
    'Patients Today': [12, 8, 5],
    'Avg Wait Time (min)': [30, 45, 25]
}
df = pd.DataFrame(data)

# Layout
st.title("📊 Hospital Daily Dashboard")
st.subheader("Department Overview")

st.dataframe(df)
st.bar_chart(df.set_index('Department')['Patients Today'])

wait_adjust = st.slider("Adjust wait time", -10, 10, 0)
df['Adjusted Wait Time'] = df['Avg Wait Time (min)'] + wait_adjust
st.write("Updated Wait Times:")
st.dataframe(df[['Department', 'Adjusted Wait Time']])