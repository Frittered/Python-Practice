import numpy as np
import pandas as pd
import DDM
#DDM is a custom Data Description Module found in github.com/Fritz-Stevenson/Data-Analysis
from sklearn import metrics, linear_model
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

a = DDM.DDM('healthcare-dataset-stroke-data.csv', 'unsafe')
a.full()

'''
What did we learn from the DDM module
5 % - 95 % stroke/no-stroke

Highly variable avg_glucose_level

Hypertension/Heart_Disease- very low mean and high standard deviation = right skew, likely determinant.

201 rows do not contain a bmi. Let's maintain 2 analysis channels: #1 which maintains the rows but doesn't use bmi as a 
independent variable and #2 which drops the rows without bmi and uses all fields as independent variables
'''
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df2 = df.dropna()

''' for sklearn to process categorical data, we need to change categories to integers. Notice that 'unknown' and 
'never smoked' have been consolidated into a single category, and 'smokes' and 'formerly smoked' have been grouped
as well.
'''

df['smoking_status'].loc[df['smoking_status'].isin(['Unknown', 'never smoked'])] = 0
df['smoking_status'].loc[df['smoking_status'].isin(['smokes', 'formerly smoked'])] = 1
df2['smoking_status'].loc[df2['smoking_status'].isin(['Unknown', 'never smoked'])] = 0
df2['smoking_status'].loc[df2['smoking_status'].isin(['smokes', 'formerly smoked'])] = 1
df['ever_married'].loc[df['ever_married'] == 'No'] = 0
df['ever_married'].loc[df['ever_married'] == 'Yes'] = 1
df2['ever_married'].loc[df2['ever_married'] == 'No'] = 0
df2['ever_married'].loc[df2['ever_married'] == 'Yes'] = 1
df['gender'].loc[df['gender'].isin(['Male', 'Other'])] = 0
df['gender'].loc[df['gender'] == 'Female'] = 1
df2['gender'].loc[df2['gender'].isin(['Male', 'Other'])] = 0
df2['gender'].loc[df2['gender'] == 'Female'] = 1

'''Groupby, much like a pivot table, shows us the difference in mean values between stroke victims and the rest of the 
population.'''
print(df2.groupby(['stroke']).mean())
''' Stroke victims were 4 times more likely to have had heart disease, had nearly 4 times the hypertension on average, 
were 26 years older on average, and had nearly 33% higher glucose levels'''

'''
Now begins the first knneighbour test, where we experiment with how the number and choice of categories affects the 
accuracy of model predictions

Here you can see two y variables which represent the two dataframes: one with bmi and one without. There are also
3 sets of x variables; 2 use a slightly paired down set of columns, identical except for the 'bmi' column. The 3rd set
is much more limited set of values that have been hand picked as hypothetically the most determinant of stroke 
likelihood. 

Experts state that the knneighbour algorithms become less effective as more variables/dimensions are added, as the 
relative distance between neighbours shrinks and data converges on the data point. 

This test aims to test this assertion at this level of dimensionality and data density.'''
y1 = df['stroke'].values
y2 = df2['stroke'].values
x1 = df[['smoking_status', 'avg_glucose_level', 'ever_married', 'hypertension', 'age', 'gender', 'heart_disease']].values
x2 = df2[['smoking_status', 'avg_glucose_level', 'ever_married', 'hypertension', 'age', 'gender', 'heart_disease', 'bmi']].values
x3 = df2[['bmi', 'hypertension', 'smoking_status', 'heart_disease']].values

for i in range(1,4):
    accuracy_set = []
    title_list = ['Variables Except BMI', 'Variables Including BMI', 'Custom Variables']
    if i == 1:
        x = x1
        y = y1
        x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=4)
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))

    elif i == 2:
        x = x2
        y = y2
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=4)
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))
    else:
        x = x3
        y = y2
        x_train, x_test, y_train, y_test = train_test_split(x3, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=4)
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))
    print(title_list[i-1], '\n',np.average(accuracy_set))

# The following tests the relative efficiency of the algorithms available in the kneighbour class: ball tree, kd tree, and brute force.
for i in range(1,4):
    accuracy_set = []
    title_list = ['ball_tree', 'kd_tree', 'brute']
    if i == 1:
        x = x1
        y = y1
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=4, algorithm='ball_tree')
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))
    elif i == 2:
        x = x2
        y = y2
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=4, algorithm='kd_tree')
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))
    else:
        x = x3
        y = y2
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=4, algorithm='brute')
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))
    print(title_list[i-1], '\n',np.average(accuracy_set))
# I appears for this dataset, kd tree is marginally more effective, and brute force is marginally less effective.

'''As the number of neighbours tested is a key variable that determines the answer, it is worth testing how this affects the accuracy results. Due to the density of the 
dimensions, and complexity and variance in bioinformatic correllation, I predict a relatively high number of neighbours will yield more consistent results.
for i in range(1, 4):
    accuracy_set = []
    title_list = ['2 Neighbours', '4 Neighbours', '8 Neighbours']
    if i == 1:
        x = x1
        y = y1
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=2)
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))

    elif i == 2:
        x = x2
        y = y2
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=4)
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))
    else:
        x = x3
        y = y2
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=.20)
        kn = KNeighborsClassifier(n_neighbors=8)
        for x in range(100):
            kn.fit(x_train, y_train)
            predictions = kn.predict(x_test)
            accuracy_set.append(metrics.accuracy_score(y_test, predictions))
    print(title_list[i - 1], '\n', np.average(accuracy_set))
# My hypothesis was somewhat correct. The fit with 2 neighbours tested was the least accurate, but the difference between 4 and 8 neighbours isn't statistically relevant.
    
# Lets check the regression score for each variable. Perhaps this will allow us to isolate the most determinant variables to refine our kneighbour machine learning algorithm
for variable in ['smoking_status', 'avg_glucose_level', 'ever_married', 'hypertension', 'age', 'gender', 'heart_disease']:
    lm = linear_model.LinearRegression()
    model = lm.fit(df2[variable].values.reshape(-1,1), df['stroke'].values.reshape(-1,1))
    print(f'{variable} r^2 value: {lm.score(df2[variable].values.reshape(-1,1), df2["stroke"].values.reshape(-1,1))}')
# Like in the Hepatitis C model, linear regression for any single factor is ineffective. 

