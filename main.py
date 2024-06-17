import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Data Formatting
pd.set_option('display.max_columns', 30)

df = pd.read_csv("Housing.csv")
df = pd.DataFrame(df)

df['price'] = pd.to_numeric(df['price'])
df = df.dropna()
df['airconditioning'] = df['airconditioning'].map({'yes': 1, 'no': 0})
df['mainroad'] = df['mainroad'].map({'yes': 1, 'no': 0})
df['guestroom'] = df['guestroom'].map({'yes': 1, 'no': 0})
df['basement'] = df['basement'].map({'yes': 1, 'no': 0})
df['hotwaterheating'] = df['hotwaterheating'].map({'yes': 1, 'no': 0})
df['prefarea'] = df['prefarea'].map({'yes': 1, 'no': 0})
df['furnishingstatus'] = df['furnishingstatus'].map({'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0})

fdf = df


# Plotting
def plot_chart(data):
    correlation_matrix = data.corr()
    plt.figure(figsize=(15, 8))
    sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True)
    plt.show()


# Feautre engineering

df['price_bathrooms_ratio'] = round(df['price'] / df['bathrooms'], 2)
df['price_bedrooms_ratio'] = round(df['price'] / df['bedrooms'], 2)
df['price_stories_ratio'] = round(df['price'] / df['stories'], 2)
df['total_rooms'] = df['bedrooms'] + df['bathrooms'] + df['guestroom'] + df['basement']
df['area_parking_ratio'] = round(df['area'] / df['parking'], 2)
columns_to_drop = ['hotwaterheating']
df = df.drop(columns_to_drop, axis=1)
data = df
# plot_chart(data)
#
# print(df)
