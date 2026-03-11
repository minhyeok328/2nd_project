"""
=========================================================================
Project:
- <project-name>

Module:
- pipeline/db

File: config.py

Purpose:
- TODO: Datbase configuration

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
=========================================================================
"""
import pymysql

DB_INSERT_CONFIG = {
    'host': 'mysql',
    'port': 3306,
    'user': 'pipeline_insert_user',
    'password': 'pipeline_insert_pw',
    'database': 'creditcard_churn_db',
    'cursorclass': pymysql.cursors.DictCursor,
}

DB_SELECT_CONFIG = {
    'host': 'mysql',
    'port': 3306,
    'user': 'pipeline_select_user',
    'password': 'pipeline_select_pw',
    'database': 'creditcard_churn_db',
    'cursorclass': pymysql.cursors.DictCursor,
}
