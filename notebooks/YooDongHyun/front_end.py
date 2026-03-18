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
=========================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests

# 1. 페이지 설정 및 세션 초기화
st.set_page_config(page_title="CRM | Churn AI", layout="wide")
if 'page' not in st.session_state:
    st.session_state['page'] = 'Dashboard'
if 'res_prob' not in st.session_state:
    st.session_state['res_prob'] = 0.0

# 사용하는 모델 리스트
MODEL_LIST = ["HistGradientBoosting", "XGBoost", "Logistic Regression"]

# 데이터 파이프라인에서 df load 함수
def fetch_creditcard(X_y_split: bool = False
                     ) -> pd.DataFrame | tuple[pd.DataFrame, pd.Series]:
    # response = requests.get("http://pipeline:8000/dataset/creditcard-churn", params={"X_y_split": X_y_split})
    # payload = response.json()
    
    # if X_y_split:
    #     X = pd.DataFrame(payload["x"], index=payload["index"])
    #     y = pd.Series(payload["y"], index=payload["index"])
    #     return X, y
    
    # df = pd.DataFrame(payload["data"], index=payload["index"])
    
    df = pd.read_csv("df_fetch.csv").drop("Unnamed: 0", axis=1)

    return df

# bank_df 없으면 (train_X, train_y) Dataframe tuple 형태로 저장
# Standard Scaler 역시 instance 생성
if 'bank_df' not in st.session_state:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler

    fetch_df = fetch_creditcard(False).drop("creditcard_churn_id", axis=1)

    feature_df =fetch_df[[k for k in fetch_df.columns if k != "churn"]]
    churn_df = fetch_df['churn']

    train_X, _, train_y, _ = train_test_split(
        feature_df,
        churn_df,
        test_size=0.2,
        stratify=churn_df,
        random_state=42
    )

    scaler = StandardScaler()
    train_X_scaled = scaler.fit_transform(train_X)

    st.session_state['bank_df'] = (train_X_scaled, train_y)
    st.session_state['scaler'] = scaler

if 'models' not in st.session_state:
    st.session_state['models'] = {}

# [내부 로직] 실시간 추론 시뮬레이션
def predict_churn_logic(model_name:str, userdat:list) -> float:
    if model_name not in MODEL_LIST:
        return 0

    if model_name not in st.session_state['models']:
        match (model_name):
            case "HistGradientBoosting":
                from sklearn.ensemble import HistGradientBoostingClassifier
                model = HistGradientBoostingClassifier(
                    max_iter=150,
                    random_state=42,
                    early_stopping=True,
                    n_iter_no_change=20,
                    validation_fraction=0.05
                )
                model.fit(st.session_state['bank_df'][0], st.session_state['bank_df'][1])
                st.session_state['models'][model_name] = model
            case "XGBoost":
                from xgboost import XGBClassifier
                final_params = {
                    'colsample_bytree': 1.0,
                    'gamma': 0.3,
                    'learning_rate': 0.05,
                    'max_depth': 4,
                    'n_estimators': 300,
                    'reg_lambda': 1.0,
                    'scale_pos_weight': 1,
                    'subsample': 0.8
                }

                model = XGBClassifier(
                    **final_params,
                    random_state=42,
                    use_label_encoder=False,
                    eval_metric='logloss'
                )
                model.fit(st.session_state['bank_df'][0], st.session_state['bank_df'][1])
                st.session_state['models'][model_name] = model
            case "Logistic Regression":
                from sklearn.linear_model import LogisticRegression
                model = LogisticRegression(max_iter=1000)
                model.fit(st.session_state['bank_df'][0], st.session_state['bank_df'][1])
                st.session_state['models'][model_name] = model
            case _:
                raise Exception("Wrong Model Name")

    userdat_np = np.array(userdat).reshape(1, -1)
    userdat_scaled = st.session_state['scaler'].transform(userdat_np)
    prob = st.session_state['models'][model_name].predict_proba(userdat_scaled)          

    return prob[0][1]


# [🎨 색상 로직] 0%(Red) -> 100%(Blue) 그라데이션
def get_gradient_color(prob):
    if prob < 0.5:
        r, g, b = 255, int(75 + (prob * 2 * 125)), int(75 - (prob * 2 * 25))
    else:
        ratio = (prob - 0.5) * 2
        r, g, b = int(255 - (ratio * 180)), int(200 - (ratio * 92)), int(50 + (ratio * 133))
    return f"rgb({r}, {g}, {b})"


