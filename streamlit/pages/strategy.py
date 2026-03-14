"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- pages

File:
- strategy.py

Purpose:
- Strategy 페이지 렌더링을 담당합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from streamlit import title, markdown, session_state, columns

from utils.data_loader import get_leaderboard_data, get_model_guides


def render_strategy_page() -> None:
    """
    Strategy 페이지를 렌더링합니다.
    """
    leaderboard_data = get_leaderboard_data()
    model_guides = get_model_guides()

    title("Strategy Report")

    current_model = session_state.get(
        "last_model",
        leaderboard_data["모델명(Model)"].iloc[0],
    )

    markdown(
        f"""
        <div class="dashboard-card">
            <div class="section-tag">STRATEGIC-DECISION-SUPPORT</div>
            <h2 style="margin: 0; font-weight: 900; color: white;">{current_model} 기반 대응 전략</h2>
            <p style="margin-top: 15px; color: #cbd5e1; font-size: 16px;">
                최근 분석된 모델의 특성을 기반으로 최적의 CRM 가이드를 제시합니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    guide_strength, guide_weakness, guide_recommendation = model_guides.get(
        current_model,
        ["데이터 기반 분석", "모델 고유 특성 고려", "맞춤형 오퍼 제안"],
    )

    markdown(
        f"""
        <div class="dashboard-card">
            <h3 style="color:white; font-weight:900;">{current_model} 분석 리포트</h3>
            <div style="margin-top: 25px; line-height:1.8;">
                <p style="color: #cbd5e1;">💪🏼 <b>강점(Strength):</b> {guide_strength}</p>
                <p style="color: #cbd5e1;">⚠️ <b>보완점(Weakness):</b> {guide_weakness}</p>
                <div style="background: rgba(34, 139, 230, 0.1); padding: 25px; border-radius: 20px; border: 1px solid rgba(34, 139, 230, 0.3); margin-top: 20px;">
                    <strong style="color:#7dd3fc; font-size:18px;">💡 비즈니스 추천(Recommendation):</strong><br>
                    <span style="color: white; opacity: 0.9;">{guide_recommendation}</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = columns(2)

    with col1:
        markdown(
            """
            <div class="dashboard-card">
                <h3 style="color:white;">핵심 리텐션 타겟</h3>
                <ul style="color:#cbd5e1;line-height:1.8;">
                    <li>VIP 고액 결제 이탈 위험군</li>
                    <li>최근 3개월 사용 빈도 급감 고객</li>
                    <li>리볼빙 잔액 급증 고위험 고객</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        markdown(
            """
            <div class="dashboard-card">
                <h3 style="color:white;">CRM 실행 방안</h3>
                <ul style="color:#cbd5e1;line-height:1.8;">
                    <li>AI Score 기반 자동 오퍼링</li>
                    <li>한도 상향 및 금리 인하 제안</li>
                    <li>개인화된 멤버십 혜택 강화</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
