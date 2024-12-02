# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
titanic_data = pd.read_csv('M_YOUNAS_CS351_AI_Lab04\train.csv')
print(titanic_data.head())  # Display first few rows of the dataset

# Check the data types and for any missing values
print(titanic_data.info())
print(titanic_data.isnull().sum())

# Visualize distribution of key features
sns.countplot(x='Pclass', hue='Survived', data=titanic_data)
plt.title('Passenger Class vs Survival')
plt.show()

sns.histplot(titanic_data['Age'].dropna(), kde=True, bins=30)
plt.title('Age Distribution')
plt.show()

sns.countplot(x='Sex', hue='Survived', data=titanic_data)
plt.title('Gender vs Survival')
plt.show()
