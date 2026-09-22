import pandas as pd
import numpy as np
df = pd.read_csv("data/students.csv")
print(df)

print ("\nfirst 5 rows of the dataframe\n")
print(df.head())

print("\nInfornmation of dataset\n")
print(df.info())

print("\nStatistical summary of dataset\n")
print(df.describe())

df['Average'] = df[['Python', 'Maths', 'AIML']].mean(axis=1)
print("\nDataframe with Average column\n")
print(df[['Name', 'Average']])

highest_student = df.loc[df["Average"].idxmax()]

lowest_student = df.loc[df["Average"].idxmin()]

print("\nHighest Average:")
print(highest_student)

print("\nLowest Average:")
print(lowest_student)

def performance_category(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 60:
        return "Average"
    else:
        return "Poor"
df["Performance"] = df["Average"].apply(performance_category)
print("\nDataframe with Performance column:")
print(df[['Name', 'Average', 'Performance']])

print("\n Study Hours analysis\n")
print(df[['Name', 'Study_Hours','Average']].sort_values(by='Study_Hours',ascending=False))

print("Missing values in the dataset:\n")
print(df.isnull().sum())

df.to_csv("data/analyzed_students.csv", index=False)
print("\nAnalyzed dataset saved successfully!")