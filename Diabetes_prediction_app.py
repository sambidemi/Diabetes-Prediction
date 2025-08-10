import streamlit as st 
import pandas as pd

userfile = 'users.csv'
user_df = pd.read_csv(userfile)

def save_user(username, password): 
    new_row = pd.DataFrame([[username,password]], columns = ['username', 'password'])
    updated_user_df = pd.concat([user_df,new_row], ignore_index = True)
    updated_user_df.to_csv(userfile,index = False)
    st.session_state.dataframe = updated_user_df

if 'dataframe' not in st.session_state:
    st.session_state.dataframe = pd.read_csv(userfile)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

def login_form():
    st.markdown('## __Login__')
    left, right = st.columns(2)
    username = left.text_input('Username').strip()
    password = left.text_input('Password', type = 'password').strip()
    right.image('diabetes_img.jpg')
    if left.button('Login'):
        if username in st.session_state.dataframe['username'].values and password in st.session_state.dataframe.loc[st.session_state.dataframe['username']== username,'password'].values:
            st.session_state.logged_in = True
            st.session_state.username = username
            left.success('Login Successful')
            st.rerun()
       
        else:
            st.error('Invalid Username or Password')

def register_form():
    st.markdown('## __Create Account__')
    left, right = st.columns(2)
    right.image('diabetes_img.jpg')
    new_username = left.text_input('New Username')
    new_password = left.text_input('New Password', type = 'password')
    confirm_password = left.text_input('Confirm Pasword', type = 'password')
    
    if left.button('Register'):
        if new_username in st.session_state.dataframe['username'].values:
            left.error('Username already exists.')
        elif new_username == '' or new_password == '':
            left.error('Please Fill all Fields.')
        else:
            if new_password != confirm_password:
                left.error('Passwords do not match.')
            else:
                save_user(username = new_username, password = new_password)
                left.success('Account Created! Please log in.')

if not st.session_state.logged_in:
    st.markdown('# __Diabetes Prediction Application__')
    left_col,right_col = st.columns(2)
    choice = left_col.radio('Choose an Option', ['Login','Create Account'])
    if choice == 'Login':
        login_form()
    else:
        register_form()

    st.stop()

st.sidebar.markdown(f'__Welcome, {st.session_state.username}__')

### Creating Pages and Navigation
main_page = st.Page('home.py', title= 'Home', icon = ':material/home:')
predict = st.Page('predict.py', title ='Predict', icon = ':material/stethoscope:')

pg = st.navigation([main_page, predict])

pg.run()

if st.sidebar.button('Logout'):
    st.session_state.logged_in = False
    st.session_state.username = ''
    st.rerun()

