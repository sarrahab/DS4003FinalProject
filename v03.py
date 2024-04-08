# %% [markdown]
# ## Internal Human Resources Analytics Dashboard V0: Sarrah Abdulali
# 
# DS4003 | Spring 2024
# 
# Objective: To begin the dashboard build of DS 4003 Final Project
# 
# Task: Build an app/dashboard that contains components using the human resources dataset: `data.csv`. [Info](https://www.kaggle.com/datasets/rhuebner/human-resources-data-set/code)

# %% [markdown]
# ### Data Dictionary

# %% [markdown]
# | Feature                     | Description                                                               | DataType |
# |-----------------------------|---------------------------------------------------------------------------|----------|
# | Employee Name               | Employee’s full name                                                      | Object   |
# | EmpID                       | Employee ID is unique to each employee                                    | Integer  |
# | MarriedID                   | Is the person married (1 or 0 for yes or no)                              | Integer  |
# | MaritalStatusID             | Marital status code that matches the text field MaritalDesc               | Integer  |
# | GenderID                    | Gender status code that matches the text field Sex                        | Integer  |
# | EmpStatusID                 | Employment status code that matches text field EmploymentStatus           | Integer  |
# | DeptID                      | Department ID code that matches the department the employee works in      | Integer  |
# | PerfScoreID                 | Performance Score code that matches the employee’s most recent performance score | Integer  |
# | FromDiversityJobFairID      | Was the employee sourced from the Diversity job fair? 1 or 0 for yes or no | Binary   |
# | Salary                      | The person’s yearly salary. $ U.S. Dollars                                | Integer    |
# | Termd                       | Has this employee been terminated - 1 or 0                                | Binary   |
# | PositionID                  | An integer indicating the person’s position                               | Integer  |
# | Position                    | The text name/title of the position the person has                        | Object     |
# | DOB                         | Date of Birth for the employee                                            | Date     |
# | Sex                         | Sex - M or F                                                              | Object    |
# | MaritalDesc                 | The marital status of the person (divorced, single, widowed, separated, etc) | Object     |
# | HispanicLatino              | Yes or No field for whether the employee is Hispanic/Latino               | Boolean    |
# | RaceDesc                    | Description/text of the race the person identifies with                   | Object    |
# | DateofHire                  | Date the person was hired                                                 | Date     |
# | DateofTermination           | Date the person was terminated, only populated if, in fact, Termd = 1     | Date     |
# | TermReason                  | A text reason / description for why the person was terminated             | Object     |
# | EmploymentStatus            | A description/category of the person’s employment status. Anyone currently working full time = Active | Object     |
# | Department                  | Name of the department that the person works in                           | Object     |
# | ManagerName                 | The name of the person’s immediate manager                                | Object    |
# | ManagerID                   | A unique identifier for each manager.                                     | Integer  |
# | RecruitmentSource           | The name of the recruitment source where the employee was recruited from  | Object     |
# | PerformanceScore            | Performance Score text/category (Fully Meets, Partially Meets, PIP, Exceeds) | Object     |
# | EngagementSurvey            | Results from the last engagement survey, managed by an external partner  | Integer    |
# | EmpSatisfaction             | A basic satisfaction score between 1 and 5, as reported on a recent employee satisfaction survey | Integer  |
# | LastPerformanceReviewDate   | The most recent date of the person’s last performance review.              | Date     |
# | Absences                    | The number of times the employee was absent from work.                    | Integer  |
# 

# %%
#import dependencies
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output
from datetime import datetime
import numpy as np

# %%
#read in the dataset and then see first five rows of the dataframe df
df = pd.read_csv('C:/Users/Student/Downloads/data.csv')
df.head()

# %% [markdown]
# ### Coding UI and Graph Components

# %% [markdown]
# (1) UI Components:
# Dropdown menus for each of the following components:
# - `Department`
# - `Position`
# - `Performance Scores`
# - `Gender`
# 
# Sliders that allows the user to select:
# - `Salary Range`
# - `Age Range`
# - `Employee Satisfaction`
# 
# Date Range Selector that allows a start and end date for all visuals in the dashboard
# - `Start Date`
# - `End Date`
#  
# 
# (2) Write Callback functions for the widgets to interact with the graphs
# 
# Layout:
# - Use a stylesheet
# - There should be a title at the top of the page
# - There should be a description of the data and app below the title (3-5 sentences)
# 

# %%
# convert DOB to datetime format if not already
df['DOB'] = pd.to_datetime(df['DOB'])

# calculate age correctly
today = pd.to_datetime('today')
df['Age'] = today.year - df['DOB'].dt.year
# adjusting for whether the birthday has happened this year
df['Age'] -= ((today.month < df['DOB'].dt.month) | ((today.month == df['DOB'].dt.month) & (today.day < df['DOB'].dt.day))).astype(int)

# %%
# set the minimum salary for the slider
salary_min = df['Salary'].min()
# set the maximum salary for the slider
salary_max = df['Salary'].max()
# finding a representative middle value for user friendliness in the slider
salary_mid = round((salary_min + salary_max) / 2 / 1000) * 1000  

