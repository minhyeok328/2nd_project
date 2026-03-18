"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- utils

File:
- prediction.py

Purpose:
- MLflow 모델 기반 이탈 예측 로직을 제공합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
- 2026-03-16: 모델별 입력 전처리 및 예측 확률 반환 구조 반영 (@nobrain711)
=========================================================================
"""

from __future__ import annotations

from typing import Any

import pandas as pd
from pandas import DataFrame
from streamlit import session_state

from common.config import (
    MLFLOW_EXPERIMENT_NAME,
    MLFLOW_TRACKING_URI,
    MODEL_NAME_LIST,
)
from common.mlflow.load_latest_model_by_name import load_latest_model_by_name


CATEGORICAL_COLUMNS = [
    "gender",
    "education_id",
    "marital_id",
    "income_id",
    "card_type_id",
]

MODEL_REQUIRED_COLUMNS = {
    "HistGradientBoosting": [
        "age",
        "gender",
        "dependents",
        "education_id",
        "marital_id",
        "income_id",
        "card_type_id",
        "relationship_months",
        "product_count",
        "inactive_months",
        "contact_count",
        "credit_limit",
        "revolving_balance",
        "available_credit",
        "amount_change",
        "count_change",
        "transaction_amount",
        "transaction_count",
        "utilization_ratio",
    ],
    "LightGBM": [
        "age",
        "gender",
        "dependents",
        "education_id",
        "marital_id",
        "income_id",
        "card_type_id",
        "relationship_months",
        "product_count",
        "inactive_months",
        "contact_count",
        "credit_limit",
        "revolving_balance",
        "available_credit",
        "amount_change",
        "count_change",
        "transaction_amount",
        "transaction_count",
        "utilization_ratio",
    ],
    "XGBoost": [
        "creditcard_churn_id",
        "age",
        "gender",
        "dependents",
        "education_id",
        "marital_id",
        "income_id",
        "card_type_id",
        "relationship_months",
        "product_count",
        "inactive_months",
        "contact_count",
        "credit_limit",
        "revolving_balance",
        "available_credit",
        "amount_change",
        "count_change",
        "transaction_amount",
        "transaction_count",
        "utilization_ratio",
    ],
    "Logistic Regression": [
        "age",
        "gender",
        "dependents",
        "education_id",
        "marital_id",
        "income_id",
        "card_type_id",
        "relationship_months",
        "product_count",
        "inactive_months",
        "contact_count",
        "credit_limit",
        "revolving_balance",
        "available_credit",
        "amount_change",
        "count_change",
        "transaction_amount",
        "transaction_count",
        "utilization_ratio",
    ],
    "EasyEnsemble": [
        "age",
        "gender",
        "dependents",
        "education_id",
        "marital_id",
        "income_id",
        "card_type_id",
        "relationship_months",
        "product_count",
        "inactive_months",
        "contact_count",
        "credit_limit",
        "revolving_balance",
        "available_credit",
        "amount_change",
        "count_change",
        "transaction_amount",
        "transaction_count",
        "utilization_ratio",
    ],
}


def _get_or_load_model(model_name: str) -> Any:
    """
    세션에 캐시된 모델을 재사용하거나 MLflow에서 로드합니다.
    """
    if "models" not in session_state:
        session_state["models"] = {}

    if model_name not in session_state["models"]:
        model = load_latest_model_by_name(
            tracking_uri=MLFLOW_TRACKING_URI,
            experiment_name=MLFLOW_EXPERIMENT_NAME,
            model_name=model_name,
        )
        session_state["models"][model_name] = model

    return session_state["models"][model_name]


def preprocess_for_prediction(
    input_df: DataFrame,
    model_name: str,
) -> DataFrame:
    """
    모델별 예측 입력 컬럼과 dtype을 맞춥니다.
    """
    if model_name not in MODEL_REQUIRED_COLUMNS:
        raise ValueError(f"지원하지 않는 모델입니다: {model_name}")

    df = input_df.copy()
    required_columns = MODEL_REQUIRED_COLUMNS[model_name]

    for column in required_columns:
        if column not in df.columns:
            df[column] = 0

    df = df[required_columns]

    for column in CATEGORICAL_COLUMNS:
        if column in df.columns:
            df[column] = df[column].astype("category")

    return df


def _extract_probability_from_predict_output(prediction: Any) -> float:
    """
    predict() 출력에서 확률처럼 해석 가능한 값을 추출합니다.
    fallback 용도입니다.
    """
    if isinstance(prediction, pd.DataFrame):
        if prediction.empty:
            raise ValueError("예측 결과가 비어 있습니다.")

        first_row = prediction.iloc[0]

        for column in ["probability", "proba", "score", "prediction"]:
            if column in prediction.columns:
                return float(first_row[column])

        if len(first_row) >= 2:
            return float(first_row.iloc[1])

        return float(first_row.iloc[0])

    if isinstance(prediction, pd.Series):
        return float(prediction.iloc[0])

    if hasattr(prediction, "__len__") and not isinstance(prediction, (str, bytes)):
        if len(prediction) == 0:
            raise ValueError("예측 결과가 비어 있습니다.")

        first_item = prediction[0]

        if hasattr(first_item, "__len__") and not isinstance(first_item, (str, bytes)):
            if len(first_item) >= 2:
                return float(first_item[1])
            return float(first_item[0])

        return float(first_item)

    return float(prediction)


def _predict_probability(model: Any, prepared_df: DataFrame) -> float:
    """
    모델에서 churn 확률(class 1)을 반환합니다.
    """
    print("model type:", type(model))
    print("has predict_proba:", hasattr(model, "predict_proba"))
    print("prepared_df columns:", prepared_df.columns.tolist())
    print("prepared_df dtypes:")
    print(prepared_df.dtypes)

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(prepared_df)
        print("predict_proba raw:", probability)
        return float(probability[0][0])

    prediction = model.predict(prepared_df)
    print("predict raw:", prediction)

    probability = _extract_probability_from_predict_output(prediction)

    if probability < 0.0:
        return 0.0
    if probability > 1.0:
        return 1.0

    return probability


def predict_churn_logic(model_name: str, input_df: DataFrame) -> float:
    """
    입력 DataFrame을 받아 churn 확률(class 1 probability)을 반환합니다.
    """
    if model_name not in MODEL_NAME_LIST:
        raise ValueError(f"지원하지 않는 모델입니다: {model_name}")

    model = _get_or_load_model(model_name)
    prepared_df = preprocess_for_prediction(
        input_df=input_df,
        model_name=model_name,
    )

    return _predict_probability(model=model, prepared_df=prepared_df)