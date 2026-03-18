"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common.mlflow

File:
- extract_run_info.py

Purpose:
- MLflow run 객체를 dict 형태로 변환합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from typing import Dict, Any


def extract_run_info(run_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    MLflow search_runs DataFrame row dict에서 필요한 정보를 추출합니다.
    """
    return {
        "run_id": run_dict.get("run_id"),
        "run_name": run_dict.get("tags.mlflow.runName", ""),
        "model_name": run_dict.get("params.model_name", "unknown_model"),
        "status": run_dict.get("status"),
        "start_time": run_dict.get("start_time"),
        "end_time": run_dict.get("end_time"),
        "artifact_uri": run_dict.get("artifact_uri"),
        "parent_run_id": run_dict.get("tags.mlflow.parentRunId"),
        "is_nested": run_dict.get("tags.mlflow.parentRunId") is not None,
        "metrics": {
            "accuracy": run_dict.get("metrics.accuracy"),
            "precision": run_dict.get("metrics.precision"),
            "recall": run_dict.get("metrics.recall"),
            "f1_score": run_dict.get("metrics.f1_score"),
            "roc_auc": run_dict.get("metrics.roc_auc"),
            "pr_auc": run_dict.get("metrics.pr_auc"),
        },
    }