import streamlit as st

st.markdown('## **Diabetes Prediction Application** 🩺')
st.markdown('------------------------------------------')

st.markdown('''### __This Application Predicts Your Diabetes Status Based on__:''')

left_cols, right_cols = st.columns(2)
left_cols.markdown('''- __Your Age__

- __Hypertension Status__
- __Heart-Disease Status 🫀__''')

right_cols.markdown('''
- __Smoking_History 🚬__
- __Body Mass Index ⚖️__
- __Blood Glucose Level 🩸__
- __HbA1c-level__''')

