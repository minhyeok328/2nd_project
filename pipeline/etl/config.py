"""
=========================================================================
Project:
- <project-name>

Module:
- pipeline\etl

File: config.py

Purpose:
- etl configuration

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
=========================================================================
"""
CUSTOMER_RENAME_DICT = {
    "Attrition_Flag": "churn",
    "Customer_Age": "age",
    "Gender": "gender",
    "Dependent_count": "dependents",
    "Education_Level": "education",
    "Marital_Status": "marital",
    "Income_Category": "income",
    "Card_Category": "card_type",
    "Months_on_book": "relationship_months",
    "Total_Relationship_Count": "product_count",
    "Months_Inactive_12_mon": "inactive_months",
    "Contacts_Count_12_mon": "contact_count",
    "Credit_Limit": "credit_limit",
    "Total_Revolving_Bal": "revolving_balance",
    "Avg_Open_To_Buy": "available_credit",
    "Total_Amt_Chng_Q4_Q1": "amount_change",
    "Total_Ct_Chng_Q4_Q1": "count_change",
    "Total_Trans_Amt": "transaction_amount",
    "Total_Trans_Ct": "transaction_count",
    "Avg_Utilization_Ratio": "utilization_ratio",
}

DB_RENAME_DICT = {
    "education": "education_id",
    "marital": "marital_id",
    "income": "income_id",
    "card_type": "card_type_id",
    "churn": "churn_status",
}

CUSTOMER_COLUMNS = [
    "churn",
    "age",
    "gender",
    "dependents",
    "education",
    "marital",
    "income",
    "card_type",
    "relationship_months",
    "product_count",
    "inactive_months",
    "contact_count",
    "credit_limit",
    "revolving_balance",
    "available_credit",
    "amount_change",
    "count_change",
    "transaction_amount",
    "transaction_count",
    "utilization_ratio",
]

CREDITCARD_CHURN_COLUMNS = [
    "education_id",
    "marital_id",
    "income_id",
    "card_type_id",
    "age",
    "gender",
    "dependents",
    "relationship_months",
    "product_count",
    "churn_status",
    "inactive_months",
    "contact_count",
    "credit_limit",
    "revolving_balance",
    "available_credit",
    "amount_change",
    "count_change",
    "transaction_amount",
    "transaction_count",
    "utilization_ratio",
]

CHURN_MAP = {
    "Existing Customer": 0,
    "Attrited Customer": 1,
}

EDUCATION_MAP = {
    "Uneducated": 1,
    "High School": 2,
    "College": 3,
    "Graduate": 4,
    "Post-Graduate": 5,
    "Doctorate": 6,
    "Unknown": 7,
}

MARITAL_MAP = {
    "Single": 1,
    "Married": 2,
    "Divorced": 3,
    "Unknown": 4,
}

INCOME_MAP = {
    "Less than $40K": 1,
    "$40K - $60K": 2,
    "$60K - $80K": 3,
    "$80K - $120K": 4,
    "$120K +": 5,
    "Unknown": 6,
}

CARD_TYPE_MAP = {
    "Blue": 1,
    "Silver": 2,
    "Gold": 3,
    "Platinum": 4,
}

GENDER_MAP = {
    "F": 0,
    "M": 1,
}
