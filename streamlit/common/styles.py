"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common

File:
- styles.py

Purpose:
- Streamlit 앱의 공통 CSS 및 JS 스타일을 적용합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

# steamlit markdown function
from streamlit import markdown


def apply_global_styles() -> None:
    """
    전역 CSS 및 JS 스타일을 적용합니다.
    """
    markdown(
        """
        <script>
            const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
            if (sidebar) { sidebar.style.display = 'none'; }
        </script>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

        .main {
            background: radial-gradient(circle at top right, #1e293b, #0f172a);
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            scroll-behavior: smooth;
        }

        .dashboard-card {
            padding: 30px;
            border-radius: 28px;
            margin-bottom: 25px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(12px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            transition: transform 0.3s ease;
        }

        .top-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 55px;
            height: 55px;
            background: rgba(75, 108, 183, 0.2);
            backdrop-filter: blur(10px);
            color: white !important;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            font-weight: 900;
            z-index: 9999;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .section-tag {
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-bottom: 15px;
            color: #94a3b8;
        }

        .highlight-gold {
            color: #fde047;
            font-weight: 700;
            text-shadow: 0 0 10px rgba(253, 224, 71, 0.3);
        }
        </style>

        <div id="top"></div>
        <a href="#top" class="top-btn">▲</a>
        """,
        unsafe_allow_html=True,
    )