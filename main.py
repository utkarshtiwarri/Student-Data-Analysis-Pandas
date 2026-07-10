import pandas as pd

df = pd.read_csv("Data/students.csv")

while True:
    print("\n" + "=" * 60)
    print("      STUDENT DATA ANALYSIS USING PANDAS")
    print("=" * 60)

    print("1. Display Dataset")
    print("2. Display Dataset Information")
    print("3. Display Statistics")
    print("4. Show Students with Marks > 80")
    print("5. Show CSE Students")
    print("6. Save Filtered Files")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nDataset\n")
        print(df)

    elif choice == "2":
        print("\nFirst 5 Rows")
        print(df.head())

        print("\nLast 5 Rows")
        print(df.tail())

        print("\nShape")
        print(df.shape)

        print("\nColumns")
        print(df.columns)

        print("\nData Types")
        print(df.dtypes)

    elif choice == "3":
        print("\nAverage Marks :", df["Marks"].mean())
        print("Median Marks  :", df["Marks"].median())
        print("Highest Marks :", df["Marks"].max())
        print("Lowest Marks  :", df["Marks"].min())
        print("Total Students:", df["Marks"].count())
        print("Average Age   :", df["Age"].mean())

    elif choice == "4":
        high = df[df["Marks"] > 80]
        print(high)

    elif choice == "5":
        cse = df[df["Department"] == "CSE"]
        print(cse)

    elif choice == "6":
        high = df[df["Marks"] > 80]
        cse = df[df["Department"] == "CSE"]

        high.to_csv("output/high_marks_students.csv", index=False)
        cse.to_csv("output/cse_students.csv", index=False)

        print("\nFiles saved successfully!")

    elif choice == "7":
        print("\nThank you for using Student Data Analysis Project.")
        break

    else:
        print("\nInvalid Choice!")