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
- 2026-03-13: dashborad 색상 반영 (@nobrain711)
- 2026-03-16: MLflow 예측 입력 구조 반영 (@nobrain711)
- 2026-03-16: 버튼 클릭 시 예측 결과 반영 구조 수정 (@nobrain711)
=========================================================================
"""

import pandas as pd
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
    caption,
)

from common.config import MODEL_NAME_LIST
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

    if not leaderboard_data.empty:
        dataframe(
            leaderboard_data.style.background_gradient(
                cmap="Blues", subset=["정확도(Acc)"]
            )
            .background_gradient(cmap="Purples", subset=["정밀도(Precision)"])
            .background_gradient(cmap="Oranges", subset=["재현율(Recall)"])
            .background_gradient(cmap="Greens", subset=["ROC-AUC"])
            .background_gradient(cmap="PuBuGn", subset=["PR-AUC"])
            .background_gradient(cmap="Reds", subset=["F1-score"]),
            width="stretch",
            hide_index=True,
        )

    markdown("<br>", unsafe_allow_html=True)
    markdown(
        '<div class="section-tag">PREDICTION-SERVICE</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = columns(3)
    with col1:
        user_age = number_input("고객 연령", min_value=18, max_value=100, value=47)
    with col2:
        gender_list = ["남성", "여성"]
        user_gender = selectbox("성별", options=gender_list)
    with col3:
        user_dependents = number_input("부양가족 수", min_value=0, value=0)

    col1, col2, col3 = columns(3)
    with col1:
        education_list = [
            "미취학",
            "고등학생",
            "대학생",
            "대졸",
            "석사",
            "박사",
            "불명",
        ]
        user_education = selectbox("학력", options=education_list)
    with col2:
        marital_list = ["미혼", "기혼", "이혼", "불명"]
        user_marital = selectbox("결혼 상태", options=marital_list)
    with col3:
        income_list = [
            "$40K 미만",
            "$40K - $60K",
            "$60K - $80K",
            "$80K - $120K",
            "$120K 이상",
            "미확인",
        ]
        user_income = selectbox("소득 구간", options=income_list)

    col1, col2, col3 = columns(3)
    with col1:
        card_type_list = ["블루", "실버", "골드", "플래티넘"]
        user_card_type = selectbox("카드 종류", options=card_type_list)
    with col2:
        user_relationship_months = number_input("가입 기간(월)", min_value=0, value=21)
    with col3:
        user_product_count = number_input("보유 상품 수", min_value=0, value=6)

    col1, col2, col3 = columns(3)
    with col1:
        user_inactive_months = number_input("비활성 기간(월)", min_value=0, value=0)
    with col2:
        user_contact_count = number_input("고객센터 상담 횟수", min_value=0, value=2)
    with col3:
        user_credit_limit = number_input("카드 한도", min_value=0.0, value=8892.62)

    col1, col2, col3 = columns(3)
    with col1:
        user_revolving_balance = slider(
            "리볼빙 잔액 ($)", min_value=0, max_value=5000, value=1972
        )
    with col2:
        user_available_credit = number_input("가용 한도", min_value=0.0, value=22609.0)
    with col3:
        user_amount_change = number_input("결제 금액 변화율", value=1.42)

    col1, col2, col3 = columns(3)
    with col1:
        user_count_change = number_input("결제 횟수 변화율", value=1.47)
    with col2:
        user_transaction_amount = number_input(
            "총 결제 금액 ($)", min_value=0.0, value=1333.86
        )
    with col3:
        user_transaction_count = number_input("총 결제 횟수", min_value=0, value=63)

    utilization_ratio = (
        0.0 if user_credit_limit == 0 else user_revolving_balance / user_credit_limit
    )

    user_input = {
        "creditcard_churn_id": 0,
        "age": user_age,
        "gender": gender_list.index(user_gender),
        "dependents": user_dependents,
        "education_id": education_list.index(user_education) + 1,
        "marital_id": marital_list.index(user_marital) + 1,
        "income_id": income_list.index(user_income) + 1,
        "card_type_id": card_type_list.index(user_card_type) + 1,
        "relationship_months": user_relationship_months,
        "product_count": user_product_count,
        "inactive_months": user_inactive_months,
        "contact_count": user_contact_count,
        "credit_limit": user_credit_limit,
        "revolving_balance": user_revolving_balance,
        "available_credit": user_available_credit,
        "amount_change": user_amount_change,
        "count_change": user_count_change,
        "transaction_amount": user_transaction_amount,
        "transaction_count": user_transaction_count,
        "utilization_ratio": utilization_ratio,
    }

    input_df = pd.DataFrame([user_input])

    col_in, _, col_res = columns([0.6, 0.6, 1], gap="large")

    with col_in:
        selected_model = selectbox(
            "분석 모델 선택",
            options=MODEL_NAME_LIST,
            index=MODEL_NAME_LIST.index(session_state["selected_model"]),
        )
        session_state["selected_model"] = selected_model

        run_clicked = button("분석 실행 (RUN)", width="stretch")

        if run_clicked:
            try:
                result_prob = predict_churn_logic(
                    model_name=selected_model,
                    input_df=input_df,
                )
                print("result_prob:", result_prob)
                session_state["res_prob"] = float(result_prob)
                session_state["last_model"] = selected_model
                session_state["prediction_error"] = None
            except Exception as exc:
                session_state["res_prob"] = 0.0
                session_state["prediction_error"] = str(exc)

    with col_res:
        markdown(
            "<h4 style='margin:0; opacity:0.8; font-size:14px; letter-spacing:0.1em; color: white;'>CHURN RISK STATUS</h4>",
            unsafe_allow_html=True,
        )

        final_prob = float(session_state.get("res_prob", 0.0))
        dynamic_color = get_gradient_color(final_prob)
        percent_text = f"{final_prob * 100:.1f}%"

        markdown(
            f"""
            <div style="margin-top: 10px;">
                <span style="font-size: 96px; font-weight: 900; color: {dynamic_color}; text-shadow: 0px 10px 20px rgba(0,0,0,0.3);">
                    {percent_text}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        caption("버튼을 누르면 선택한 모델의 최신 MLflow artifact로 예측합니다.")

        prediction_error = session_state.get("prediction_error")
        if prediction_error:
            markdown(
                f"""
                <div class='dashboard-card' style='border:1px solid rgba(248,113,113,0.35); margin-top:12px;'>
                    <strong style='color:#fca5a5;'>예측 실패</strong><br>
                    <span style='color:#cbd5e1;'>{prediction_error}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    markdown("---")

    current_model = session_state["selected_model"]

    col_left, col_right = columns([1, 1.5], gap="large")

    with col_left:
        markdown(
            f"""
            <div class="dashboard-card" style="background: linear-gradient(135deg, rgba(75, 108, 183, 0.4) 0%, rgba(24, 40, 72, 0.4) 100%); min-height: 350px;">
                <div class="section-tag" style="color: rgba(255,255,255,0.6);">MODEL-CONTEXT</div>
                <h2 style="margin: 0; font-weight:900; color: white;">{current_model}</h2>
                <p class="highlight-gold" style="margin-top:10px; font-size:18px;">AI 엔진 가동 중</p>
                <div style="margin-top:15px; font-size:15px; color: #cbd5e1; line-height: 1.6;">
                    우측 그래프를 통해 위험 점수를 결정한 핵심 변수를 확인하십시오.
                    구체적인 대응 전략은 STRATEGY REPORT에서 확인 가능합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_right:
        markdown(
            '<div class="section-tag">FEATURE-INFLUENCE</div>',
            unsafe_allow_html=True,
        )

        impact_df = get_impact_data(current_model)

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
            width="stretch",
            config={"displayModeBar": False},
        )
