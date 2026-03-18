"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common.mlflow

File:
- search_runs_by_experiment.py

Purpose:
- 특정 experiment의 run 목록을 조회합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from typing import List
from mlflow.client import MlflowClient
from mlflow.entities import Run


def search_runs_by_experiment(
    client: MlflowClient,
    experiment_id: str,
    max_results: int = 100
) -> List[Run]:
    """
    experiment의 run을 최신순으로 조회합니다.
    """

    return client.search_runs(
        experiment_ids=[experiment_id],
        order_by=["attributes.start_time DESC"],
        max_results=max_results
    )