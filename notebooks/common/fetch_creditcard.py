"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common

File: fetch_creditcard.py

Purpose:
- pipeline이랑 통신해서 creditcard 데이터셋을 가져오는 함수

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
- 2026-03-16: 호출부 관련 에러 수정 (@nobrain711)
=========================================================================
"""
import requests
from pandas import DataFrame, Series 
from typing import Tuple

from common.config import PIPELINE_DATASET_URL

def fetch_creditcard(X_y_split: bool = False
                     ) -> DataFrame | Tuple[DataFrame, Series]:
    """
    fetch_creditcard 함수는 pipeline과 통신하여 creditcard 데이터셋을 가져오는 함수입니다.

    Args:
        X_y_split (bool, optional): 데이터셋을 X와 y로 나눌지 여부. Defaults to False.

    Returns:
        DataFrame | Tuple[DataFrame, Series]: X_y_split이 False인 경우 DataFrame, True인 경우 (DataFrame, Series) 형태로 반환
    """
    response = requests.get(PIPELINE_DATASET_URL, params={"X_y_split": X_y_split})
    payload = response.json()
    
    if X_y_split:
        X = DataFrame(payload["x"], index=payload["index"])
        y = Series(payload["y"], index=payload["index"])
        return X, y
    
    df = DataFrame(payload["data"], index=payload["index"])
    
    return df
