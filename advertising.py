import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app predicts the **Number of Sales!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('Number of TV', 17.2, 296.4, 20.4)
    Radio = st.sidebar.slider('Number of Radio', 10.8, 49.6, 20.4)
    Newspaper = st.sidebar.slider('Number of Newspaper', 45.1, 114.0, 20.3)
    data = {'TV': Number_of_TV,
            'Radio': Number_of_Radio,
            'Newspaper': Number_of_Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Advertising-model-LR.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Sales Prediction')
st.write(prediction)
