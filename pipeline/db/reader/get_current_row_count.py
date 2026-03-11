"""
=========================================================================
Project:
- Credit Card Customers

Module:
- db reader

File: get_current_row_count.py

Purpose:
- 데이터베이스에서 현재 행 수를 조회하는 함수 정의

Author: 조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (조동휘)
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

    # 데이터베이스 연결을 얻고 행 수 조회 작업 수행
    conn = get_select_connection()
    
    
    # cursor를 사용하여 행 수 조회 실행 및 cursor 자동 닫기 보장
    # -> 추가적으로 예외 처리 및 연결 닫기 보장 로직을 구현할 수 있음
    try:
        # cursor를 사용하여 행 수 조회 실행 및 cursor 자동 닫기 보장
        with conn.cursor() as cursor:
            # 조회 쿼리 실행 -> 현재는 개발단계에서는 임시적으로 구현
            query = f"SELECT COUNT(*) AS count FROM {table_name}"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['count']

    finally:
        conn.close()
