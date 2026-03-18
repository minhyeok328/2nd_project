"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- pipeline/services

File: get_creditcard_churn_dataset.py

Purpose:
- creditcard_churn_all 데이터셋을 조회하여 반환하는 서비스 함수 정의

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
=========================================================================
"""

from pipeline.db.reader.fetch_creditcard_churn_all import fetch_creditcard_churn_all
from pipeline.schemas.credit_card_churn import (
    CreditCardChurnAllResponse,
    CreditCardChurnResponse,
)


def get_creditcard_churn_dataset(
    X_y_split: bool = False,
) -> CreditCardChurnAllResponse | CreditCardChurnResponse:
    """
    creditcard_churn_all 데이터셋 조회 서비스 함수

    :param X_y_split: True인 경우 X와 y를 분리하여 반환
    :return:
    - X_y_split이 False인 경우: CreditCardChurnAllResponse 객체
    - X_y_split이 True인 경우: CreditCardChurnResponse 객체
    """

    if X_y_split:
        X, y, index = fetch_creditcard_churn_all(X_y_split=True)

        return CreditCardChurnResponse(
            split=True,
            index=index.tolist(),
            X_columns=X.columns.tolist(),
            x=X.to_dict(orient="records"),
            y=y.tolist(),
        )

    df = fetch_creditcard_churn_all()

    return CreditCardChurnAllResponse(
        split=False,
        index=df.index.astype(str).tolist(),
        columns=df.columns.tolist(),
        data=df.to_dict(orient="records"),
    )
