"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common

File:
- config.py

Purpose:
- Streamlit 앱 전역 설정 상수를 관리합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
- 2026-03-14: MLflow 상수 추가 (@nobrain711)
=========================================================================
"""

from os import getenv

MLFLOW_TRACKING_URI = getenv("MLFLOW_TRACKING_URI")
MLFLOW_EXPERIMENT_NAME = "ccrm_experiment"

# steamlit에서 사용하는 상수들
PAGE_TITLE = "CRM | Churn AI"
PAGE_LAYOUT = "wide"
APP_TITLE = "JJonyeok2 | Team EXODIA"