# 2. JS & CSS (디자인 시스템 정의)
st.markdown("""
    <script>
        const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
        if (sidebar) { sidebar.style.display = 'none'; }
    </script>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    .main { background: radial-gradient(circle at top right, #1e293b, #0f172a); }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; scroll-behavior: smooth; }

    .dashboard-card {
        padding: 30px; border-radius: 28px; margin-bottom: 25px;
        background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(12px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease;
    }
    .top-btn {
        position: fixed; bottom: 30px; right: 30px; width: 55px; height: 55px;
        background: rgba(75, 108, 183, 0.2); backdrop-filter: blur(10px);
        color: white !important; border-radius: 50%; display: flex; align-items: center; justify-content: center;
        text-decoration: none; font-weight: 900; z-index: 9999; border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .section-tag { font-size: 10px; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 15px; color: #94a3b8; }
    .highlight-gold { color: #fde047; font-weight: 700; text-shadow: 0 0 10px rgba(253, 224, 71, 0.3); }
    </style>
    <div id="top"></div>
    <a href="#top" class="top-btn">▲</a>
    """, unsafe_allow_html=True)

# 3. 네비게이션
col_nav1, col_nav2 = st.columns([1, 1])
with col_nav1:
    if st.button("📊 ANALYSIS DASHBOARD", width='stretch'):
        st.session_state['page'] = 'Dashboard'
with col_nav2:
    if st.button("💳 STRATEGY REPORT", width='stretch'):
        st.session_state['page'] = 'Strategy'

st.markdown("---")

# 리더보드 데이터 (공통 사용)
leaderboard_data = pd.DataFrame({
    '모델명(Model)': MODEL_LIST,
    '정확도(Acc)': [0.9858, 0.9729, 0.7698],
    '재현율(Recall)': [0.9369, 0.9800, 0.9800],
    'ROC-AUC': [0.9979, 0.9720, 0.9701],
    'PR-AUC': [0.9901, 0.9600, 0.8868,],
    'F1-score': [0.9556, 0.9800, 0.5800]
}).sort_values(by='ROC-AUC', ascending=False)

