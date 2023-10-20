import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app predicts the **Number of Sales!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Number_of_TV = st.sidebar.slider('Number of TV', 17.2, 296.4, 20.4)
    Number_of_Radio = st.sidebar.slider('Number of Radio', 10.8, 49.6, 20.4)
    Number_of_Newspaper = st.sidebar.slider('Number of Newspaper', 45.1, 114.0, 20.3)
    data = {'Number_of_TV': Number_of_TV,
            'Number_of_Radio': Number_of_Radio,
            'Number_of_Newspaper': Number_of_Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("advertising_model.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
