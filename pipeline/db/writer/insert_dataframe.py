"""
=========================================================================
Project:
- Credit Card Customers

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
- 2026-03-10: 프로젝트 명 반영 및 주석 추가 (조동휘)
=========================================================================
"""

# python standard library
import pandas as pd

# 프로젝트 내부 모듈
from pipeline.db.connection.get_insert_connection import get_insert_connection
from .build_insert_query import build_insert_query
from .dataframe_to_tuples import dataframe_to_tuples


def insert_dataframe(table_name: str, df: pd.DataFrame) -> int:
    """
    Insert dataframe into table

    :param table_name: 삽입할 테이블 이름
    :param df: 삽입할 데이터프레임
    :return int: 적재된 행 수
    """

    # 데이터프레임이 비어있는 경우 0 반환
    if df.empty:
        return 0

    # 삽입 쿼리 생성 및 데이터프레임을 튜플 리스트로 변환
    query = build_insert_query(table_name, df.columns.tolist())
    values = dataframe_to_tuples(df)

    # 데이터베이스 연결을 얻고 삽입 작업 수행
    conn = get_insert_connection()

    # 트랜잭션을 사용하여 데이터 삽입 - 성공 시 커밋, 실패 시 롤백
    try:
        # cursor를 사용하여 다중 행 삽입 실행 및 cursor 자동 닫기 보장
        with conn.cursor() as cursor:
            # executemany를 사용하여 여러 행을 한 번에 삽입
            cursor.executemany(query, values)
        
        # 삽입이 성공적으로 완료되면 트랜잭션 커밋
        conn.commit()
        
        # 삽입된 행 수 반환
        return len(values)

    # 오류 발생 시 트랜잭션 롤백 및 예외 재발생
    except Exception:
        # 오류 발생 시 트랜잭션 롤백
        conn.rollback()

        # 예외를 다시 발생시켜 호출자에게 알림
        #  -> 예외를 처리하는 로직이 필요한 경우 이 부분에서 추가할 수 있음
        raise

    # 연결은 항상 닫히도록 보장
    finally:
        conn.close()
