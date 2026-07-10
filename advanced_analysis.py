import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/students.csv")

print("=" * 70)
print("ADVANCED DATA ANALYSIS")
print("=" * 70)

print("\nDataset Information")
df.info()

print("\nSummary Statistics")
print(df.describe())

print("\nTopper")
topper = df[df["Marks"] == df["Marks"].max()]
print(topper)

print("\nLowest Scorer")
lowest = df[df["Marks"] == df["Marks"].min()]
print(lowest)

print("\nDepartment-wise Student Count")
print(df["Department"].value_counts())

print("\nAverage Marks by Department")
print(df.groupby("Department")["Marks"].mean())

print("\nAverage Marks by Gender")
print(df.groupby("Gender")["Marks"].mean())

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/student_marks_chart.png")
plt.show()

plt.figure(figsize=(6,6))
df["Department"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Students by Department")
plt.ylabel("")
plt.tight_layout()
plt.savefig("output/department_pie_chart.png")
plt.show()

print("\nCharts saved successfully!")
