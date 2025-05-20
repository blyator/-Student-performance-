import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the data
try:
    df = pd.read_csv('student-por.csv', sep=';')
    print("Dataset loaded!")
except FileNotFoundError:
    print("File not found.")
    exit()

# Display first few rows
print("\n First 5 rows:")
print(df.head())

# Checking for missing values
print("\n Data Info:")
print(df.info())

print("\n Missing Values:")
print(df.isnull().sum())


# the basic analysis
print("\n Descriptive Statistics:")
print(df.describe())

# grouping by school and calculating mean final grade 
print("\n Mean Final Grade by School:")
print(df.groupby('school')['G3'].mean())

# visualization
sns.set(style='whitegrid')

# Line chart – average by age
df.groupby('age')['G3'].mean().plot(marker='o')
plt.title("Average Final Grade (G3) by Age")
plt.xlabel("Age")
plt.ylabel("Average G3")
plt.grid(True)
plt.show()

# Bar chart – average per school
df.groupby('school')['G3'].mean().plot(kind='bar', color='skyblue')
plt.title("Average Final Grade (G3) by School")
plt.xlabel("School")
plt.ylabel("Average G3")
plt.show()

# Histogram – distribution of final grades
plt.hist(df['G3'], bins=10, color='lightcoral', edgecolor='black')
plt.title("Final Grade (G3) Distribution")
plt.xlabel("G3")
plt.ylabel("Frequency")
plt.show()

# Scatter plot of study time
sns.scatterplot(x='studytime', y='G3', data=df, hue='school', palette='viridis')
plt.title("Study Time vs. Final Grade (G3)")
plt.xlabel("Study Time")
plt.ylabel("G3")
plt.show()
