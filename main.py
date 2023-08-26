from pickle import NONE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('creditcard.csv')
legit = data[data['Class'] == 0]
fraud = data[data['Class'] == 1]
legit_sample = legit.sample(n=492)
new_data = pd.concat([legit_sample, fraud], axis=0)
# Separate input and output
X = new_data.drop(columns='Class', axis=1)
y = new_data['Class']
print(X)
print(y)
# Select random state to modify accuracy
rs = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=rs)
model = LogisticRegression()
model.fit(X_test, y_test)
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, y_test)
print(f"accuracy = {testing_data_accuracy * 100}%")
# Use sample data to test the model
input_data = (
    0, -1.3598071336738, -0.0727811733098497, 2.53634673796914, 1.37815522427443, -0.338320769942518, 0.462387777762292,
    0.239598554061257, 0.0986979012610507, 0.363786969611213, 0.0907941719789316, -0.551599533260813,
    -0.617800855762348,
    -0.991389847235408, -0.311169353699879, 1.46817697209427, -0.470400525259478, 0.207971241929242, 0.0257905801985591,
    0.403992960255733, 0.251412098239705, -0.018306777944153, 0.277837575558899, -0.110473910188767, 0.0669280749146731,
    0.128539358273528, -0.189114843888824, 0.133558376740387, -0.0210530534538215, 149.62,)
input_data_as_numpy_array = np.asanyarray(input_data)
input_data_reshape = input_data_as_numpy_array.reshape(1, -1)
prediction = model.predict(input_data_reshape)
if (prediction[0] == 0):
    print('The transaction is Legit')
else:
    print('The transaction is Fraud')
