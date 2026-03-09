"""
=========================================================================
Project:
- <project-name>

Module:
- writer

File: insert_dataframe.py

Purpose:
- pandas DataFrame를 데이터베이스 테이블에 삽입하는 함수 정의

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
- 2026-03-09: writer package create (조동휘)
=========================================================================
"""

import pandas as pd

from pipeline.db.connection.get_insert_connection import get_insert_connection
from .build_insert_query import build_insert_query
from .dataframe_to_tuples import dataframe_to_tuples


def insert_dataframe(table_name: str, df: pd.DataFrame) -> int:
    """
    Insert dataframe into table

    :param table_name:
    :param df:
    :return:
    """

    if df.empty:
        return 0

    query = build_insert_query(table_name, df.columns.tolist())
    values = dataframe_to_tuples(df)

    conn = get_insert_connection()

    try:
        with conn.cursor() as cursor:
            cursor.executemany(query, values)

        conn.commit()

        return len(values)

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()
