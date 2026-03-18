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

MODEL_NAME_MAP = {
    "hist_gradient_boosting": "HistGradientBoosting",
    "xgboost_random_grid_search": "XGBoost",
    "easy_ensemble_baseline": "EasyEnsemble",
    "logistic_regression_baseline": "Logistic Regression",
    "lightgbm_baseline": "LightGBM",
}
MODEL_NAME_LIST = list(MODEL_NAME_MAP.values())

MODEL_ARTIFACT_CANDIDATES = {
    "HistGradientBoosting": ["hist_gradient_boosting", "histgradientboosting", "model"],
    "XGBoost": ["xgboost", "xgb_model", "model"],
    "LightGBM": ["lightgbm", "lightgbm_model", "model"],
    "Logistic Regression": ["logistic_regression", "logistic_regression_model", "model"],
    "EasyEnsemble": ["easy_ensemble", "easy_ensemble_model", "model"],
}


# pipeline url
PIPELINE_BASE_URL = getenv("PIPELINE_API_BASE_URL")
if not PIPELINE_BASE_URL:
    raise RuntimeError("환경변수 'PIPELINE_API_BASE_URL'가 설정되지 않았습니다.")

PIPELINE_DATASET_URL = f"{PIPELINE_BASE_URL}/dataset/creditcard-churn"


# steamlit에서 사용하는 상수들
PAGE_TITLE = "CRM | Churn AI"
PAGE_LAYOUT = "wide"
APP_TITLE = "JJonyeok2 | Team EXODIA"

