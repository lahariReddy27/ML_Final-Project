import numpy as np
import pandas as pd
from sklearn import *
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
df = pd.read_csv('house_data.csv')
df = df.replace({'No_Data':0}) #Replacing 'No_Data' with 0, to find out the mean
df["bedrooms"] = pd.to_numeric(df["bedrooms"])
df["sqft_living"] = pd.to_numeric(df["sqft_living"])
df["bathrooms"] = pd.to_numeric(df["bathrooms"])
df1 = df[["bedrooms","sqft_living","bathrooms"]]
meanbr = (round(df1.mean()[0])) #Rounded mean value of 'bedrooms' column
meansftl = (round(df1.mean()[1]))
meanbtr = (round(df1.mean()[2]))
df["bedrooms"] = df["bedrooms"].replace({0:meanbr})
df["bedrooms"] = pd.to_numeric(df["bedrooms"])
df["sqft_living"] = df["sqft_living"].replace({0:meansftl})
df["sqft_living"] = pd.to_numeric(df["sqft_living"])
df["bathrooms"] = df["bathrooms"].replace({0:meanbtr})
df["bathrooms"] = pd.to_numeric(df["bathrooms"])
data = df[["bedrooms","bathrooms","sqft_living","price"]].to_numpy()
#data = np.genfromtxt('house_data.csv', delimiter=',')
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:2000]
training_outputs = outputs[:2000]
testing_inputs = inputs[2000:]
testing_outputs = outputs[2000:]
classifier = GaussianNB()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
testSet = [[4,3,2950]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('GNB price prediction on the test set is:',predictions)
'''
testSet = [[3,1,1780]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('GNB price prediction on the second test set is:',predictions)
testSet = [[2,1,770]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('GNB price prediction on the third test set is:',predictions)
'''