"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common.mlflow

File:
- get_latest_run_by_model.py

Purpose:
- 모델별 최신 run을 선택합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from typing import Dict, List, Any


def get_latest_run_by_model(
    grouped_runs: Dict[str, List[Dict[str, Any]]]
) -> Dict[str, Dict[str, Any]]:
    """
    모델별 최신 run 1개를 반환합니다.
    """

    latest_runs: Dict[str, Dict[str, Any]] = {}

    for model_name, run_list in grouped_runs.items():

        if run_list:
            latest_runs[model_name] = run_list[0]

    return latest_runs