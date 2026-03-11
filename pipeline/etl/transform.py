"""
=========================================================================
Project:
- <project-name>

Module:
- 

File: transform.py

Purpose:
- dataframe processing

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
=========================================================================
"""
import pandas as pd

from .config import CARD_TYPE_MAP, CHURN_MAP, CREDITCARD_CHURN_COLUMNS, CUSTOMER_RENAME_DICT, CUSTOMER_COLUMNS, DB_RENAME_DICT, EDUCATION_MAP, GENDER_MAP, INCOME_MAP, MARITAL_MAP


def standardize_customer_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize customer dataset column names and order.

    Parameters
    ----------
    df : pd.DataFrame
        Raw customer dataframe.

    Returns
    -------
    pd.DataFrame
        DataFrame with standardized column names and column order.
    """

    df = df.rename(columns=CUSTOMER_RENAME_DICT)
    df["churn"] = df["churn"].map(CHURN_MAP)
    df["education"] = df["education"].map(EDUCATION_MAP)
    df["marital"] = df["marital"].map(MARITAL_MAP)
    df["income"] = df["income"].map(INCOME_MAP)
    df["card_type"] = df["card_type"].map(CARD_TYPE_MAP)
    df["gender"] = df["gender"].map(GENDER_MAP)
    
    df = df.rename(columns=DB_RENAME_DICT)
    df = df[CREDITCARD_CHURN_COLUMNS]
    
    return df.loc[:, CREDITCARD_CHURN_COLUMNS].copy()