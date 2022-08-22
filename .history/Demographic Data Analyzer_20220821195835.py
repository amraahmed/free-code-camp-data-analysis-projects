import pandas as pd


def dataAnalyzer():
    df = pd.read_csv(R"C:\Users\Amr\OneDrive\Documents\GitHub\FreeCodeCampProjects\data\adultdata.csv")
    #Get the Count of races
    race_count = df['race'].value_counts()
    # Getting mean age of men
    mean_men_age = (df[df['sex'] == 'Male']['age'].mean()).round(1)
    # Percentage of Peopole with bachelor
    people_with_bachelor = (len(df[df['education'] == 'Bachelors'])/len(df)) * 100
    # Number of People with a high education
    people_with_high_education = len(df[df['education'].isin(['Bachelors','Masters','Doctorate'])])
    # Number of People with low education
    people_with_low_education = len(df[-df['education'].isin(['Bachelors','Masters','Doctorate'])])
    # percentage of people with advanced education and make more than 50K
    high_income_educated = len(people_with_high_education[people_with_high_education.salary == ">50k"])

    print(high_income_educated) 



dataAnalyzer()