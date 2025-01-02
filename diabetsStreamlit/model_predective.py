import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

load_model=pickle.load(open('C:/Users/Chimou/Desktop/diabetsStreamlit/tained_model.sav', 'rb'))

# making a prediction system 

input_data=(6,148,72,35,0,33.6,0.627,50)
#to array format 
input_data_array=np.asarray(input_data)
#reshape data 
data_reshpe=input_data_array.reshape(1,-1)
# prediction 
prediction= load_model.predict(data_reshpe)
if (prediction == 0):
    print('the person is not diabetic')
else:
    print('the person is diabetic')
