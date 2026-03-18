"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- pipeline/db

File: config.py

Purpose:
- db모듈에서 자주 사용하는 상수 혹은 설정들을 저장하는 파일

Author: @nobrain711
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (@nobrain711)
- 2026-03-10: 
    - 프로젝트 명 반명
    - 작성자 명 github이름으로 변경
    - TARGET_COLUMN, INDEX_COLUMN 추가
    - import 단일로 변경 (@nobrain711)
=========================================================================
"""
from pymysql.cursors import DictCursor

DB_INSERT_CONFIG = {
    'host': 'mysql',
    'port': 3306,
    'user': 'pipeline_insert_user',
    'password': 'pipeline_insert_pw',
    'database': 'creditcard_churn_db',
    'cursorclass': DictCursor,
}

DB_SELECT_CONFIG = {
    'host': 'mysql',
    'port': 3306,
    'user': 'pipeline_select_user',
    'password': 'pipeline_select_pw',
    'database': 'creditcard_churn_db',
    'cursorclass': DictCursor,
}

TARGET_COLUMN = "churn"

INDEX_COLUMN = "creditcard_churn_id"