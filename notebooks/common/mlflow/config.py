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

from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class MlflowConfig:
    """
    MLflow 설정 정보를 담는 데이터 클래스입니다.
    """

    tracking_uri: str
    experiment_name: str


def get_mlflow_config() -> MlflowConfig:
    """
    환경 변수에서 MLflow 설정값을 읽어옵니다.

    Returns:
        MlflowConfig: MLflow 설정 객체
    """
    tracking_uri = getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
    experiment_name = "ccrm_experiment"

    return MlflowConfig(
        tracking_uri=tracking_uri,
        experiment_name=experiment_name,
    )
