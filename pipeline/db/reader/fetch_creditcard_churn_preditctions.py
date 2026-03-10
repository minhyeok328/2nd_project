"""
=========================================================================
Project:
- project-name

Module:
- reader

File: fetch_creditcard_churn_preditctions.py

Purpose:
- vw_creditcard_churn_predictions 뷰의 데이터를 읽어오는 함수 정의

Author: @조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@조동휘)
=========================================================================
"""

import pandas as pd

from pipeline.db.connection.get_select_connection import get_select_connection


def fetch_creditcard_churn_predictions() -> pd.DataFrame:
    """
    vw_creditcard_churn_predictions를 이용해서 data를 조회하는 함수

    Returns:
        pd.DataFrame: vw_creditcard_churn_predictions 뷰의 데이터가 담긴 DataFrame
    """

    query = """
    SELECT *
    FROM vw_creditcard_churn_predictions
    """

    conn = get_select_connection()

    try:
        df = pd.read_sql(query, conn)

        return df

    finally:
        conn.close()
