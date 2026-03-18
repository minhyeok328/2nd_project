"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common.mlflow

File:
- get_mlflow_client.py

Purpose:
- MLflow Tracking Server와 연결된 client를 생성합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

import os
import mlflow
from mlflow.client import MlflowClient


def get_mlflow_client() -> MlflowClient:
    """
    환경변수에서 MLflow Tracking URI를 읽어 client를 생성합니다.
    """

    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")

    if not tracking_uri:
        raise ValueError("MLFLOW_TRACKING_URI 환경변수가 설정되지 않았습니다.")

    mlflow.set_tracking_uri(tracking_uri)

    return MlflowClient(tracking_uri=tracking_uri)