"""
=========================================================================
Project:
- Credit Card Customer Segmentation & Product Strategy

Module:
- reader

File: fetch_creditcard_churn_all.py

Purpose:
- extract 단계에서 creditcard_churn_all 테이블의 모든 데이터를 읽어오는 함수 정의

Author: @nobrain711
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (@nobrain711)
- 2026-03-09: reader package create and view select (@nobrain711)
- 2026-03-10: 프로젝트 명 반영 및 fastAPI 사용 가능하게 수정 (@nobrain711)
=========================================================================
"""

from pandas import DataFrame, Series, Index
from typing import Tuple

from pipeline.db.connection.get_select_connection import get_select_connection
from pipeline.db.config import TARGET_COLUMN, INDEX_COLUMN


def fetch_creditcard_churn_all(
    X_y_split: bool = False,
) -> DataFrame | Tuple[DataFrame, Series, Index]:
    """
    vw_creditcard_churn_ml 전체 조회

    :param X_y_split: True인 경우 X와 y를 분리하여 반환
    :return:
    - X_y_split이 False인 경우: vw_creditcard_churn_ml 전체 데이터프레임
    - X_y_split이 True인 경우: X (특징 데이터프레임), y (타겟 시리즈), index (인덱스) 튜플
    """

    query = """
    SELECT *
    FROM vw_creditcard_churn_ml
    """

    conn = None

    # SQL 쿼리를 실행하여 데이터프레임으로 반환
    # - 추후 에러 핸들링 추가 가능
    try:
        conn = get_select_connection()

        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

        df = DataFrame(rows, columns=columns)

        if X_y_split:
            X = df.drop(columns=[TARGET_COLUMN])
            y = df[TARGET_COLUMN]
            index = df[INDEX_COLUMN]

            return X, y, index
        else:
            return df

    except Exception as exc:
        raise RuntimeError(
            f"vw_creditcard_churn_ml 조회 중 오류가 발생했습니다.\n{exc}"
        ) from exc

        if X_y_split:
            X = df.drop(columns=[TARGET_COLUMN])
            y = df[TARGET_COLUMN]
            index = df[INDEX_COLUMN]

            return X, y, index
        else:
            return df
        
    finally:
        if conn is not None:
            conn.close()
