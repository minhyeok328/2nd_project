"""
=========================================================================
Project:
- Credit Card Customers

Module:
- pipeline

File: run_etl.py

Purpose:
- container for running the entire ETL process

Author: 조동휘
Created: 2026-03-09

Updated:
- 2026-03-09: initial version (조동휘)
- 2026-03-09: pipeline db 패키지의 내부 모듈화 작업 반영 (조동휘)
- 2026-03-09: ETL 라인 시동 시 중복 적재 방지 작업 및 프로젝트 명 반영 (조동휘)
=========================================================================
"""

# python standard library
import pandas as pd

# 프로젝트 내부 모듈
from pipeline.db.writer.insert_dataframe import insert_dataframe
from pipeline.db.reader.get_current_row_count import get_current_row_count
from pipeline.etl import load_csv
from pipeline.etl import standardize_customer_columns

# Phase 1에서는 임시 중복 방지 로직
# Phase 2에서는 load_tag 또는 seed_history와 같은 변경 사항 감지 로직으로 개선 예정
BASE_ROW_COUNT = 100 # DB에 이미 존재하는 행 수
SEED_ROW_COUNT = 10127 # CSV 파일에서 로드된 행 수
EXPECTED_ROW_COUNT = BASE_ROW_COUNT + SEED_ROW_COUNT # 전체 행 수


def run_etl() -> int:
    """
    docker compose up 시 pipeline 컨테이너에서 실행되는 ETL 라인
    임시적으로 CSV 파일에서 데이터를 로드하여 데이터베이스에 삽입하는 작업을 수행
        - 현재 개발 단계에서는 Table의 row를 구해서 row 수가 예상되는 전체 행 수보다 작은 경우에만 삽입 작업을 수행하도록 구현
        - 향후에는 데이터 변경 사항을 감지하여 변경된 데이터만 삽입하는 방식으로 개선할 예정

    :return int: 삽입된 행 수
    """

    df = load_csv()
    df = standardize_customer_columns(df)
    
    current_row_count = get_current_row_count("creditcard_churn")
    
    if current_row_count >= EXPECTED_ROW_COUNT:
        print(f"Current row count ({current_row_count}) is greater than or equal to expected row count ({EXPECTED_ROW_COUNT}). Skipping data insertion.")
        return 0

    insert_count = insert_dataframe("creditcard_churn", df)

    print(f"Inserted {insert_count} rows into the database.")

    return insert_count


if __name__ == "__main__":
    run_etl()
