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
    people_with_high_education = (df[df['education'].isin(['Bachelors','Masters','Doctorate'])])
    no_people_with_high_education = len(people_with_high_education)
    # Number of People with low education
    people_with_low_education = (df[-df['education'].isin(['Bachelors','Masters','Doctorate'])])
    no_people_with_low_education = len(people_with_low_education)
    # percentage of people with advanced education and make more than 50K
    high_income_educated = (len(people_with_high_education[people_with_high_education['salary'] == '>50K'])/no_people_with_high_education)*100
    # percentage of people without advanced education make more than 50K
    high_income_not_educated = (len(people_with_low_education[people_with_low_education['salary'] == '>50K'])/no_people_with_low_education)*100
    #  minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()
    # percentage of the people who work the minimum number of hours per week have a salary of more than 50K
    min_workers = df[df['hours-per-week']== min_work_hours]
    min_hours_high_income = ((len(min_workers[min_workers['salary'] == '>50K']))/len(min_workers))*100
    # What country has the highest percentage of people that earn >50K and what is that percentage
    richest_country = df[df['salary'] == '>50K']
    rich = (richest_country.value_counts())



    print(rich) 




dataAnalyzer()