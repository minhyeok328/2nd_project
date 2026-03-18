"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common.mlflow

File:
- load_latest_scores_by_model.py

Purpose:
- MLflow에서 모델별 최신 훈련 점수를 조회합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from typing import Dict, Any

import mlflow

from .extract_run_info import extract_run_info
from .filter_display_runs import filter_display_runs


def load_latest_scores_by_model(
    tracking_uri: str,
    experiment_name: str,
) -> Dict[str, Dict[str, Any]]:
    """
    MLflow에서 Streamlit 모델 비교용 최신 대표 run 점수를 조회합니다.
    """
    mlflow.set_tracking_uri(tracking_uri)

    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        raise ValueError(f"Experiment를 찾을 수 없습니다: {experiment_name}")

    runs_df = mlflow.search_runs(
        experiment_ids=[experiment.experiment_id],
        output_format="pandas",
    )

    if runs_df.empty:
        return {}

    run_info_list = []
    for _, row in runs_df.iterrows():
        run_dict = row.to_dict()
        run_info = extract_run_info(run_dict)
        run_info_list.append(run_info)

    display_runs = filter_display_runs(run_info_list)

    return {
        run_info["run_name"]: run_info
        for run_info in display_runs
    }