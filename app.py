# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:01:05 2024

@author: megha
"""

import streamlit as st
import pickle

st.set_option('deprecation.showfileUploaderEncoding', False) 
model = pickle.load(open(r'C:\Users\megha\University of verona\Programming\Stroke prediction\model_pkl.pkl', 'rb'))

def main():
    st.sidebar.header("Stroke Risk Prediction")
    st.sidebar.text("This is a web app that predicts whether you will have a stroke or not.")
    
   
    age = st.slider("Enter the age between 0-100", 0, 100)
    hypertension = st.slider("Do you have hypertension? (0 for no, 1 for yes)", 0, 1)
    heart_disease = st.slider("Do you have heart disease? (0 for no, 1 for yes)", 0, 1)
    glucose_level = st.slider("Average glucose level", 150.0, 300.0)
    bmi = st.slider("Enter your BMI", 0.0, 70.0)

    inputs = [[age, hypertension, heart_disease, glucose_level, bmi]]

    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(int)
        if updated_res == 0:
            st.write("Not very probable you will have a stroke soon but still take good care of yourself regardless")
        else:
            st.write("It is probable you might have a stroke soon, therefore you should take better care of yourself")

if __name__ =='__main__':
    main()
