"""
=========================================================================
Project:
- Credit Card Customers

Module:
- common.mlflow

File: run_manager.py

Purpose:
- MLflow run lifecycle을 관리합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from contextlib import contextmanager
from typing import Dict, Generator, Optional

import mlflow

from .config import get_mlflow_config


def setup_mlflow() -> None:
    """
    MLflow tracking URI와 experiment를 설정합니다.
    """
    config = get_mlflow_config()
    mlflow.set_tracking_uri(config.tracking_uri)
    mlflow.set_experiment(config.experiment_name)


def reset_active_run() -> None:
    """
    현재 활성화된 run이 있다면 종료합니다.
    """
    active_run = mlflow.active_run()
    if active_run is not None:
        mlflow.end_run()


def start_run(
    run_name: Optional[str] = None,
    nested: bool = False,
    tags: Optional[Dict[str, str]] = None,
):
    """
    MLflow run을 시작합니다.

    Args:
        run_name (Optional[str]): run 이름
        nested (bool): nested run 여부
        tags (Optional[Dict[str, str]]): run 시작 시 설정할 태그

    Returns:
        ActiveRun: MLflow active run 객체
    """
    setup_mlflow()
    run = mlflow.start_run(run_name=run_name, nested=nested)

    if tags:
        mlflow.set_tags(tags)

    return run


def end_run() -> None:
    """
    현재 활성화된 run을 종료합니다.
    """
    mlflow.end_run()


@contextmanager
def start_run_context(
    run_name: Optional[str] = None,
    nested: bool = False,
    tags: Optional[Dict[str, str]] = None,
) -> Generator:
    """
    MLflow run을 context manager 형태로 시작하고 자동 종료합니다.

    Args:
        run_name (Optional[str]): run 이름
        nested (bool): nested run 여부
        tags (Optional[Dict[str, str]]): 태그 정보

    Yields:
        ActiveRun: MLflow active run 객체
    """
    setup_mlflow()

    with mlflow.start_run(run_name=run_name, nested=nested) as run:
        if tags:
            mlflow.set_tags(tags)
        yield run
