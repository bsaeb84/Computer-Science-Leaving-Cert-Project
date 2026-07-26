import pandas as pd

#extracting the data

df = pd.read_csv("storke prediction dataset.zip")
#print(df)

#storing the age column in variable
age = df['age']

#storing the smoking_status column in a variable
smoking_status = df['smoking_status']

#storing ages with remainders
ages_with_remainders = []

# storing unknown smoking status
unknown_smoking_status = []

# isolated the value with a remainder
for value in age:
    if (value % 1) != 0:
        ages_with_remainders.append(value)
        
#print(ages_with_remainders)

#print()


# finding any missing values (N/A)
df.isna().sum()

print((df.isna().sum()/len(df))*100)  # finding the percentage of of missing values

# out of the 201 sample in the bmi column about 4 precent is missing, better to drop them
# identifying missing values (N/A) from bmi column
missing_data = df['bmi'].isnull()

# removing the record with the missing value
df_cleaned = df.drop(df.index[missing_data])


# resetting the index of the cleaned dataframe
df_cleaned = df_cleaned.reset_index(drop=True)

# dropping  columns = 'id', 'ever_married', 'Residence_type', 'work_type'
df_cleaned.drop(columns='id', inplace=True)
df_cleaned.drop(columns='ever_married', inplace=True)
df_cleaned.drop(columns='work_type', inplace=True)
df_cleaned.drop(columns='Residence_type', inplace=True)

print()

# checking age column for 'other' (stated in the dataset pn kaggle)

print(df_cleaned['gender'].value_counts())
print()

#there is one outlier with other, i will just drop the column
#getting the index
index_to_drop = df_cleaned[df_cleaned['gender'] == 'Other'].index

# droping the row
df_cleaned = df_cleaned.drop(index=index_to_drop)

print(df_cleaned['smoking_status'].value_counts())

print(df_cleaned)

# saving the cleaned data as a csv file
df_cleaned.to_csv("cleaned_strokePrediction_data.csv", index = False)





