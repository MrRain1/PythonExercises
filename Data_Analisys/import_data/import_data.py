import numpy as np
import pandas as pd
import seaborn as sns

data_file = pd.read_csv("./House_Price.csv", header= 0)

data_file.head()

data_file.describe()

sns.jointplot(x = "n_hot_rooms", y = "price", data = data_file)

sns.jointplot(x = "rainfall", y = "price", data = data_file)

data_file.head()

sns.countplot(x = "airport", data = data_file)
sns.countplot(x = "waterbody", data = data_file)
sns.countplot(x = "bus_ter", data = data_file)