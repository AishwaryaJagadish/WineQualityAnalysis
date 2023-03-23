# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 08:17:38 2023

@author: Aishwarya
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('F:/Projects 2022/PYTHON/Wine Quality Analysis/wine_quality_model.sav', 'rb'))


# creating a function for Prediction

def winequality_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'Good Quality Wine'
    else:
      return 'Bad Quality Wine'
  
    
  
def main():
    
    
    # giving a title
    st.title('Wine Quality Analysis')
    
    
    # getting the input data from the user
    
    
    fixedacidity = st.text_input('Fixed Acidity')
    volatileacidity = st.text_input('Volatile Acidity')
    citricacid = st.text_input('Citric Acid')
    residualsugar= st.text_input('Residual Sugar')
    chlorides = st.text_input('Chlorides')
    freesulfurdioxide = st.text_input('Free Sulfur Dioxide')
    totalsulfurdioxide = st.text_input('Total Sulfur Dioxide')
    density = st.text_input('Density')
    pH = st.text_input('pH')
    sulphates = st.text_input('Sulphates')
    alcohol = st.text_input('Alcohol')
    
    
    # code for Prediction
    winequality = ''
    
    # creating a button for Prediction
    
    if st.button('Wine Quality Test Result'):
        winequality = winequality_prediction([fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol])
        
        
    st.success(winequality)
    
    
    
    
    
if __name__ == '__main__':
    main()