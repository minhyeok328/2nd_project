"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common.mlflow

File:
- group_runs_by_model.py

Purpose:
- run 정보를 model_name 기준으로 그룹화합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from typing import Dict, List, Any


def group_runs_by_model(
    run_info_list: List[Dict[str, Any]]
) -> Dict[str, List[Dict[str, Any]]]:
    """
    run 정보 리스트를 model_name 기준으로 그룹화합니다.
    """

    grouped_runs: Dict[str, List[Dict[str, Any]]] = {}

    for run_info in run_info_list:

        model_name = run_info["model_name"]

        if model_name not in grouped_runs:
            grouped_runs[model_name] = []

        grouped_runs[model_name].append(run_info)

    return grouped_runs