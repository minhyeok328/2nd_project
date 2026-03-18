"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- utils

File:
- data_loader.py

Purpose:
- Streamlit 화면에서 사용하는 데이터 로드 기능을 제공합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
- 2026-03-15: MLflow leaderboard 연동 (@nobrain711)
=========================================================================
"""

from typing import Dict, List

from pandas import DataFrame

from common.config import (
    MLFLOW_EXPERIMENT_NAME,
    MLFLOW_TRACKING_URI,
    MODEL_NAME_MAP,
)
from common.fetch_creditcard import fetch_creditcard
from common.mlflow.load_latest_scores_by_model import load_latest_scores_by_model


def get_feature_columns() -> list[str]:
    """
    예측 입력에 사용할 feature 컬럼 순서를 반환합니다.
    """
    df = fetch_creditcard(X_y_split=False)

    excluded_columns = ["creditcard_churn_id", "churn"]
    feature_columns = [col for col in df.columns if col not in excluded_columns]

    return feature_columns


def get_leaderboard_data() -> DataFrame:
    """
    MLflow에서 최신 모델 리더보드 데이터를 조회하여 반환합니다.
    """
    latest_scores = load_latest_scores_by_model(
        tracking_uri=MLFLOW_TRACKING_URI,
        experiment_name=MLFLOW_EXPERIMENT_NAME,
    )

    rows = []
    for run_name, run_info in latest_scores.items():
        metrics = run_info.get("metrics", {})

        rows.append(
            {
                "모델명(Model)": MODEL_NAME_MAP.get(run_name, run_name),
                "정확도(Acc)": metrics.get("accuracy"),
                "정밀도(Precision)": metrics.get("precision"),
                "재현율(Recall)": metrics.get("recall"),
                "ROC-AUC": metrics.get("roc_auc"),
                "PR-AUC": metrics.get("pr_auc"),
                "F1-score": metrics.get("f1_score"),
            }
        )

    leaderboard_data = DataFrame(rows)

    if leaderboard_data.empty:
        return leaderboard_data

    return leaderboard_data.sort_values(
        by="ROC-AUC",
        ascending=False,
    ).reset_index(drop=True)


def get_impact_data(model_name: str) -> DataFrame:
    """
    모델별 feature 영향력 예시 데이터를 반환합니다.
    """
    impact_map = {
        "HistGradientBoosting": {
            "feature": ["총 결제 금액", "소득 구간", "총 결제 횟수", "한도 소진율", "리볼빙 잔액"],
            "영향력": [0.55, 0.45, 0.38, 0.25, 0.18],
        },
        "XGBoost": {
            "feature": ["총 결제 금액", "총 결제 횟수", "리볼빙 잔액", "소득 구간", "비활성 기간"],
            "영향력": [0.51, 0.43, 0.34, 0.29, 0.21],
        },
        "EasyEnsemble": {
            "feature": ["리볼빙 잔액", "비활성 기간", "고객센터 상담 횟수", "총 결제 금액", "총 결제 횟수"],
            "영향력": [0.49, 0.42, 0.36, 0.28, 0.24],
        },
        "Logistic Regression": {
            "feature": ["총 결제 금액", "한도 소진율", "리볼빙 잔액", "소득 구간", "총 결제 횟수"],
            "영향력": [0.41, 0.35, 0.31, 0.24, 0.19],
        },
        "LightGBM": {
            "feature": ["총 결제 금액", "총 결제 횟수", "소득 구간", "한도 소진율", "리볼빙 잔액"],
            "영향력": [0.53, 0.44, 0.33, 0.27, 0.22],
        },
    }

    selected = impact_map.get(
        model_name,
        {
            "feature": ["총 결제 금액", "소득 구간", "총 결제 횟수", "한도 소진율", "리볼빙 잔액"],
            "영향력": [0.55, 0.45, 0.38, 0.25, 0.18],
        },
    )

    return DataFrame(selected).sort_values(by="영향력")

def get_model_guides() -> Dict[str, List[str]]:
    """
    모델별 전략 가이드 데이터를 반환합니다.
    """
    return {
        "HistGradientBoosting": [
            "대용량 데이터 미세 패턴 포착",
            "과적합 위험(Noise)",
            "Random Forest 교차 타겟팅",
        ],
        "XGBoost": [
            "정확도/재현율 밸런스 에이스",
            "복잡한 비선형 해석 난해",
            "Logistic Regression 보조 활용",
        ],
        "EasyEnsemble": [
            "이탈자 전수 탐지(Recall 중심)",
            "마케팅 비용 낭비 우려",
            "LightGBM 기반 예산 효율화",
        ],
        "Random Forest": [
            "안정적인 일반화 성능",
            "정교한 신호 탐지 한계",
            "HistGBM 모델 고도화 추천",
        ],
        "LightGBM": [
            "실시간 오퍼 최적화 속도",
            "소량 데이터 취약성",
            "XGBoost와 상호 보완",
        ],
        "Logistic Regression": [
            "명확한 원인 설명력",
            "비선형 관계 포착 한계",
            "앙상블 모델 병행 사용",
        ],
    }