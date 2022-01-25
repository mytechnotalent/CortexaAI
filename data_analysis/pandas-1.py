# Copyright: (c) 2021, Kevin Thomas <kevin@mytechnotalent.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import pandas as pd
import matplotlib.pyplot as plt

# Importing Data
# --------------

# Import data into a Pandas DataFrame (axis=0 ROW & axis=1 COLUMN)
# car_sales = pd.read_csv('data/car-sales.csv')

# Print car_sales DataFrame
# print(car_sales)

# Export DataFrame
# car_sales.to_csv('data/exported-car-sales.csv', index=False)


# Describe Data
# -------------

# Attributes
# print(car_sales.dtypes)  # data types
# print(car_sales.columns)  # how many columns
# print(car_sales.index)  # how many rows

# Functions
# print(car_sales.describe())  # works on only numerical columns
# print(car_sales.info())  # index combined with dtypes and memory usage
# print(car_sales.mean())  # average of the numerical columns
# print(car_sales['Doors'].sum())  # sum of the doors numerical column
# print(len(car_sales))  # length of the DataFrame, number of rows


# Viewing & Selecting Data
# ------------------------

# Head of DF, top 5 rows, you can pass an argument to specify more
# print(car_sales.head())
# print(car_sales.head(10))

# Tail of DF, bottom 5 rows, you can pass an argument to specify more
# print(car_sales.tail())
# print(car_sales.tail(10))

# Index & Position, loc(refers to index) & .iloc(refers to position)
# print(car_sales.loc[0])  # 1st row
# print(car_sales.iloc[:3])  # DF up to index 2
# print(car_sales.loc[:3])  # DF up to position 3

# Single column
# print(car_sales['Make'])

# Single column w/ filter
# print(car_sales[car_sales['Make'] == 'Toyota'])
# print(car_sales[car_sales['Odometer (KM)'] > 100000])

# Compare two columns (ex: BMW, 1 car with 5 doors; Honda, 3 cars with 4 doors; etc...)
# print(pd.crosstab(car_sales['Make'], car_sales['Doors']))

# Groupby (Provide the mean values of the 'Make' for numerical data)
# print(car_sales.groupby(['Make']).mean())

# Plot data
# car_sales['Odometer (KM)'].plot()
# plt.show()
# car_sales['Odometer (KM)'].hist()
# plt.show()

# Convert object to numeric dtype
# print(car_sales['Price'].dtype)  # object
# car_sales['Price'] = car_sales['Price'].str.replace('[\$\,]', '', regex=True).astype(float)
# car_sales['Price'].plot()
# plt.show()


# Manipulating data
# -----------------

# Make lowercase a string column (to reassign, assign it back to itself or use .inplace)
# print(car_sales['Make'].str.lower())


# Real datasets have missing data
# -------------------------------

# Load missing dataset
# car_sales_missing = pd.read_csv('data/car-sales-missing-data.csv')

# Print data
# print(car_sales_missing)

# Fill 'Odometer' missing values with mean data (clean data)
# car_sales_missing['Odometer'].fillna(car_sales_missing['Odometer'].mean(), inplace=True)
# print(car_sales_missing)

# Drop missing data
# car_sales_missing.dropna(inplace=True)
# print(car_sales_missing)

# Better way to drop and clean data and save to new csv
# car_sales_missing_clean = car_sales_missing.dropna()
# car_sales_missing_clean.to_csv("data/car-sales-missing-clean.csv")


# Import data into a Pandas DataFrame (axis=0 ROW & axis=1 COLUMN)
car_sales_missing_clean = pd.read_csv('data/car-sales-missing-clean.csv')
# print(car_sales_missing_clean)


