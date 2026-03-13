"""
=========================================================================
Project:
- Credit Card Customers

Module:
- common.mlflow

File: artifact_logger.py

Purpose:
- MLflow 일반 artifact 저장을 담당합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from pathlib import Path
from typing import Optional

import mlflow


def log_artifact(local_path: str, artifact_path: Optional[str] = None) -> None:
    """
    단일 파일 artifact를 기록합니다.

    Args:
        local_path (str): 로컬 파일 경로
        artifact_path (Optional[str]): MLflow 내부 저장 경로
    """
    path = Path(local_path)

    if not path.exists():
        raise FileNotFoundError(f"artifact 파일이 존재하지 않습니다: {local_path}")

    mlflow.log_artifact(local_path=str(path), artifact_path=artifact_path)
