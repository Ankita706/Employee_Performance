# x order -> 'Years_At_Company', 'Monthly_Salary', 'Overtime_Hours', 'Promotions','Projects_Handled', 'Employee_Satisfaction_Score'
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Run the app.py file
# Open the browser and type http://
# Enter the values in the form and click on Predict button
# The predicted value will be displayed on the screen


import streamlit as st
import joblib
import numpy as np

scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

st.title('Employee Performance Prediction')

st.divider()

st.write('Enter the details of the employee to predict the performance')

st.divider()

years_at_company = st.number_input('Years at Company', min_value=0, max_value=40, value=2)
salary = st.number_input('Monthly Salary', min_value=0, max_value=100000, value=50000)
overtime_hours = st.number_input('Overtime Hours', min_value=0, max_value=100, value=10)
promotions = st.number_input('Promotions', min_value=0, max_value=10, value=1)
projects_handled = st.number_input('Projects Handled', min_value=0, max_value=10, value=1)
employee_satisfaction_score = st.number_input('Employee Satisfaction Score', min_value=0, max_value=5, value=0)



x = [years_at_company, salary, overtime_hours, promotions, projects_handled, employee_satisfaction_score]

st.divider()

if predict_button := st.button('Predict'):
    x = np.array(x).reshape(1, -1)
    x = scaler.transform(x)
    prediction = model.predict(x)
    st.balloons()
    st.write(f'The predicted performance of the employee is {prediction[0]}')


else:
    st.write('Click on the Predict button to get the prediction')