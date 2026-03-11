"""
=========================================================================
Project:
- <project-name>

Module:
- pipeline\test

File: etl.py

Purpose:
- etl line test

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
=========================================================================
"""
import pandas as pd

from pipeline.db import insert_dataframe
from pipeline.etl import load_csv
from pipeline.etl import standardize_customer_columns

def run_etl_test() -> pd.DataFrame:
    """
    test for etl line

    :return:
    """

    df = load_csv()
    df = standardize_customer_columns(df)

    insert_count = insert_dataframe("creditcard_churn", df)
    
    print(f"Inserted {insert_count} rows into the database.")

if __name__ == '__main__':
    run_etl_test()
