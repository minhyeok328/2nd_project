"""
=========================================================================
Project:
- project-name

Module:
- reader

File: fetch_creditcard_churn_preditctions.py

Purpose:
- vw_creditcard_churn_predictions 뷰의 데이터를 읽어오는 함수 정의

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
- 2026-03-10: 작성자와 업데이트자 이름 github로 변경 및 pd.read에서 conn사용 (@nobrain711)
=========================================================================
"""
from pandas import DataFrame

from pipeline.db.connection.get_select_connection import get_select_connection


def fetch_creditcard_churn_predictions() -> DataFrame:
    """
    vw_creditcard_churn_predictions를 이용해서 data를 조회하는 함수

    Returns:
        DataFrame: vw_creditcard_churn_predictions 뷰의 데이터가 담긴 DataFrame
    """

    query = """
    SELECT *
    FROM vw_creditcard_churn_predictions
    """

    conn = get_select_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

        df = DataFrame(rows, columns=columns)

        return df

    finally:
        conn.close()
