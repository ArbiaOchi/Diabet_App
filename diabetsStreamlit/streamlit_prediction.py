import numpy as np 
import pickle 
import streamlit as st

#load model 
load_model=pickle.load(open('C:/Users/Chimou/Desktop/diabetsStreamlit/tained_model.sav', 'rb'))

# diabetes functions 
def diabetes_predictions(input_data):

    input_data_asarray=np.asarray(input_data)
    input_data_reshape=input_data_asarray.reshape(1,-1)

    prediction=load_model.predict(input_data_reshape)
    if (prediction==0):
        return 'the person is not diabetes'
    else:
        return 'the person is diabetes'


def main():

    # title 
    st.title('Diabetes Prediction')
    #input data from user 
    Pregnancies =st.text_input('Number of Pregnancies')
    Glucose =st.text_input('Glucose level')
    BloodPressure =st.text_input('BloodPressure value')
    SkinThickness =st.text_input('SkinThickness value')
    Insulin =st.text_input('Insulin level')
    BMI	=st.text_input('BMI value')
    DiabetesPedigreeFunction =st.text_input('DiabetesPedigreeFunction value')
    Age	=st.text_input('Age of the person ' )

    # button for prediction 
    diagnosis=''

    if st.button('Diabetes test Result'):
        diagnosis=diabetes_predictions([Pregnancies, Glucose, BloodPressure, SkinThickness,	Insulin, BMI, DiabetesPedigreeFunction,	Age	])

    st.success(diagnosis)

if __name__ =='__main__':
    main()