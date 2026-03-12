"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common

File: fetch_creditcard.py

Purpose:
- pipeline과 통신하여 creditcard 데이터셋을 가져오는 함수

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
- 2026-03-11: API 예외 처리 추가 및 불필요한 매핑 로직 제거 (@JJonyeok2)
- 2026-03-11: API 응답 검증 및 JSON 예외 처리 추가 (@JJonyeok2)
=========================================================================
"""

# NOTE
# 반환되는 데이터셋에는 `creditcard_churn_id` 컬럼이 포함되어 있습니다.
# 해당 컬럼은 고객 레코드를 식별하기 위한 Primary Key이며 머신러닝 모델의 feature로 사용되지 않습니다.
#
# 따라서 모델 학습 시에는 반드시 feature에서 제외해야 합니다.
#
# 예시)
# df = fetch_creditcard()
# X = df.drop(columns=["creditcard_churn_id", "churn"])
# y = df["churn"]
#
# pipeline API에서 전달되는 `index` 값은 pandas DataFrame의 index로 설정됩니다.
# 이 index는 row ordering을 유지하기 위한 용도이며 모델 feature에는 포함되지 않습니다.
#
# 데이터 구조
# - index                : row identifier
# - creditcard_churn_id  : customer identifier
# - churn                : target variable
# - 나머지 컬럼            : feature


import requests
from pandas import DataFrame, Series
from typing import Tuple, Union


PIPELINE_URL = "http://pipeline:8000/dataset/creditcard-churn"


def fetch_creditcard(X_y_split: bool = False) -> Union[DataFrame, Tuple[DataFrame, Series]]:
    """
    pipeline과 통신하여 이미 수치화된 creditcard 데이터셋을 가져옵니다.

    Args:
        X_y_split (bool, optional):
            데이터셋을 X와 y로 나눌지 여부. Default False

    Returns:
        Union[DataFrame, Tuple[DataFrame, Series]]:
            - False : 전체 DataFrame 반환
            - True  : (X DataFrame, y Series) 반환
    """

    # ---------------------------
    # 1️⃣ API 호출
    # ---------------------------
    try:
        response = requests.get(
            PIPELINE_URL,
            params={"X_y_split": X_y_split},
            timeout=10
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Pipeline API 요청 실패: {e}")

    # ---------------------------
    # 2️⃣ JSON 파싱
    # ---------------------------
    try:
        payload = response.json()
    except ValueError:
        raise RuntimeError("Pipeline API 응답이 JSON 형식이 아닙니다.")

    # ---------------------------
    # 3️⃣ 응답 schema 검증
    # ---------------------------
    if "index" not in payload:
        raise RuntimeError("Pipeline API 응답에 'index'가 없습니다.")

    # ---------------------------
    # 4️⃣ X / y 분리 반환
    # ---------------------------
    if X_y_split:

        if "x" not in payload or "y" not in payload:
            raise RuntimeError("Pipeline API 응답에 'x' 또는 'y'가 없습니다.")

        if len(payload["x"]) != len(payload["y"]):
            raise RuntimeError("X와 y 데이터 길이가 일치하지 않습니다.")

        df = DataFrame(payload["x"], index=payload["index"])
        y = Series(payload["y"], index=payload["index"])

        return df, y

    # ---------------------------
    # 5️⃣ 전체 데이터 반환
    # ---------------------------
    if "data" not in payload:
        raise RuntimeError("Pipeline API 응답에 'data'가 없습니다.")

    return DataFrame(payload["data"], index=payload["index"])