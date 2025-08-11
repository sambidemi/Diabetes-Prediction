import streamlit as st
import pandas as pd
st.sidebar.header('Predict Your Diabetes Status 🩺')

def userinput():
    global name
    name = str(st.sidebar.text_input('Enter Your Name: ')).strip()
    if name == '':
        st.sidebar.warning('Please Enter your name')
    gender = str(st.sidebar.radio('👨👩‍🦰 Gender: ', ['Male', 'Female']))

    age = int(st.sidebar.number_input('👴🏿 Age: ', 3, 90))
    if age > 60:
        st.sidebar.warning('Being Over 60 increases the tendency of being diabetic')

    hypertension = str(st.sidebar.radio(' 🔗 Are you Hypertensive? ', ['Yes', "No"]))

    heart_disease = str(st.sidebar.radio(' 🫀 Do you have heart disease?', ['Yes','No']))

    smoking_history = str(st.sidebar.selectbox(' 🚬 Smoking History:', ['never', 'No Info', 'current', 'former', 'ever', 'not current']))
    if smoking_history == 'current':
        st.sidebar.warning('Smokers are liable to die young')

    bmi = float(st.sidebar.slider('⚖️ Body Mass Index:', 10.0, 97.0))

    HbA1c_level = float(st.sidebar.slider('HbA1c-level: ', 3, 10))

    blood_glucose_level  = int(st.sidebar.number_input(' 🩸 Blood Glucose Level: ', 70, 300))

    user_data = {'gender':gender, 'age': age, 'hypertension': hypertension, 'heart_disease': heart_disease,
                'smoking_history': smoking_history, 'bmi':bmi, 'HbA1c_level':HbA1c_level, 'blood_glucose_level': blood_glucose_level}

    features = pd.DataFrame(user_data, index = [name])
    return features
df = userinput()

st.markdown('----------------------------------')
st.markdown('### __User Features__')
st.write(df)

#### perform encoding 
df['gender'] = df['gender'].map(lambda x: 1 if 'Male' else 0)

smoking_history_dict = {'No Info': 0,'never':1, 'not current':2, 'former':3, 'current':4, 'ever': 6 }
df['smoking_history'] = df['smoking_history'].map(smoking_history_dict)

df['hypertension'] = df['hypertension'].map(lambda x : 1 if 'Yes' else 0 )

df['heart_disease'] = df['heart_disease'].map(lambda x: 1 if 'Yes' else 0)

import joblib
if 'model' not in st.session_state:
    st.session_state.model = joblib.load('Diabetes_prediction_model.pkl')

btn = st.sidebar.button('Predict')
left_col , right_col = st.columns(2)
if btn: 
    prediction = st.session_state.model.predict(df)
    prediction_prob = st.session_state.model.predict_proba(df)
    
    prob_0 = round((prediction_prob[0,0]) * 100, 2)
    prob_1 = round((prediction_prob[0,1]) * 100,2)

    left_col.header('Diabetes Prediction')
    if prediction[0] == 1:
            left_col.warning(f'Dear {name}, You Have Diabetes.')
    else:
        left_col.success(f'Dear {name}, You Do Not Have Diabetes.')
    
    left_col.markdown(f'''- __The Probability of Having Diabetes is {prob_1}%__''')
    
    left_col.markdown(f'''- __The Probability of not Having Diabetes is {prob_0}%__''')

    right_col.image('img2.jpg')
st.markdown('--------------------------------')
