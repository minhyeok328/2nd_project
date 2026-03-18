"""
=========================================================================
Project:
- Credit Card Customers

Module:
- db reader

File: get_current_row_count.py

Purpose:
- 데이터베이스에서 현재 행 수를 조회하는 함수 정의

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
- 2026-03-13: 테이블 조회 로직의 안정성 확보 (@nobrain711)
=========================================================================
"""

# 프로젝트 내부 모듈
from pipeline.db.connection.get_select_connection import get_select_connection

def get_current_row_count(table_name: str) -> int:
    """
    Get current row count from table

    :param table_name: 조회할 테이블 이름
    :return int: 현재 행 수
    """

    # 조회할 테이블 지정
    allowed_tables = {
        "creditcard_churn",
    }

    if table_name not in allowed_tables:
        raise ValueError(f"허용되지 않은 테이블입니다: {table_name}")

    query = f"""
    SELECT COUNT(*) AS count
    FROM `{table_name}`
    """

    # 메모리에 conn을 할당
    conn = None

    # cursor를 사용하여 행 수 조회 실행 및 cursor 자동 닫기 보장
    # -> 추가적으로 예외 처리 및 연결 닫기 보장 로직을 구현할 수 있음
    try:
        # 데이터베이스 연결을 얻고 행 수 조회 작업 수행
        conn = get_select_connection()

        with conn.cursor() as cursor:
            # 조회 쿼리 실행 -> 현재는 개발단계에서는 임시적으로 구현
            cursor.execute(query)
            result = cursor.fetchone()

            return result["count"]

    finally:
        if conn is not None:
            conn.close()