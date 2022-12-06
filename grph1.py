import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

house_prices = pd.read_csv(r'regression_data.csv')
df = DataFrame(house_prices,columns=['id','date','price','bedrooms','bathrooms','sqft_living','condition','grade','yr_built'])

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




