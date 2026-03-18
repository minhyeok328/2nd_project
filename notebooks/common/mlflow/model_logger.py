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
import mlflow.sklearn
import mlflow.xgboost
import mlflow.lightgbm
import mlflow.pyfunc  # 추가
from typing import Any, Optional

def log_model(
    model: Any,
    model_type: str,
    artifact_path: str = "model",
    input_example: Optional[Any] = None,
) -> None:
    match model_type:
        case "sklearn":
            # imblearn 모델 등 sklearn 호환 모델을 더 범용적으로 기록
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path=artifact_path,
                input_example=input_example,
                # 필요시 serialization_format="cloudpickle" 등을 고려할 수 있음
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
            
        # [긴급 추가] 만약 위 방법들이 다 안되면 최후의 보루
        case "pyfunc":
            mlflow.pyfunc.log_model(
                python_model=model,
                artifact_path=artifact_path,
            )

        case _:
            raise ValueError(f"지원하지 않는 model_type 입니다: {model_type}")