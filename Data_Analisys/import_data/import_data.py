import numpy as np
import pandas as pd
import seaborn as sns

data_file = pd.read_csv("./House_Price.csv", header= 0)

print(data_file.head())

print(data_file.describe())

print(sns.jointplot(x = "n_hot_rooms", y = "price", data = data_file))

print(sns.jointplot(x = "rainfall", y = "price", data = data_file))

print(data_file.head())

print(sns.countplot(x = "airport", data = data_file))
print(sns.countplot(x = "waterbody", data = data_file))
print(sns.countplot(x = "bus_ter", data = data_file))