"""
=========================================================================
Project:
- <project-name>

Module:
- writer

File: build_insert_query.py

Purpose:
- insert 작업을 위한 SQL 쿼리를 생성하는 함수 정의

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
- 2026-03-09: writer package create (조동휘)
=========================================================================
"""
from typing import List


def build_insert_query(table_name: str, columns: List[str]) -> str:
    """
    build INSERT query

    :param table_name:
    :param columns:
    :return:
    """

    cols = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(columns))

    return f"""
        INSERT INTO {table_name} 
        ({cols}) 
        VALUES ({placeholders})
    """.strip()