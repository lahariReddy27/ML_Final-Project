import numpy as np
import pandas as pd
from sklearn import *
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error
df = pd.read_csv('regression_data.csv')
data = df[['bedrooms','sqft_living','condition','grade','price']].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = BaggingRegressor()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
#mse = mean_squared_error(testing_outputs, predictions)- 2100.00
#print ("The mean squared error of Logistic Regression on testing data is: " + str(mse))
testSet = [[3,1400,4,6]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('Bagging Prediction on the test set is:',predictions)
