"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- pipeline/schemas

File: credit_card_churn.py

Purpose:
- file purpose

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
=========================================================================
"""

from pydantic import BaseModel
from typing import Dict, List


class CreditCardChurnAllResponse(BaseModel):
    split: bool
    index: List[int]
    columns: List[str]
    data: List[Dict[str, int | float]]


class CreditCardChurnResponse(BaseModel):
    split: bool
    index: List[int]
    X_columns: List[str]
    x: List[Dict[str, int | float]]
    y: List[int]
