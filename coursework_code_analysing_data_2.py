import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import statsmodels.api as sm

data = pd.read_csv("cleaned_strokePrediction_data.csv")


# Defining non-numeric values
non_numeric_cols = ['gender','hypertension', 'heart_disease', 'smoking_status', 'stroke']

# creating a dictionary to store statistical values for the numeric columns
stats_dictionary = {}

# The loop goes through each individual columns and finds the numeric ones and stores them as status_data
for col in data.columns:
    if col not in non_numeric_cols:
        stats_data = data[col]
        
        stats_dictionary[col] = {
            'Mean': stats_data.mean(),
            'Median': stats_data.median(),
            'Mode': stats_data.mode().iloc[0] if not stats_data.mode().empty else np.nan,
            'Range': stats_data.max() - stats_data.min()
            }
        
stats_df = pd.DataFrame(stats_dictionary).transpose()
print("Statistical analysis on numeric columns in the dataset")
print(stats_df)


# Visualization #

# deciding on the plot colour
plot_colour = ['#531975', '#b8165c']

# counting the number of females and males
gender_count = data['gender'].value_counts()

# making a pie chart on the ratio of females to males
gender_pie_chart = px.pie(
    gender_count,
    values = gender_count.values,
    names=['Female', 'Male'],
    title = 'Proportion of Females to Males',
    color_discrete_sequence= plot_colour)

gender_pie_chart.update_layout(legend_title_text = 'Gender Status', title_x=0.3, title_y= 0.95)
gender_pie_chart.show()


# counting the numbers in smoking_status column
smoking_status_count = data['smoking_status'].value_counts()

# smoking status pie chart
smoking_status_pie_chart = px.pie(
    smoking_status_count,
    values = smoking_status_count.values,
    names = ['Never smoked', 'Unknown', 'formerly smoked', 'smokes'],
    title = 'Proportion of smoking status of the participents',
    color_discrete_sequence = plot_colour)

smoking_status_pie_chart.update_layout(legend_title_text = 'Smoking Status', title_x = 0.3, title_y = 0.95)
smoking_status_pie_chart.show()

# counting the stroke account
stroke_count = data['stroke'].value_counts()

# stroke pie chart
stroke_pie_chart = px.pie(
    stroke_count,
    values = stroke_count.values,
    names = ['Yes', 'No'],
    title = 'Proportion of participents who did or did not suffer from a stroke',
    color_discrete_sequence = plot_colour)

stroke_pie_chart.update_layout(legend_title_text = 'Stroke Answers', title_x = 0.3, title_y = 0.95)
stroke_pie_chart.show()


# bar chart - gender vs stroke
bar_chart_gender = px.bar(
    data,
    x="gender",
    y="stroke",
    title="Bar chart: Gender vs Stroke",
    color_discrete_sequence = plot_colour,
    labels={"gender": "Gender", "stroke": "Stroke"})

bar_chart_gender.show()


# stroke vs hypertension  - pie chart  - finding the relationship between hypertension and stroke cases
grouped_hypertension = data.groupby('hypertension')['stroke'].mean().reset_index()
grouped_hypertension['stroke_percentage'] = grouped_hypertension['stroke'] * 100

hypertension_pie_chart = px.pie(
    grouped_hypertension,
    names="hypertension",
    values="stroke_percentage",
    title="Proportion participents that suffered from a stroke and hypertension/or no hypertension (high blood pressure)",
    color_discrete_sequence = plot_colour,
    labels={"hypertension":"Hypertension", "stroke_percentage": "Stroke Percentage",}
)
hypertension_pie_chart.update_layout(legend_title_text = 'Stroke Answers (1=Yes, 0=No)', title_x = 0.3, title_y = 0.95)
hypertension_pie_chart.show()

# converting the pie chart to a html
hypertension_pie_chart.write_html('hypertension_vs_stroke_pie_chart.html')

# stroke vs heart disease  - pie chart  - finding the relationship between heart disease and stroke cases
grouped_heart_disease = data.groupby('heart_disease')['stroke'].mean().reset_index()
grouped_heart_disease['stroke_percentage'] = grouped_heart_disease['stroke'] * 100

heart_disease_pie_chart = px.pie(
    grouped_heart_disease,
    names="heart_disease",
    values="stroke_percentage",
    title="Proportion of stroke cases that suffered from a stroke and heart disease/or no heart disease",
    color_discrete_sequence = plot_colour,
    labels={"heart_disease":"Heart Disease", "stroke_percentage": "Stroke Percentage"}
)
heart_disease_pie_chart.update_layout(legend_title_text = 'Stroke Answers (1=Yes, 0=No)', title_x = 0.3, title_y = 0.95)
heart_disease_pie_chart.show()

# converting the pie chart to a html
heart_disease_pie_chart.write_html('heart_disease_vs_stroke_pie_chart.html')


# average glucose level vs bmi  - scatter plot correlation between average glucose levels and bmi
data_stroke = data[data['stroke']==1]  # isolating the values that have stroke = 1

avg_glucose_bmi_scatter = px.scatter(
    data_stroke,
    x="bmi",
    y="avg_glucose_level",
    trendline="ols",
    title="Correlation between Average Glucose Level and BMI index of the participents who have had a stroke",
    color_discrete_sequence = plot_colour
)
avg_glucose_bmi_scatter.show()

# converting the pie chart to a html
avg_glucose_bmi_scatter.write_html('avg_glucose_bmi_scatter_plot.html')

# bar chart - age vs stroke
age_vs_stroke_histogram = px.histogram(
    data_stroke,
    x="age",
    y="stroke",
    title="Age of people who suffered from a stroke",
    color_discrete_sequence = plot_colour,
    labels={"age": "Age", "stroke": "Stroke Count"})

age_vs_stroke_histogram.show()

# converting the histogram to a html
age_vs_stroke_histogram.write_html('age_vs_stroke_histogram.html')

# smoking status vs stroke - bar chart
smoking_status_stroke = data.groupby(["smoking_status", "stroke"]).size().reset_index(name="count")
smoking_status_bar_chart = px.bar(
    smoking_status_stroke,
    x="smoking_status",
    y="count",
    color='stroke',
    barmode='group',
    title="Smoking Status of Participents who had and did not have a stroke",
    color_discrete_sequence = plot_colour,
    labels={"smoking_status":"Smoking Status", "stroke":"Stroke", "count": "Stroke Count"}
)
smoking_status_bar_chart.show()

# converting the pie chart to a html
smoking_status_bar_chart.write_html('smoking_status_bar_chart.html')







