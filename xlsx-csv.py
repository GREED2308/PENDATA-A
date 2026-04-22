import pandas as pd
data = pd.read_excel("data.xlsx")
data.to_csv("data.csv", sep=",", index=False)

print("File berhasil diubah menjadi CSV")