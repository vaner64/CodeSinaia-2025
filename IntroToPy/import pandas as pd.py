import pandas as pd

df = pd.read_csv("IntroToPy/mountains_db.tsv", sep="\t", header=None, names=["Name", "Elevation", "Country", "Code"])
print(len(df["Code"].unique()), "unique countries.")

null_count = df["Elevation"].isnull().sum()
print(f"The Height column has {null_count} NULL values.")
print (df ["Elevation"].min())
print (df ["Elevation"].max())
print (df ["Elevation"].sum())
