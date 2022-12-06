import numpy as np
import pandas as pd
from sklearn import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('house_data.csv')
df = df.replace({'No_Data':0}) #Replacing 'No_Data' with 0, to find out the mean
df["bedrooms"] = pd.to_numeric(df["bedrooms"])
df["sqft_living"] = pd.to_numeric(df["sqft_living"])
df["condition"] = pd.to_numeric(df["condition"])
df["grade"] = pd.to_numeric(df["grade"]) 
df1 = df[["bedrooms","sqft_living","condition","grade"]]
meanbr = (round(df1.mean()[0])) #Rounded mean value of 'bedrooms' column
meansftl = (round(df1.mean()[1]))
meancndn = (round(df1.mean()[2]))
meangr = (round(df1.mean()[3]))
df["bedrooms"] = df["bedrooms"].replace({0:meanbr})
df["bedrooms"] = pd.to_numeric(df["bedrooms"])
df["sqft_living"] = df["sqft_living"].replace({0:meansftl})
df["sqft_living"] = pd.to_numeric(df["sqft_living"])
df["condition"] = df["condition"].replace({0:meancndn})
df["condition"] = pd.to_numeric(df["condition"])
df["grade"] = df["grade"].replace({0:meangr})
df["grade"] = pd.to_numeric(df["grade"])
data = df[["bedrooms","sqft_living","condition","grade","price"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:2000]
training_outputs = outputs[:2000]
testing_inputs = inputs[2000:]
testing_outputs = outputs[2000:]
classifier = DecisionTreeClassifier()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
testSet = [[4,1800,4,6]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('DT Prediction on the test set is:',predictions)
