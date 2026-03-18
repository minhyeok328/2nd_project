"""
=========================================================================
Project:
- Credit Card Customers

Module:
- common.mlflow

File: config.py

Purpose:
- MLflow tracking 설정값을 관리합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""
# common/mlflow/config.py

from dataclasses import dataclass
from os import getenv

@dataclass(frozen=True)
class MlflowConfig:
    tracking_uri: str
    experiment_name: str

def get_mlflow_config() -> MlflowConfig:
    """
    환경 변수에서 MLflow 설정값을 읽어옵니다.
    """
    # .strip()을 추가해서 혹시 모를 공백 문제를 원천 차단합니다.
    tracking_uri = getenv("MLFLOW_TRACKING_URI", "localhost:15000").strip()
    
    # 실험 이름도 환경 변수에서 읽어오도록 개선
    experiment_name = getenv("MLFLOW_EXPERIMENT_NAME", "ccrm_experiment").strip()

    return MlflowConfig(
        tracking_uri=tracking_uri,
        experiment_name=experiment_name,
    )