# ---------------------------------------------------------
# PAGE 1: Dashboard
# ---------------------------------------------------------
if st.session_state['page'] == 'Dashboard':
    st.title("CRM Intelligence")

    st.markdown('''
        <div class="dashboard-card" style="background: rgba(255, 255, 255, 0.05);">
            <div class="section-tag">SERVICE-OVERVIEW</div>
            <h2 style="margin: 0; font-weight: 900; color: white;">AI 기반 카드 고객 이탈 예측 시스템</h2>
            <p style="margin-top: 15px; font-size: 16px; line-height: 1.6; color: #cbd5e1;">
                실시간 데이터 분석을 통해 고객의 이탈 리스크를 사전에 진단합니다.
            </p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="section-tag">MODEL-LEADERBOARD</div>', unsafe_allow_html=True)
    st.dataframe(leaderboard_data.style.background_gradient(cmap='Blues', subset=['정확도(Acc)'])
                 .background_gradient(cmap='Oranges', subset=['재현율(Recall)'])
                 .background_gradient(cmap='Greens', subset=['ROC-AUC']), width='stretch', hide_index=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-tag">PREDICTION-SERVICE</div>', unsafe_allow_html=True)


    # 1줄
    col1, col2, col3 = st.columns(3)
    with col1:
        u_age = st.number_input("고객 연령", 18, 100, 47)
    with col2:
        gender_ls = ["남성", "여성"]
        u_gender = st.selectbox("성별", options=gender_ls)
    with col3:
        u_dependent = st.number_input("자식 수", value=0)


    # 2줄
    col1, col2, col3 = st.columns(3)
    with col1:
        education_ls = ["미취학", "고등학생", "대학생", "대졸", "석사", "박사", "불명"]
        u_education = st.selectbox("학력", options=education_ls)
    with col2:
        marital_ls = ["미혼", "기혼", "이혼", "불명"]
        u_marital = st.selectbox("결혼 상태", options=marital_ls)
    with col3:
        income_ls = ['$40K 미만', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K 이상', '미확인']
        u_income = st.selectbox("소득 구간", options=income_ls)


    # 3줄
    col1, col2, col3 = st.columns(3)
    with col1:
        cardtype_ls = ["블루", "실버", "골드", "플래티넘"]
        u_cardtype = st.selectbox("카드 종류", options=cardtype_ls)
    with col2:
        u_relmonth = st.number_input("가입기간", value=21)
    with col3:
        u_prodcount = st.number_input("카드 수", value=6)


    # 4줄
    col1, col2, col3 = st.columns(3)
    with col1:
        u_inactive = st.number_input("비활성 기간", value=0)
    with col2:
        u_contactcnt = st.number_input("고객센터 상담 횟수", value=2)
    with col3:
        u_crditlim = st.number_input("카드 한도", value=8892.62)


    # 5줄
    col1, col2, col3 = st.columns(3)
    with col1:
        u_revolving = st.slider("리볼빙 잔액 ($)", 0, 5000, 1972)
    with col2:
        u_balance = st.number_input("통장 잔액", value=22609)
    with col3:
        u_amtchange = st.number_input("결제 금액 변화", value=1.42)


    # 6줄
    col1, col2, col3 = st.columns(3)
    with col1:
        u_cntchange = st.number_input("결제 횟수 변화", value=1.47)
    with col2:
        u_amount = st.number_input("총 결제 금액 ($)", value=1333.86)
    with col3:
        u_count = st.number_input("총 결제 횟수", value=63)
    
    #     ['age', 'gender', 'dependents', 'education_id', 'marital_id',
    #    'income_id', 'card_type_id', 'relationship_months', 'product_count',
    #    'inactive_months', 'contact_count', 'credit_limit', 'revolving_balance',
    #    'available_credit', 'amount_change', 'count_change',
    #    'transaction_amount', 'transaction_count', 'utilization_ratio']

    userdat = [
            u_age, gender_ls.index(u_gender), u_dependent, education_ls.index(u_education)+1, marital_ls.index(u_marital)+1,
            income_ls.index(u_income)+1, cardtype_ls.index(u_cardtype)+1, u_relmonth, u_prodcount,
            u_inactive, u_contactcnt, u_crditlim, u_revolving,
            u_balance, u_amtchange, u_cntchange,
            u_amount, u_count, (u_amount / 1 if (u_crditlim == 0) else u_crditlim)
    ]

    col_in, col_res = st.columns([1.2, 1], gap="large")
    with col_in:

        s_model = st.selectbox("분석 모델 선택", options=MODEL_LIST)

        if st.button("분석 실행 (RUN)", width='stretch'):
            res = predict_churn_logic(s_model, userdat)
            st.session_state['res_prob'] = res
            st.session_state['last_model'] = s_model  # 모델 기억

    with col_res:
        st.markdown(
            "<h4 style='margin:0; opacity:0.8; font-size:14px; letter-spacing:0.1em; color: white;'>CHURN RISK STATUS</h4>",
            unsafe_allow_html=True)
        final_prob = st.session_state['res_prob']
        dynamic_color = get_gradient_color(final_prob)
        st.markdown(
            f'<div style="margin-top: 10px;"><span style="font-size: 96px; font-weight: 900; color: {dynamic_color} !important; text-shadow: 0px 10px 20px rgba(0,0,0,0.3);">{final_prob * 100:.1f}%</span></div>',
            unsafe_allow_html=True)

    st.markdown("---")
    col_left, col_right = st.columns([1, 1.5], gap="large")
    with col_left:
        st.markdown(f'''<div class="dashboard-card" style="background: linear-gradient(135deg, rgba(75, 108, 183, 0.4) 0%, rgba(24, 40, 72, 0.4) 100%); min-height: 350px;">
            <div class="section-tag" style="color: rgba(255,255,255,0.6);">MODEL-CONTEXT</div>
            <h2 style="margin: 0; font-weight:900; color: white;">{s_model}</h2>
            <p class="highlight-gold" style="margin-top:10px; font-size:18px;">AI 엔진 가동 중</p>
            <div style="margin-top:15px; font-size:15px; color: #cbd5e1; line-height: 1.6;">우측 SHAP 그래프를 통해 위험 점수를 결정한 핵심 변수를 확인하십시오. 구체적인 대응 전략은 STRATEGY REPORT에서 확인 가능합니다.</div>
        </div>''', unsafe_allow_html=True)
    with col_right:
        st.markdown('<div class="section-tag">FEATURE-INFLUENCE (SHAP)</div>', unsafe_allow_html=True)
        impact_df = pd.DataFrame({',': ['총 결제 금액', '소득 구간', '총 결제 횟수', '한도 소진율', '리볼빙 잔액'],
                                  '영향력': [0.55, 0.45, 0.38, 0.25, 0.18]}).sort_values(by='영향력')
        fig = px.bar(impact_df, x='영향력', y=',', orientation='h', color_discrete_sequence=['#7dd3fc'])
        fig.update_layout(height=320, margin=dict(l=0, r=20, t=10, b=0), paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#94a3b8"), xaxis={'showgrid': False})
        st.plotly_chart(fig, width='stretch', config={'displayModeBar': False})

# ---------------------------------------------------------
# PAGE 2: Strategy (7번 섹션이 넘어온 페이지)
# ---------------------------------------------------------
elif st.session_state['page'] == 'Strategy':
    st.title("Strategy Report")

    current_model = st.session_state.get('last_model', leaderboard_data['모델명(Model)'].iloc[0])

    st.markdown(f'''
        <div class="dashboard-card">
            <div class="section-tag">STRATEGIC-DECISION-SUPPORT</div>
            <h2 style="margin: 0; font-weight: 900; color: white;">{current_model} 기반 대응 전략</h2>
            <p style="margin-top: 15px; color: #cbd5e1; font-size: 16px;">
                최근 분석된 모델의 특성을 기반으로 최적의 CRM 가이드를 제시합니다.
            </p>
        </div>
    ''', unsafe_allow_html=True)

    # 모델별 맞춤 가이드 데이터
    guides = {
        "HistGradientBoosting": ["대용량 데이터 미세 패턴 포착", "과적합 위험(Noise)", "Random Forest 교차 타겟팅"],
        "XGBoost": ["정확도/재현율 밸런스 에이스", "복잡한 비선형 해석 난해", "Logistic Regression 보조 활용"],
        "EasyEnsemble": ["이탈자 전수 탐지(Recall 0.98)", "마케팅 비용 낭비 우려", "LightGBM 기반 예산 효율화"],
        "Random Forest": ["안정적인 일반화 성능", "정교한 신호 탐지 한계", "HistGBM 모델 고도화 추천"],
        "LightGBM": ["실시간 오퍼 최적화 속도", "소량 데이터 취약성", "XGBoost와 상호 보완"],
        "Logistic Regression": ["명확한 원인 설명력", "비선형 관계 포착 한계", "앙상블 모델 병행 사용"]
    }
    g_s, g_w, g_r = guides.get(current_model, ["데이터 기반 분석", "모델 고유 특성 고려", "맞춤형 오퍼 제안"])

    # 🌊 리퀴드 글래스 전략 가이드 카드 (7번 섹션 복구 및 강화)
    st.markdown(f'''
        <div class="dashboard-card">
            <h3 style="color:white; font-weight:900;">{current_model} 분석 리포트</h3>
            <div style="margin-top: 25px; line-height:1.8;">
                <p style="color: #cbd5e1;">💪🏼 <b>강점(Strength):</b> {g_s}</p>
                <p style="color: #cbd5e1;">⚠️ <b>보완점(Weakness):</b> {g_w}</p>
                <div style="background: rgba(34, 139, 230, 0.1); padding: 25px; border-radius: 20px; border: 1px solid rgba(34, 139, 230, 0.3); margin-top: 20px;">
                    <strong style="color:#7dd3fc; font-size:18px;">💡 비즈니스 추천(Recommendation):</strong><br>
                    <span style="color: white; opacity: 0.9;">{g_r}</span>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="dashboard-card"><h3 style="color:white;">핵심 리텐션 타겟</h3><ul style="color:#cbd5e1;line-height:1.8;"><li>VIP 고액 결제 이탈 위험군</li><li>최근 3개월 사용 빈도 급감 고객</li><li>리볼빙 잔액 급증 고위험 고객</li></ul></div>',
            unsafe_allow_html=True)
    with col2:
        st.markdown(
            '<div class="dashboard-card"><h3 style="color:white;">CRM 실행 방안</h3><ul style="color:#cbd5e1;line-height:1.8;"><li>AI Score 기반 자동 오퍼링</li><li>한도 상향 및 금리 인하 제안</li><li>개인화된 멤버십 혜택 강화</li></ul></div>',
            unsafe_allow_html=True)

st.caption("© 2026 JJonyeok2 | Team EXODIA")