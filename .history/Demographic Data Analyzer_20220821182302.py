import pandas as pd


def dataAnalyzer():
    df = pd.read_csv(R"C:\Users\Amr\OneDrive\Documents\GitHub\FreeCodeCampProjects\data\adultdata.csv")
    race_count = df['race'].value_counts()
    mean_men_age = (df[df['sex'] == 'Male']['age'].mean()).round(1)
    people_with_bachelor = df[df['education'] == 'Bachelor'].count()
    print(people_with_bachelor)



dataAnalyzer()