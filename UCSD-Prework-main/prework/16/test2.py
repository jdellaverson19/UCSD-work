import pandas as pd

# df = pd.read_csv(...)
df = pd.DataFrame({"Country": ["UK", "India", " US"]})

print(df.head())

print(df.columns)
print(df.dtypes)
only_ints = df.select_dtypes(include=["int"])

pd.get_dummies(df, columns=["Country"], drop_first=True, prefix="C")
# Drop_first is dummy encoding
counts = df["Country"].value_counts()
mask = df["Country"].isin(counts[counts < 5].index)
df["Country"][mask] = "Other"
testy = range(3)
df["Number_of_viol"] = testy
print(df.head())
df["Binar"] = 0
df.loc[df["Number_of_viol"] > 0, "Binar"] = 1
