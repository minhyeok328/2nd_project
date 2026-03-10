"""
=========================================================================
Project:
- Credit Card Customers

Module:
- streamlit

File: app.py

Purpose:
- Streamlit main page

Author: @조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@조동휘)
=========================================================================
"""

import streamlit as st

st.set_page_config(
    page_title="Credit Card Customers",
    page_icon="💳",
    layout="wide",
)

st.title("Credit Card Customers Dashboard")

st.write(
    """
    Streamlit UI for the Credit Card Customers project.

    This dashboard will provide:
    - EDA visualization
    - Model performance monitoring
    - Prediction interface
    """
)

st.success("Streamlit container is running successfully.")