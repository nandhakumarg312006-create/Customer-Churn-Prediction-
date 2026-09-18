import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained model
# -----------------------------
pipeline = joblib.load("models/churn_model_pipeline.pkl")


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict the probability of churn.")


# -----------------------------
# Customer Information
# -----------------------------

st.subheader("Customer Information")

senior_citizen = st.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)

partner = st.selectbox(
    "Partner",
    ["No", "Yes"]
)

dependents = st.selectbox(
    "Dependents",
    ["No", "Yes"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)


# -----------------------------
# Services
# -----------------------------

st.subheader("Services")

phone_service = st.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["No", "DSL", "Fiber optic"]
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No", "Yes"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["No", "Yes"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["No", "Yes"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes"]
)


# -----------------------------
# Billing Information
# -----------------------------

st.subheader("Billing Information")

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)


# -----------------------------
# Contract & Payment
# -----------------------------

st.subheader("Contract & Payment")

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)


# -----------------------------
# Prediction Button
# -----------------------------

if st.button("🔮 Predict Churn", use_container_width=True):

    # Convert Yes/No values into 0/1
    senior_citizen_value = 1 if senior_citizen == "Yes" else 0
    partner_value = 1 if partner == "Yes" else 0
    dependents_value = 1 if dependents == "Yes" else 0
    phone_service_value = 1 if phone_service == "Yes" else 0
    paperless_billing_value = 1 if paperless_billing == "Yes" else 0

    gender_male = 1 if gender == "Male" else 0

    multiple_lines_true = 1 if multiple_lines == "Yes" else 0

    internet_fiber = 1 if internet_service == "Fiber optic" else 0

    online_security_true = 1 if online_security == "Yes" else 0
    online_backup_true = 1 if online_backup == "Yes" else 0
    device_protection_true = 1 if device_protection == "Yes" else 0
    tech_support_true = 1 if tech_support == "Yes" else 0
    streaming_tv_true = 1 if streaming_tv == "Yes" else 0
    streaming_movies_true = 1 if streaming_movies == "Yes" else 0

    contract_one_year = 1 if contract == "One year" else 0
    contract_two_year = 1 if contract == "Two year" else 0

    payment_credit_card = (
        1 if payment_method == "Credit card (automatic)" else 0
    )

    payment_electronic_check = (
        1 if payment_method == "Electronic check" else 0
    )

    payment_mailed_check = (
        1 if payment_method == "Mailed check" else 0
    )


    # -----------------------------
    # Create input dataframe
    # -----------------------------

    input_data = pd.DataFrame([{
        "SeniorCitizen": senior_citizen_value,
        "Partner": partner_value,
        "Dependents": dependents_value,
        "tenure": tenure,
        "PhoneService": phone_service_value,
        "PaperlessBilling": paperless_billing_value,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "gender_Male": gender_male,
        "MultipleLines_True": multiple_lines_true,
        "InternetService_Fiber optic": internet_fiber,
        "OnlineSecurity_True": online_security_true,
        "OnlineBackup_True": online_backup_true,
        "DeviceProtection_True": device_protection_true,
        "TechSupport_True": tech_support_true,
        "StreamingTV_True": streaming_tv_true,
        "StreamingMovies_True": streaming_movies_true,
        "Contract_One year": contract_one_year,
        "Contract_Two year": contract_two_year,
        "PaymentMethod_Credit card (automatic)": payment_credit_card,
        "PaymentMethod_Electronic check": payment_electronic_check,
        "PaymentMethod_Mailed check": payment_mailed_check
    }])


    # -----------------------------
    # Make prediction
    # -----------------------------

    prediction = pipeline.predict(input_data)[0]

    probability = pipeline.predict_proba(input_data)[0][1]

    probability_percent = probability * 100


    # -----------------------------
    # Display result
    # -----------------------------

    st.subheader("Prediction Result")

    st.metric(
        "Churn Probability",
        f"{probability_percent:.2f}%"
    )

    if prediction == 1:

        st.error("⚠️ Customer is likely to CHURN")

    else:

        st.success("✅ Customer is likely to STAY")
# ------------------------------
# Retention Strategy
# ------------------------------

    st.subheader("💡 Retention Strategy")

    if probability >= 0.70:
      st.error("🔴 High Churn Risk")
      st.write(
        "Recommended Action: Offer a personalized retention discount "
        "and encourage the customer to move to a longer-term contract."
    )

    elif probability >= 0.40:
     st.warning("🟠 Medium Churn Risk")
     st.write(
        "Recommended Action: Provide a targeted offer and contact the "
        "customer to understand their concerns."
    )

    else:
      st.success("🟢 Low Churn Risk")
      st.write(
        "Recommended Action: Continue regular engagement and provide "
        "loyality benifits to encourage continued usage."
    )
