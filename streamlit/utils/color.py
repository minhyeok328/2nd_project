"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- utils

File:
- color.py

Purpose:
- 이탈 확률 시각화를 위한 색상 계산 기능을 제공합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""


def get_gradient_color(prob: float) -> str:
    """
    확률값에 따라 RGB 그라데이션 색상을 반환합니다.

    Args:
        prob: 0~1 사이 확률값

    Returns:
        str: CSS rgb 형식 문자열
    """
    if prob < 0.5:
        r = 255
        g = int(75 + (prob * 2 * 125))
        b = int(75 - (prob * 2 * 25))
    else:
        ratio = (prob - 0.5) * 2
        r = int(255 - (ratio * 180))
        g = int(200 - (ratio * 92))
        b = int(50 + (ratio * 133))

    return f"rgb({r}, {g}, {b})"