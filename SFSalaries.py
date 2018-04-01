import pandas as pd

# Read Salaries.csv as a dataframe called sal.
sal = pd.read_csv('data/SmallSalaries.csv')

# Check the head of the DataFrame.
print(sal.head())

# What is the average BasePay ?
print(sal['BasePay'].mean())

# What is the highest amount of OvertimePay in the dataset ?
print(sal['OvertimePay'].max())

# What is the job title of PATRICIA JACKSON ?
print(sal[sal['EmployeeName'] == 'PATRICIA JACKSON'] ['JobTitle'])

# How much does PATRICIA JACKSON make (including benefits)?
print(sal[sal['EmployeeName'] == 'PATRICIA JACKSON']['TotalPayBenefits'])

# What is the name of highest paid person (including benefits)?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])

# What is the name of lowest paid person (including benefits)?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])

# What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print(sal.groupby('Year').mean()['BasePay'])

# How many unique job titles are there?
print(sal['JobTitle'].nunique()) #use .unique() to print unique job's title

# What are the top 5 most common jobs?
print(sal['JobTitle'].value_counts().head(5))

# How many Job Titles were represented by only one person in 2013?
# (e.g. Job Titles with only one occurence in 2013?)
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

# How many people have the word Chief in their job title? (This is pretty tricky)
def chief_string(title):
    if 'executive' in title.lower():
        return True
    else:
        return False
print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

 Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['BasePay', 'TotalPay']].corr()) #correlation
print(sal[['title_len', 'JobTitle']].corr()) # correlation
print(sal[['title_len', 'TotalPayBenefits']].corr()) # No correlation
