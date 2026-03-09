"""
=========================================================================
Project:
- <project-name>

Module:
- reader

File: fetch_creditcard_churn_all.py

Purpose:
- extract 단계에서 creditcard_churn_all 테이블의 모든 데이터를 읽어오는 함수 정의

Author: qazx9
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
- 2026-03-09: reader package create and view select (조동휘)
=========================================================================
"""
import pandas as pd

from pipeline.db.connection.get_select_connection import get_select_connection

def fetch_creditcard_churn_all() -> pd.DataFrame:
    """

    :param query:
    :return:
    """

    query = """
    SELECT *
    FROM vw_creditcard_churn_ml
    """

    conn = get_select_connection()

    try:
        df = pd.read_sql(query, conn)

        return df

    finally:
        conn.close()