"""
=========================================================================
Project:
- Credit Card Customers

Module:
- common.mlflow

File: model_logger.py

Purpose:
- MLflow model artifact 저장을 담당합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from typing import Any, Optional

import mlflow.sklearn
import mlflow.xgboost
import mlflow.lightgbm

def log_model(
    model: Any,
    model_type: str,
    artifact_path: str = "model",
    input_example: Optional[Any] = None,
) -> None:
    """
    모델 타입에 맞게 MLflow에 모델을 기록합니다.

    Args:
        model (Any): 학습된 모델 객체
        model_type (str): 모델 타입
            - "sklearn"
            - "lightgbm"
            - "xgboost"
        artifact_path (str): artifact 저장 경로
        input_example (Optional[Any]): 입력 예시 데이터
    """
    match model_type:
        case "sklearn":
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path=artifact_path,
                input_example=input_example,
            )

        case "lightgbm":
            mlflow.lightgbm.log_model(
                lgb_model=model,
                artifact_path=artifact_path,
                input_example=input_example,
            )

        case "xgboost":
            mlflow.xgboost.log_model(
                xgb_model=model,
                artifact_path=artifact_path,
                input_example=input_example,
            )

        case _:
            raise ValueError(f"지원하지 않는 model_type 입니다: {model_type}")
