"""
=========================================================================
Project:
- <project-name>

Module:
- writer

File: dataframe_to_tuples.py

Purpose:
- pandas DataFrame를 튜플 리스트로 변환하는 함수 정의

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version (조동휘)
- 2026-03-09: writer package create (조동휘)
=========================================================================
"""
from typing import List, Tuple

import pandas as pd

def dataframe_to_tuples(df: pd.DataFrame) -> List[Tuple]:
    """
    convert pandas dataframe to list of tuples

    :param df:
    :return:
    """

    return [tuple(row) for row in df.to_numpy()]