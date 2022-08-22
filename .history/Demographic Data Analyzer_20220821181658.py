import pandas as pd

df = pd.read_csv(R"C:\Users\Amr\OneDrive\Documents\GitHub\FreeCodeCampProjects\data\adultdata.csv")
print(df['race'].value_counts())