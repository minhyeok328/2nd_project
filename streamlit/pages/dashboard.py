"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- pages

File:
- dashboard.py

Purpose:
- Dashboard 페이지 렌더링을 담당합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from plotly.express import bar
from streamlit import (
    title,
    markdown,
    dataframe,
    button,
    number_input,
    selectbox,
    columns,
    slider,
    session_state,
    plotly_chart,
)

from utils.color import get_gradient_color
from utils.data_loader import get_impact_data, get_leaderboard_data
from utils.prediction import predict_churn_logic


def render_dashboard_page() -> None:
    """
    Dashboard 페이지를 렌더링합니다.
    """
    leaderboard_data = get_leaderboard_data()

    title("CRM Intelligence")

    markdown(
        """
        <div class="dashboard-card" style="background: rgba(255, 255, 255, 0.05);">
            <div class="section-tag">SERVICE-OVERVIEW</div>
            <h2 style="margin: 0; font-weight: 900; color: white;">AI 기반 카드 고객 이탈 예측 시스템</h2>
            <p style="margin-top: 15px; font-size: 16px; line-height: 1.6; color: #cbd5e1;">
                실시간 데이터 분석을 통해 고객의 이탈 리스크를 사전에 진단합니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    markdown(
        '<div class="section-tag">MODEL-LEADERBOARD</div>',
        unsafe_allow_html=True,
    )
    dataframe(
        leaderboard_data.style.background_gradient(cmap="Blues", subset=["정확도(Acc)"])
        .background_gradient(cmap="Oranges", subset=["재현율(Recall)"])
        .background_gradient(cmap="Greens", subset=["ROC-AUC"]),
        use_container_width=True,
        hide_index=True,
    )

    markdown("<br>", unsafe_allow_html=True)
    markdown(
        '<div class="section-tag">PREDICTION-SERVICE</div>',
        unsafe_allow_html=True,
    )

    col_in, col_res = columns([1.2, 1], gap="large")

    with col_in:
        selected_model = selectbox(
            "분석 모델 선택",
            options=leaderboard_data["모델명(Model)"].tolist(),
        )
        user_age = number_input("고객 연령", 18, 100, 45)
        user_amount = number_input("총 결제 금액 ($)", value=5000)
        user_income = selectbox(
            "소득 구간",
            options=[
                "$40K 미만",
                "$40K - $60K",
                "$60K - $80K",
                "$80K - $120K",
                "$120K 이상",
                "미확인",
            ],
        )
        user_revolving = slider("리볼빙 잔액 ($)", 0, 5000, 1500)

        if button("분석 실행 (RUN)", use_container_width=True):
            result_prob = predict_churn_logic(
                model_name=selected_model,
                age=user_age,
                amount=user_amount,
                income=user_income,
                revolving=user_revolving,
            )
            session_state["res_prob"] = result_prob
            session_state["last_model"] = selected_model

    with col_res:
        markdown(
            "<h4 style='margin:0; opacity:0.8; font-size:14px; letter-spacing:0.1em; color: white;'>CHURN RISK STATUS</h4>",
            unsafe_allow_html=True,
        )
        final_prob = session_state["res_prob"]
        dynamic_color = get_gradient_color(final_prob)

        markdown(
            f"""
            <div style="margin-top: 10px;">
                <span style="font-size: 96px; font-weight: 900; color: {dynamic_color} !important; text-shadow: 0px 10px 20px rgba(0,0,0,0.3);">
                    {final_prob * 100:.1f}%
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    markdown("---")

    col_left, col_right = columns([1, 1.5], gap="large")

    with col_left:
        current_model = session_state.get("last_model", selected_model)

        markdown(
            f"""
            <div class="dashboard-card" style="background: linear-gradient(135deg, rgba(75, 108, 183, 0.4) 0%, rgba(24, 40, 72, 0.4) 100%); min-height: 350px;">
                <div class="section-tag" style="color: rgba(255,255,255,0.6);">MODEL-CONTEXT</div>
                <h2 style="margin: 0; font-weight:900; color: white;">{current_model}</h2>
                <p class="highlight-gold" style="margin-top:10px; font-size:18px;">AI 엔진 가동 중</p>
                <div style="margin-top:15px; font-size:15px; color: #cbd5e1; line-height: 1.6;">
                    우측 SHAP 그래프를 통해 위험 점수를 결정한 핵심 변수를 확인하십시오.
                    구체적인 대응 전략은 STRATEGY REPORT에서 확인 가능합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_right:
        markdown(
            '<div class="section-tag">FEATURE-INFLUENCE (SHAP)</div>',
            unsafe_allow_html=True,
        )

        impact_df = get_impact_data()

        fig = bar(
            impact_df,
            x="영향력",
            y="feature",
            orientation="h",
            color_discrete_sequence=["#7dd3fc"],
        )
        fig.update_layout(
            height=320,
            margin=dict(l=0, r=20, t=10, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#94a3b8"),
            xaxis={"showgrid": False},
        )

        plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False},
        )
