"""
=========================================================================
Project:
- Credit Card Customers

Module:
- common.mlflow

File: logger.py

Purpose:
- MLflow params / metrics / tags 로깅을 담당합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from typing import Any, Dict, Mapping, Optional

import mlflow


def log_params(params: Mapping[str, Any]) -> None:
    """
    파라미터들을 MLflow에 기록합니다.

    Args:
        params (Mapping[str, Any]): 기록할 파라미터 딕셔너리
    """
    if not params:
        return

    clean_params = {
        str(key): value for key, value in params.items() if value is not None
    }
    mlflow.log_params(clean_params)


def log_metrics(
    metrics: Mapping[str, Any],
    step: Optional[int] = None,
) -> None:
    """
    평가지표들을 MLflow에 기록합니다.

    Args:
        metrics (Mapping[str, Any]): 기록할 metric 딕셔너리
        step (Optional[int]): step 정보
    """
    if not metrics:
        return

    clean_metrics: Dict[str, float] = {
        str(key): float(value) for key, value in metrics.items() if value is not None
    }

    if step is None:
        mlflow.log_metrics(clean_metrics)
        return

    for key, value in clean_metrics.items():
        mlflow.log_metric(key=key, value=value, step=step)


def log_tags(tags: Mapping[str, Any]) -> None:
    """
    태그들을 MLflow에 기록합니다.

    Args:
        tags (Mapping[str, Any]): 기록할 tag 딕셔너리
    """
    if not tags:
        return

    clean_tags = {
        str(key): str(value) for key, value in tags.items() if value is not None
    }
    mlflow.set_tags(clean_tags)
