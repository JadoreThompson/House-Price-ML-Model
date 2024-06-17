import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from main import data
import numpy as np

scaler = StandardScaler()
forest = RandomForestRegressor()
data = pd.DataFrame(data)

data = data.replace([np.inf, -np.inf], 0)
x = data[['price']]
y = data.drop('price', axis=1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train_s = scaler.fit_transform(X_train)

regr = LinearRegression()
regr.fit(X_train, y_train)
lr_test_score = regr.score(X_test, y_test)

print("LR Score:", lr_test_score)

forest.fit(X_train, y_train)
rfr_score = regr.score(X_test, y_test)

print("RFR Score: ", rfr_score)

from sklearn.model_selection import GridSearchCV
forest = RandomForestRegressor()
param_grid = {
    'n_estimators': [3, 10, 20],
    'max_features': [2, 4, 6, 8]
}

grid_search = GridSearchCV(forest, param_grid, cv=5, scoring='neg_mean_squared_error',
                           return_train_score=True)
best_forest = grid_search.fit(x_train_s, y_train)
print(best_forest.score(x_train_s, y_train))





