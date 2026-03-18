"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common

File:
- session.py

Purpose:
- Streamlit session_state 초기화를 담당합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
- 2026-03-16: default_state에 model 반영 (@nobrain711)
=========================================================================
"""

from streamlit import session_state

from common.config import MODEL_NAME_LIST


def init_session_state() -> None:
    """
    앱 실행에 필요한 session_state 기본값을 초기화합니다.
    """
    default_state = {
        "page": "Dashboard",
        "res_prob": 0.0,
        "last_model": MODEL_NAME_LIST[0],
        "selected_model": MODEL_NAME_LIST[0],
        "models": {},
    }

    for key, value in default_state.items():
        if key not in session_state:
            session_state[key] = value