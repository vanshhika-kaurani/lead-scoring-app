import streamlit as st
import pandas as pd

st.title("Lead Scoring Dashboard")

# Example dummy data
df = pd.DataFrame({
    'Lead Source': ['Website', 'Referral', 'Social Media'],
    'Converted': [1, 0, 1]
})

st.dataframe(df)
