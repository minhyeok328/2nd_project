"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common.mlflow

File:
- load_latest_model_by_name.py

Purpose:
- 모델명 기준 최신 MLflow 모델 artifact를 로드합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
- 2026-03-16: model flavor별 loader 반영 (@nobrain711)
=========================================================================
"""

from __future__ import annotations

from typing import Any

import mlflow
import mlflow.lightgbm
import mlflow.sklearn
import mlflow.xgboost
from mlflow.client import MlflowClient

from common.config import MODEL_ARTIFACT_CANDIDATES, MODEL_NAME_MAP


def _load_model_by_flavor(model_name: str, model_uri: str) -> Any:
    """
    모델명에 맞는 MLflow flavor loader로 모델을 로드합니다.
    """
    if model_name in ["HistGradientBoosting", "Logistic Regression", "EasyEnsemble", "XGBoost"]:
        return mlflow.sklearn.load_model(model_uri)

    if model_name == "LightGBM":
        return mlflow.lightgbm.load_model(model_uri)

    return mlflow.pyfunc.load_model(model_uri)


def load_latest_model_by_name(
    tracking_uri: str,
    experiment_name: str,
    model_name: str,
) -> Any:
    """
    모델명에 해당하는 최신 run을 검색한 뒤,
    artifact path 후보를 순서대로 시도하여 모델을 로드합니다.
    """
    if not tracking_uri:
        raise ValueError("MLFLOW_TRACKING_URI 값이 비어 있습니다.")

    mlflow.set_tracking_uri(tracking_uri)

    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        raise ValueError(f"Experiment를 찾을 수 없습니다: {experiment_name}")

    run_name_map = {
        display_name: run_name
        for run_name, display_name in MODEL_NAME_MAP.items()
    }
    target_run_name = run_name_map.get(model_name, model_name)

    client = MlflowClient(tracking_uri=tracking_uri)

    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        filter_string=(
            f"attributes.status = 'FINISHED' "
            f"AND tags.mlflow.runName = '{target_run_name}'"
        ),
        order_by=["attributes.start_time DESC"],
        max_results=50,
    )

    if not runs:
        raise ValueError(
            f"모델 run을 찾을 수 없습니다: {model_name} "
            f"(target_run_name={target_run_name})"
        )

    artifact_candidates = MODEL_ARTIFACT_CANDIDATES.get(model_name, ["model"])
    debug_logs: list[str] = []

    for run in runs:
        if "mlflow.parentRunId" in run.data.tags:
            continue

        run_id = run.info.run_id

        for artifact_path in artifact_candidates:
            model_uri = f"runs:/{run_id}/{artifact_path}"

            try:
                print(
                    f"[MLflow] try load: model_name={model_name}, "
                    f"run_id={run_id}, artifact_path={artifact_path}"
                )
                model = _load_model_by_flavor(
                    model_name=model_name,
                    model_uri=model_uri,
                )
                print(f"[MLflow] load success: {type(model)}")
                return model
            except Exception as exc:
                debug_logs.append(
                    f"run_id={run_id}, artifact_path={artifact_path}, error={exc}"
                )

    raise ValueError(
        f"{model_name} 최신 run들에서 로드 가능한 모델을 찾지 못했습니다. "
        f"debug={' | '.join(debug_logs[:10])}"
    )