# labelling on the slider
salary_marks = {
    int(salary_min): f'${int(salary_min):,}',
    int(salary_mid): f'${int(salary_mid):,}',
    int(salary_max): f'${int(salary_max):,}'
}

# set the minimum age for the slider
age_min = df['Age'].min()
# set the maximum salary for the slider
age_max = df['Age'].max()
# finding a representative middle value for user friendliness in the slider
age_mid = round((age_min + age_max) / 2 / 10) * 10

# labelling on the slider
age_marks = {
    int(age_min): f'{int(age_min)} yrs',
    int(age_mid): f'{int(age_mid)} yrs',
    int(age_max): f'{int(age_max)} yrs'
}

# correcting marks for EmpSatisfaction slider to ensure keys are Python integers
satisfaction_marks = {int(satisfaction): str(satisfaction) for satisfaction in sorted(df['EmpSatisfaction'].unique())}

# %%
# import external stylesheet using class code below

stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # load the CSS stylesheet

app = dash.Dash(__name__, external_stylesheets=stylesheets) # initialize the app
server = app.server

# %%
app.layout = html.Div(children=[
    html.H1('HR Analytics Dashboard', style={'textAlign': 'center', 'color': '#4b2e83'}), # purple text color for the title
    
    html.P('''
        Welcome to our HR Analytics Dashboard! This powerful tool brings you closer to understanding the intricacies of employee engagement, performance, and satisfaction across the spectrum of departments, job positions, and diverse demographic backgrounds. 
        Leverage our intuitive filters to segment the data meaningfully, and embark on your journey towards data-driven HR excellence today. Discover trends, pinpoint opportunities for improvement, and make informed decisions that lead to impactful outcomes.
        ''', style={'textAlign': 'center', 'color': '#4b2e83'}), # purple text color for the description of the app
    
    html.Div([
        # wrapping each component in a Div with padding for spacing
        # starting with the department dropdown menu
        html.Div([
            dcc.Dropdown(
                id='department-dropdown',
                options=[{'label': dept, 'value': dept} for dept in df['Department'].unique()],
                value=None,
                placeholder='Select Department',
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),

        # position dropdown menu
        html.Div([
            dcc.Dropdown(
                id='position-dropdown',
                options=[{'label': pos, 'value': pos} for pos in df['Position'].unique()],
                value=None,
                placeholder='Select Position',
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),
        
        # performance dropdown menu
        html.Div([
            dcc.Dropdown(
                id='performance-dropdown',
                options=[{'label': score, 'value': score} for score in df['PerformanceScore'].unique()],
                value=None,
                placeholder='Select Performance Score',
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),
        
        # gender dropdown menu
        html.Div([
            dcc.Dropdown(
                id='gender-dropdown',
                options=[{'label': gender, 'value': gender} for gender in df['Sex'].unique()],
                value=None,
                placeholder='Select Gender',
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),
        
        # creating the salary slider 
        html.Div([
            html.Label('Salary', style={'fontSize': 15, 'marginTop': '20px'}),  # adding a label for the salary slider
            dcc.RangeSlider(
                id='salary-slider',
                min=df['Salary'].min(),
                max=df['Salary'].max(),
                value=[df['Salary'].min(), df['Salary'].max()],
                marks=salary_marks,
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),
        
        # creating the age slider 
        html.Div([
            html.Label('Age', style={'fontSize': 15, 'marginTop': '20px'}),  # adding a label for the age slider
            dcc.RangeSlider(
                id='age-slider',
                min=df['Age'].min(),
                max=df['Age'].max(),
                value=[df['Age'].min(), df['Age'].max()],
                marks=age_marks,
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),
        
        # creating the employee satisfaction score slider 
        html.Div([
            html.Label('Employee Satisfaction Score', style={'fontSize': 15, 'marginTop': '20px'}),  # adding a label for the satisfaction slider
            dcc.Slider(
                id='satisfaction-slider',
                min=df['EmpSatisfaction'].min(),
                max=df['EmpSatisfaction'].max(),
                value=df['EmpSatisfaction'].max(),
                marks=satisfaction_marks,
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),
        
        # creating the date picker for start date and end date
        html.Div([
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=df['DateofHire'].min(),
                end_date=df['DateofHire'].max(),
                display_format='YYYY-MM-DD',
            ),
        ], style={'marginBottom': '20px', 'position': 'relative'}),
        
    ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px', 'backgroundColor': '#f3f2f4', 'position': 'relative'}), #light gray sidebar background
    
    #container for the graphs--scatterplot and bar graph
    html.Div([
        dcc.Graph(id='salary-engagement-scatter'),
        dcc.Graph(id='avg-satisfaction-bar'),  # add this line for the bar chart
    ], style={'width': '70%', 'display': 'inline-block', 'backgroundColor': '#f3f2f4', 'position': 'relative'}), #light gray background in main content area
])

# callback for updating the scatter plot
@app.callback(
    Output('salary-engagement-scatter', 'figure'),
    [Input('department-dropdown', 'value'),
     Input('position-dropdown', 'value'),
     Input('performance-dropdown', 'value'),
     Input('gender-dropdown', 'value'),
     Input('salary-slider', 'value'),
     Input('age-slider', 'value'),
     Input('satisfaction-slider', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')])
def update_scatter_plot(department, position, performance, gender, salary_range, age_range, satisfaction, start_date, end_date):
    # ensure DateofHire is a datetime object for date filtering
    filtered_df = df.copy()
    filtered_df['DateofHire'] = pd.to_datetime(filtered_df['DateofHire'])

    # apply filters based on the inputs
    if department:
        filtered_df = filtered_df[filtered_df['Department'] == department]
    if position:
        filtered_df = filtered_df[filtered_df['Position'] == position]
    if performance:
        filtered_df = filtered_df[filtered_df['PerformanceScore'] == performance]
    if gender:
        filtered_df = filtered_df[filtered_df['Sex'] == gender]
    if salary_range:
        filtered_df = filtered_df[(filtered_df['Salary'] >= salary_range[0]) & (filtered_df['Salary'] <= salary_range[1])]
    if age_range:
        filtered_df = filtered_df[(filtered_df['Age'] >= age_range[0]) & (filtered_df['Age'] <= age_range[1])]
    if satisfaction:
        filtered_df = filtered_df[filtered_df['EmpSatisfaction'] == satisfaction]
    
    # generate and return the scatter plot figure based on filtered_df
    fig_scatter = px.scatter(filtered_df, x='Salary', y='EngagementSurvey', 
                             title='Employee Engagement Score VS Salary', 
                             hover_data=['Employee_Name']) 
    
    fig_scatter.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # transparent background for plot
        paper_bgcolor= '#f3f2f4',  # light gray background outside the plot area
        font=dict(color= '#4b2e83'),  # purple font color
    )

    # update the y-axis title
    fig_scatter.update_yaxes(title_text='Engagement Survey Score')

    fig_scatter.update_traces(marker=dict(color='#4b2e83'))  # my preferred shade of purple


    return fig_scatter

# callback for updating the bar chart
@app.callback(
    Output('avg-satisfaction-bar', 'figure'),
    [Input('department-dropdown', 'value'),
     Input('position-dropdown', 'value'),
     Input('performance-dropdown', 'value'),
     Input('gender-dropdown', 'value'),
     Input('salary-slider', 'value'),
     Input('age-slider', 'value'),
     Input('satisfaction-slider', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')])
def update_bar_chart(department, position, performance, gender, salary_range, age_range, satisfaction, start_date, end_date):
    # start with a copy of the full DataFrame
    filtered_df1 = df.copy()
    
    # convert 'DateofHire' to datetime for filtering, if necessary
    filtered_df1['DateofHire'] = pd.to_datetime(filtered_df1['DateofHire'])
    
    # apply filters based on the inputs
    if department:
        filtered_df1 = filtered_df1[filtered_df1['Department'] == department]
    if position:
        filtered_df1 = filtered_df1[filtered_df1['Position'] == position]
    if performance:
        filtered_df1 = filtered_df1[filtered_df1['PerformanceScore'] == performance]
    if gender:
        filtered_df1 = filtered_df1[filtered_df1['Sex'] == gender]
    if salary_range:
        filtered_df1 = filtered_df1[(filtered_df1['Salary'] >= salary_range[0]) & (filtered_df1['Salary'] <= salary_range[1])]
    if age_range:
        filtered_df1 = filtered_df1[(filtered_df1['Age'] >= age_range[0]) & (filtered_df1['Age'] <= age_range[1])]
    if start_date and end_date:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        filtered_df1 = filtered_df1[(filtered_df1['DateofHire'] >= start_date_obj) & (filtered_df1['DateofHire'] <= end_date_obj)]

    # calculate the average employee satisfaction by department for the filtered DataFrame
    avg_emp_satisfaction = filtered_df1.groupby('Department')['EmpSatisfaction'].mean().reset_index()

    # generate the bar chart figure based on the filtered and aggregated data
    fig_bar = px.bar(avg_emp_satisfaction, x='Department', y='EmpSatisfaction',
                     text=avg_emp_satisfaction['EmpSatisfaction'].apply(lambda x: f'{x:.2f}'),
                     labels={'EmpSatisfaction': 'Average Satisfaction'},
                     title='Average Employee Satisfaction by Department',
                     color_discrete_sequence=['#4b2e83']  # Makes bars purple
    )
    fig_bar.update_traces(marker_color='#4b2e83', texttemplate='%{text}', textposition='outside') #preferred shade of purple for the traces

    fig_bar.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',  # transparent background for plot
        paper_bgcolor='#f3f2f4',  # light gray background outside the plot area
        font=dict(color='#4b2e83'),  # purple font color
        xaxis_tickangle=-45
    )
    
    return fig_bar

# run the app
if __name__ == '__main__':
    app.run_server(debug=True) #run the server

# %%



