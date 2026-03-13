"""
=========================================================================
Project:
- Credit Card Customers

Module:
- common

File: mlflow_utils.py

Purpose:
- LightGBM 학습 시 MLflow 실험 추적 공통 기능을 제공합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from pathlib import Path
from typing import Any, Optional

import mlflow
import mlflow.lightgbm


MLFLOW_EXPERIMENT_NAME = "ccc_experiment"


def setup_mlflow(tracking_uri: str) -> None:
    """
    MLflow tracking URI와 experiment를 설정합니다.

    Args:
        tracking_uri (str): MLflow 서버 주소
    """
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)


def reset_active_run() -> None:
    """
    현재 활성화된 run이 있으면 종료합니다.
    """
    active_run = mlflow.active_run()
    if active_run is not None:
        mlflow.end_run()


def start_run(run_name: Optional[str] = None) -> Any:
    """
    MLflow run을 시작합니다.

    Args:
        run_name (Optional[str]): run 이름

    Returns:
        Any: MLflow active run 객체
    """
    return mlflow.start_run(run_name=run_name)


def end_run() -> None:
    """
    현재 활성화된 run을 종료합니다.
    """
    mlflow.end_run()


def log_params(params: dict) -> None:
    """
    파라미터를 MLflow에 기록합니다.

    Args:
        params (dict): 파라미터 딕셔너리
    """
    if not params:
        return

    clean_params = {
        str(key): value for key, value in params.items() if value is not None
    }
    mlflow.log_params(clean_params)


def log_metrics(metrics: dict) -> None:
    """
    평가 지표를 MLflow에 기록합니다.

    Args:
        metrics (dict): metric 딕셔너리
    """
    if not metrics:
        return

    clean_metrics = {
        str(key): float(value) for key, value in metrics.items() if value is not None
    }
    mlflow.log_metrics(clean_metrics)


def log_tags(tags: dict) -> None:
    """
    태그를 MLflow에 기록합니다.

    Args:
        tags (dict): tag 딕셔너리
    """
    if not tags:
        return

    clean_tags = {
        str(key): str(value) for key, value in tags.items() if value is not None
    }
    mlflow.set_tags(clean_tags)


def log_lightgbm_model(model: Any, artifact_path: str = "model") -> None:
    """
    LightGBM 모델을 MLflow에 기록합니다.

    Args:
        model (Any): 학습된 LightGBM 모델
        artifact_path (str): artifact 저장 경로
    """
    mlflow.lightgbm.log_model(
        lgb_model=model,
        artifact_path=artifact_path,
    )


def log_artifact(local_path: str, artifact_path: Optional[str] = None) -> None:
    """
    일반 파일 artifact를 MLflow에 기록합니다.

    Args:
        local_path (str): 로컬 파일 경로
        artifact_path (Optional[str]): MLflow 내부 artifact 경로
    """
    path = Path(local_path)

    if not path.exists():
        raise FileNotFoundError(f"파일이 존재하지 않습니다: {local_path}")

    mlflow.log_artifact(str(path), artifact_path=artifact_path)
