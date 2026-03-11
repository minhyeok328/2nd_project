import streamlit as st
import pandas as pd
import numpy as np

# 1. 페이지 설정
st.set_page_config(page_title="CRM | Churn AI", layout="wide")

# 2. JS & CSS
st.markdown("""
    <script>
        const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
        if (sidebar) { sidebar.style.display = 'none'; }
    </script>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .dashboard-card {
        padding: 30px;
        border-radius: 24px;
        margin-bottom: 25px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 12px 40px rgba(0,0,0,0.06);
    }

    .section-tag {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin-bottom: 15px;
        color: #868E96;
    }

    /* 다크모드 대응 */
    @media (prefers-color-scheme: dark) {
        .stApp h1 { color: #ADB5BD !important; }
        .section-tag { color: #ADB5BD !important; opacity: 1 !important; }
        .overview-section { background-color: #1E1E1E !important; border: 1px solid #333333 !important; }
        .overview-section h2, .overview-section h4, .overview-section p { color: #E9ECEF !important; }
    }

    /* 섹션별 배경색 */
    .overview-section { background: #F1F3F5; border: 1px solid #E9ECEF; color: #1A1A1A; }
    .predict-section { background: linear-gradient(135deg, #1A1A1A 0%, #373B44 100%) !important; padding: 50px; color: white !important; }
    .predict-section * { color: white !important; }

    .model-section { background: linear-gradient(135deg, #4B6CB7 0%, #182848 100%) !important; min-height: 500px; justify-content: flex-start !important; color: white !important; }
    .model-section * { color: white !important; }

    .vis-area { background: transparent !important; border: none !important; box-shadow: none !important; padding: 10px 0 0 0 !important; }
    .display-value { font-size: 96px; font-weight: 900; line-height: 1; color: #FFFFFF !important; }
    [data-testid="stWidgetLabel"] p { color: white !important; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

# 3. 메인 타이틀
st.title("CRM Intelligence")
st.markdown("---")

# 4. [🌟 핵심 수정] Service Overview - 포트폴리오용 상세 설명
st.markdown('''
    <div class="dashboard-card overview-section">
        <div class="section-tag">Service-Overview</div>
        <h2 style="margin: 0; font-weight: 900;">AI 기반 카드 고객 이탈 예측 시스템</h2>
        <p style="margin-top: 15px; font-size: 16px; line-height: 1.6; opacity: 0.9;">
            본 애플리케이션은 신용카드 고객 데이터를 분석하여 <b>이탈 가능성이 높은 고객을 실시간으로 감지</b>하고, 
            비즈니스 리스크를 최소화하기 위한 전략적 인사이트를 제공합니다.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 30px; margin-top: 25px; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 25px;">
            <div>
                <h4 style="margin:0;">🚀 Multi-Inference</h4>
                <p style="font-size: 13px; margin-top:8px;">LGBM, XGBoost 등 5가지 머신러닝 모델을 활용한 교차 검증 및 최적의 예측 성능 제공</p>
            </div>
            <div>
                <h4 style="margin:0;">📊 Explainable AI (XAI)</h4>
                <p style="font-size: 13px; margin-top:8px;">SHAP 알고리즘을 적용하여 특정 고객이 왜 이탈 위험군으로 분류되었는지 기술적 근거 시각화</p>
            </div>
            <div>
                <h4 style="margin:0;">📈 Strategic Insight</h4>
                <p style="font-size: 13px; margin-top:8px;">단순 예측을 넘어 리텐션(Retention) 마케팅을 위한 핵심 변수 파악 및 전략 가이드 제시</p>
            </div>
        </div>
    </div>
''', unsafe_allow_html=True)

# 5. Predict Section
with st.container():
    st.markdown('<div class="dashboard-card predict-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-tag">Predict-Section</div>', unsafe_allow_html=True)
    col_in, col_res = st.columns([1, 1], gap="large")
    with col_in:
        selected_model = st.selectbox("Select Model",
                                      options=["LightGBM (LGBM)", "XGBoost (XGB)", "Logistic Regression", "Extra Trees",
                                               "HistGradientBoosting"])
        st.number_input("Customer Age", 18, 100, 45)
        st.number_input("Transaction Amount ($)", value=5000)
        st.button("RUN ANALYSIS")
    with col_res:
        st.markdown("<h4 style='color:#FF4B4B !important; margin:0;'>CHURN RISK STATUS</h4>", unsafe_allow_html=True)
        st.markdown('<div class="display-value">87.4%</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Model & Vis Section
col_left, col_right = st.columns([1, 1.5], gap="large")
with col_left:
    st.markdown(f'''
        <div class="dashboard-card model-section">
            <div class="section-tag">Model-Section</div>
            <h2 style="margin: 0; font-weight:900;">{selected_model}</h2>
            <div style="margin-top:25px; font-size:15px; opacity:0.9;">
                <b>Baseline Model</b><br>
                선택된 알고리즘을 통해 고객의 금융 활동 패턴을 정밀 분석합니다.
            </div>
        </div>
    ''', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="vis-area">', unsafe_allow_html=True)
    st.markdown('<div class="section-tag">Feature Influence (SHAP)</div>', unsafe_allow_html=True)
    impact_data = pd.DataFrame({'Features': ['Trans_Amt', 'Total_Ct', 'Util_Ratio', 'Revolving_Bal', 'Age'],
                                'Impact': [0.48, 0.35, 0.22, 0.15, 0.08]})
    st.bar_chart(impact_data.set_index('Features'), height=420)
    st.markdown('</div>', unsafe_allow_html=True)

# 7. Summary
st.markdown(f'''
    <div class="dashboard-card" style="background: #F8F9FA; border: 1px solid #E9ECEF; color:#1A1A1A;">
        <div class="section-tag">Summary-Section</div>
        <h2 style="margin: 0; font-weight: 900;">Strategic Insight</h2>
        <p style="margin-top: 15px; line-height:1.6;">{selected_model} 분석 결과, 고객 관리가 시급한 상태입니다. SHAP 지표에서 나타난 상위 변수를 중심으로 맞춤형 혜택 제공을 권장합니다.</p>
    </div>
''', unsafe_allow_html=True)

st.caption("© 2026 JJonyeok2 | SK Networks AI Camp Baseline System")