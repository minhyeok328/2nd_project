"""
=========================================================================
Project:
- project-name

Module:
- test

File: vw_creditcard_churn_predictions.py

Purpose:
- fetch_creditcard_churn_predictions 뷰의 데이터를 테스트하는 모듈

Author: @조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@조동휘)
=========================================================================
"""

import pandas as pd

from pipeline.db.reader.fetch_creditcard_churn_preditctions import (
    fetch_creditcard_churn_predictions,
)

def test_fetch_creditcard_churn_predictions() -> None:
    """
    fetch_creditcard_churn_predictions 함수의 테스트 함수

    :return: None
    """

    df = fetch_creditcard_churn_predictions()

    # DataFerame 타입 확인
    assert isinstance(
        df, pd.DataFrame
    ), "fetch_creditcard_churn_predictions 함수는 pandas DataFrame을 반환해야 합니다."

    # 최소 칼럼 존재 여부 확인
    assert (
        len(df.columns) > 0
    ), "fetch_creditcard_churn_predictions 함수는 적어도 하나 이상의 칼럼을 반환해야 합니다."

    # 데이터가 존재하는지 확인
    assert (
        len(df) > 0
    ), "fetch_creditcard_churn_predictions 함수는 적어도 하나 이상의 행을 반환해야 합니다."

    print("fetch_creditcard_churn_predictions 함수 테스트 통과!")
    print(f"row count: {len(df)}")
    print(f"columns: {df.columns.tolist()}")
    print(df.head())
    
if __name__ == "__main__":
    test_fetch_creditcard_churn_predictions()