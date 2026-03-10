"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- pipeline/router

File: read_creditcard_dataset

Purpose:
- read_creditcard_churn_dataset API 엔드포인트 정의

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
=========================================================================
"""

from fastapi import APIRouter, Query
from typing import Union

from pipeline.schemas.credit_card_churn import (
    CreditCardChurnAllResponse,
    CreditCardChurnResponse,
)
from pipeline.services.get_creditcard_churn_dataset import get_creditcard_churn_dataset

router = APIRouter(prefix="/dataset", tags=["dataset"])


@router.get(
    "/creditcard-churn",
    response_model=Union[CreditCardChurnAllResponse, CreditCardChurnResponse],
    summary="Credit Card Churn Dataset 조회",
    description="creditcard_churn_all 데이터셋을 조회하여 반환하는 API 엔드포인트입니다. X_y_split 쿼리 파라미터에 따라 전체 데이터셋 또는 X와 y로 분리된 데이터셋을 반환합니다.",
)
def read_creditcard_churn_dataset(
    X_y_split: bool = Query(
        default=False,
        description="True인 경우 X와 y를 분리하여 반환. 기본값은 False로 전체 데이터셋 반환",
        examples={
            "split_dataset": {"summary": "X와 y 분리하여 반환", "value": True},
            "full_dataset": {"summary": "전체 데이터셋 반환", "value": False},
        },
    )
) -> Union[CreditCardChurnAllResponse, CreditCardChurnResponse]:
    """
    creditcard churn dataset 조회 API 엔드포인트 함수

    :param X_y_split: True인 경우 X와 y를 분리하여 반환
    :return: - X_y_split이 False인 경우: CreditCardChurnAllResponse 객체
             - X_y_split이 True인 경우: CreditCardChurnResponse 객체
    """
    return get_creditcard_churn_dataset(X_y_split=X_y_split)
