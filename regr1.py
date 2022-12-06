import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

house_prices = pd.read_csv(r'regression_data.csv')
df = DataFrame(house_prices,columns=['id','date','price','bedrooms','bathrooms','sqft_living','condition','grade','yr_built'])
'''
#First Linearity Check
plt.scatter(df['bedrooms'], df['price'], color='red')
plt.title('No.of Bed Rooms Vs Price', fontsize=14)
plt.xlabel('Bed Rooms', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(True)
plt.show()
#Second Linearity Check
plt.scatter(df['sqft_living'], df['price'], color='green')
plt.title('Living_Square_Feet Vs Price', fontsize=14)
plt.xlabel('Living_Square_Feet', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(True)
plt.show()
'''
X = df[['bedrooms','sqft_living','condition','grade']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['price']
 
# with Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# prediction with sklearn
New_bedrooms = 3
New_sqft_living = 1400
New_condition = 4
New_grade = 6
print ('Predicted House Price with sklearn: ', regr.predict([[New_bedrooms ,New_sqft_living,New_condition,New_grade]]))
print ('Predicted House Price with linear regression:',regr.intercept_ + (regr.coef_[0]*New_bedrooms) + (regr.coef_[1]*New_sqft_living)+ (regr.coef_[2]*New_condition)+(regr.coef_[3]*New_grade))



