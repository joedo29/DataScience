import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

USAhousing = pd.read_csv('USA_Housing.csv')

# A few things we should run to understand the dataset
# USAhousing.head()
# USAhousing.info()
# USAhousing.describe()
# USAhousing.columns
# sns.pairplot(USAhousing)
# sns.distplot(USAhousing['Price'])
# sns.heatmap(USAhousing.corr())

# TRAINING A LINEAR REGRESSION MODEL
from sklearn.model_selection import train_test_split
# Now let's split the data into a training set and a testing set.
# We will train out model on the training set and
# then use the test set to evaluate the model.
# X = training set, y = testing set
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']
# test_size = percentage of your dataset that you want to allocate for test size
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# CREATING AND TRAINING THE MODEL
from sklearn.linear_model import LinearRegression
lm = LinearRegression() #create a LinearRegression object
lm.fit(X_train, y_train)

# MODEL EVALUATION
# Let's evaluate the model by checking out it's coefficients and how we can interpret them
print(lm.intercept_) # -2640159.79685

# build a dataframe from coefficients
coeff = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print(coeff)

# PREDICTION FROM OUR TEST SET
predictions = lm.predict(X_test)
# scatterplot of the real test values versus the predicted values.
plt.scatter(y_test,predictions) # straigt line = perfect
# Plot a histogram of the residuals and make sure it looks normally distributed.
sns.distplot((y_test - predictions),bins=50);

# REGRESSION EVALUATION METRICS
from sklearn import metrics
# 1. Mean Absolute Error (MAE) is the mean of the absolute value of the errors
# 2. Mean Squared Error (MSE) is the mean of the squared errors
# 3. Root Mean Squared Error (RMSE) is the square root of the mean of the squared errors
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
# MAE is the easiest to understand, because it's the average error.
# MSE is more popular than MAE, because MSE "punishes" larger errors, which tends to be useful in the real world.
# RMSE is even more popular than MSE, because RMSE is interpretable in the "y" units.

# CREATE AND INTERPRET THE COEFFECIENTS
coeffecients = pd.DataFrame(lm.coef_, X.columns)
coeffecients.columns = ['Coeffecient']
print(coeffecients)
# Interpreting the coefficients:
#                                  Coeffecient
# Avg. Area Income                  21.528276
# Avg. Area House Age           164883.282027
# Avg. Area Number of Rooms     122368.678027
# Avg. Area Number of Bedrooms    2233.801864
# Area Population                   15.150420

# 1. Holding all other features fixed, a 1 unit increase in
# Avg. Area Income is associated with an increase of 21.528276 total dollars
# 2. Holding all other features fixed, a 1 unit increase in
# Avg. Area House Age is associated with an increase of 164883.282027 total dollars
# 3. Holding all other features fixed, a 1 unit increase in
# Avg. Area Number of Rooms is associated with an increase of 122368.678027 total dollars
# 4. Holding all other features fixed, a 1 unit increase in
# Avg. Area Number of Bedrooms is associated with an increase of 2233.801864 total dollars
# 5. Holding all other features fixed, a 1 unit increase in
# Area Population is associated with an increase of 15.150420 total dollars

plt.show()
