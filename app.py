import streamlit as st
import pandas as pd
import pickle as pk


with open('insurance_model.pkl', 'rb') as f:
    model = pk.load(f)

try:
    st.title("🚫 Insurance Claim Checker 🚫")
    st.write("Check Your insurance claim  based on the info you give, answer the questions to check your claim ")

    st.warning("❗ Note that the predicted number might not be accurate ❗")

    with st.form(key = 'claim'):
        st.title("Insurance Claim")
        st.info("Fill the form below to check your claim")

        # ['age', 'gender', 'bmi', 'bloodpressure', 'diabetic', 'children','smoker', 'region']

        age = st.number_input("What is your age?", min_value = 10, max_value = 100)
        gender = st.selectbox("What is your gender?", options= ["","male", "female"])
        bmi = st.number_input("What is your BMI level?",min_value = 0.0, max_value = 60.0)
        bp = st.number_input("Blood Pressure?", min_value = 50, max_value=150)
        diabetic = st.selectbox("Are you Diabetic?", options = ["","Yes", "No"])
        children = st.number_input("How many children do you have (give birth to)?", min_value = 0, max_value = 10)
        smoker = st.selectbox("Do you smoke?", options = ["","Yes", "No"])
        region = st.selectbox("Which region are you located?", options = ['northeast', 'southeast', 'southwest', 'northwest'])
        btn = st.form_submit_button("Check Claim")

        if btn:
            st.success(f"Your insurance claim would be around: ${model.predict(pd.DataFrame({"age": [age], "gender": [gender], "bmi": [bmi], "bloodpressure": [bp], 
                    "diabetic": diabetic, "children": [children], "smoker": [smoker],
                    "region": [region]})).round(2)[0]}")

except st.exception as e:
    st.error(e)