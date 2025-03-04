# Employee Performance Prediction Model  

## 📌 Overview  
This project builds and deploys a machine learning model to **predict employee performance scores** based on key factors such as **years at the company, salary, overtime hours, promotions, projects handled, and employee satisfaction scores**. The model is deployed as an interactive web app using **Streamlit**.

## 🛠 Tech Stack  
- **Programming Language:** Python  
- **Libraries:** pandas, scikit-learn, matplotlib, seaborn  
- **Model:** Random Forest, Linear Regression, Decision Tree (best model selected based on evaluation)  
- **Deployment:** Streamlit  

## 📊 Data & Features  
The dataset includes the following key attributes:  
| Feature                | Description |
|------------------------|------------|
| `years_at_company`     | Total years the employee has worked in the company |
| `monthly_salary`       | Employee's monthly salary |
| `overtime_hours`       | Total overtime hours worked |
| `promotions`           | Number of promotions received |
| `projects_handled`     | Total projects assigned |
| `employee_satisfaction`| Satisfaction score (scale of 1-10) |
| `performance_score`    | Target variable (performance rating) |

## 🔍 Exploratory Data Analysis (EDA)  
EDA was conducted to understand **feature distributions, correlations, and outliers**. Some key insights:  
- **Employee satisfaction** has the highest positive correlation with performance.  
- **Overtime hours** show a non-linear effect—moderate overtime increases performance, but excessive overtime reduces it.  
- **Higher salaries** are generally associated with better performance, but some high-paid employees underperform.  

## 🚀 Model Training & Evaluation  
The following models were tested:  
- **Linear Regression** (Baseline)  
- **Random Forest Regressor** (Best Performing Model)  
- **Decision Tree Regressor**  

📈 **Best Model Performance:**  
| Metric | Value |
|--------|-------|
| R² Score | 0.87 |
| RMSE | 3.2 |

## 🌍 Deployment  
The model is deployed using **Streamlit**, enabling users to input employee details and predict performance interactively.  

