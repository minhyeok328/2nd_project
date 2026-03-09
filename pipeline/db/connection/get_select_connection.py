"""
=========================================================================
Project:
- <project-name>

Module:
- connection

File: get_select_connection.py

Purpose:
- 데이터 베이스 select 작업을 위한 connection 객체를 반환하는 함수 정의

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
- 2026-03-09: connection package create (조동휘)
=========================================================================
"""
import pymysql
from pipeline.db.config import DB_SELECT_CONFIG

def get_select_connection():
    """connection for read operations"""
    return pymysql.connect(**DB_SELECT_CONFIG)