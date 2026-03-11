"""
=========================================================================
Project:
- <project-name>

Module:
- 

File: load_csv.py

Purpose:
- load the csv file and exchange pandas dataframe

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
=========================================================================
"""
from pathlib import Path

import pandas as pd

def load_csv():
    """
    load the csv file and exchange pandas dataframe
    :return:
    """
    csv_path = Path(__file__).resolve().parent.parent / "data" / "BankChurners.csv"
    return pd.read_csv(csv_path)