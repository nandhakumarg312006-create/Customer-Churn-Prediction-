📊 Customer Churn Prediction

An end-to-end **Customer Churn Prediction** project developed using **Python, SQL, Machine Learning, MLflow, and Streamlit**.

The project analyzes customer behavior, identifies factors associated with churn, builds a machine learning model to predict churn probability, and provides a Streamlit application with a retention strategy.

---

#🎯 Project Objective

The main objective of this project is to:

- Understand customer behavior and churn patterns
- Clean and prepare customer data
- Perform data analysis using Python and SQL
- Identify important factors contributing to customer churn
- Build and evaluate a machine learning model
- Track experiments using MLflow
- Create an interactive dashboard
- Develop a Streamlit application for customer churn prediction
- Provide retention strategies based on predicted churn probability

---

🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and machine learning |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| SQL | Data querying and analysis |
| Jupyter Notebook | Development and analysis |
| Scikit-learn | Machine learning |
| MLflow | Experiment tracking |
| Streamlit | Web application |
| Git & GitHub | Version control |

---

📌 Project Phases

## Phase 1 — Data Understanding & Exploration

The first phase focuses on understanding the customer churn dataset.
### Activities

- Dataset inspection
- Understanding columns and data types
- Checking missing values
- Checking duplicate records
- Understanding categorical and numerical variables
- Exploratory data analysis
- Identifying initial churn patterns

### Key Areas

- Customer demographics
- Services subscribed
- Contract information
- Payment methods
- Monthly charges
- Total charges
- Customer tenure
- Churn status

---

## Phase 2 — Data Cleaning & SQL Analysis

The second phase focuses on preparing the dataset for analysis and modeling.

### Activities

- Handling missing values
- Removing unnecessary columns
- Correcting data types
- Handling categorical variables
- Preparing clean data
- Performing SQL-based analysis

### SQL Analysis

SQL queries were used to analyze:

- Customer distribution
- Churn distribution
- Contract types
- Payment methods
- Monthly charges
- Customer tenure
- Churn-related patterns

---

## Phase 3 — Feature Engineering & Machine Learning

The third phase focuses on developing the churn prediction model.

### Activities

- Feature selection
- Feature engineering
- Encoding categorical variables
- Preparing input and target variables
- Splitting data into training and testing sets
- Model training
- Model evaluation

### Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC where applicable

The objective was to develop a model capable of estimating the probability that a customer may churn.

---

## Phase 4 — Dashboard & MLflow

The fourth phase focuses on visualization and experiment tracking.

### Dashboard

An interactive dashboard was developed to visualize customer churn information and important business insights.

The dashboard helps understand:

- Overall churn distribution
- Customer characteristics
- Contract patterns
- Payment behavior
- Charges
- Service usage
- Churn-related trends

### MLflow

MLflow was used for experiment tracking.

Tracked information includes:

- Model experiments
- Parameters
- Evaluation metrics
- Model results

---

# 🚀 Phase 5 — Customer Churn Prediction Application

The final phase converts the machine learning solution into an interactive application using **Streamlit**.

The application allows users to enter customer information and generate a churn prediction.

### Application Features

- Customer information input
- Service information
- Tenure
- Monthly charges
- Total charges
- Contract type
- Payment method
- Churn probability
- Churn prediction
- Retention strategy

### Prediction Result

The application displays the estimated churn probability.

Example:

```text
Churn Probability: 78.67%

Customer is likely to churn.
