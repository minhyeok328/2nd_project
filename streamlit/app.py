"""
=========================================================================
Project:
- Credit Card Customers

Module:
- streamlit

File: app.py

Purpose:
- Streamlit main page

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
- 2026-03-13: 기능 분리 작업 (@nobrain711)
=========================================================================
"""

import streamlit as st

from common.config import APP_TITLE, PAGE_LAYOUT, PAGE_TITLE
from common.session import init_session_state
from common.styles import apply_global_styles
from pages.dashboard import render_dashboard_page
from pages.strategy import render_strategy_page
from pages.eda import render_eda_page


def render_navigation() -> None:
    """
    상단 네비게이션 버튼을 렌더링합니다.
    """
    col_nav1, col_nav2, col_nav3 = st.columns([1, 1, 1])

    with col_nav1:
        if st.button("📊 ANALYSIS DASHBOARD", use_container_width=True):
            st.session_state["page"] = "Dashboard"

    with col_nav2:
        if st.button("💳 STRATEGY REPORT", use_container_width=True):
            st.session_state["page"] = "Strategy"
    
    with col_nav3:
        if st.button("📊 Credit Card Customer EDA", use_container_width=True):
            st.session_state["page"] = "EDA"

def main() -> None:
    """
    Streamlit 앱을 실행합니다.
    """
    st.set_page_config(page_title=PAGE_TITLE, layout=PAGE_LAYOUT)

    init_session_state()
    apply_global_styles()

    render_navigation()

    current_page = st.session_state["page"]

    if current_page == "Dashboard":
        render_dashboard_page()
    elif current_page == "Strategy":
        render_strategy_page()
    elif current_page == 'EDA':
        render_eda_page()

    st.caption(f"© 2026 {APP_TITLE}")


if __name__ == "__main__":
    main()