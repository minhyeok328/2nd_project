"""
=========================================================================
Project:
- Credit Card Customers

Module:
- streamlit

File: eda_streamlit.py

Purpose:
- EDA main page

Author: @nobrain711
Created: 2026-03-13

Updated:
=========================================================================
"""

import streamlit as st

eda1 = './data/eda1.png'
eda2 = './data/eda2.png'
eda3 = './data/eda3.png'
eda4 = './data/eda4.png'
eda5 = './data/eda5.png'
eda6 = './data/eda6.png'

st.set_page_config(page_title="EDA Overview", layout="wide")

st.title("📊 Credit Card Customer EDA")
st.markdown("고객 이탈 분석을 위한 주요 탐색적 데이터 분석 결과를 정리한 페이지입니다.")

width_ls = [1, 5, 1, 5, 1]

# EDA1
with st.container(border=True):
    _, sec_A, _, sec_B, _ = st.columns(width_ls, gap="large")
    with sec_A:
        # 사진
        st.image(eda1, caption="Correlation Heatmap with Attrition_Flag", use_container_width=True)
    with sec_B:
        # 설명
        st.markdown(
            """
            ### Correlation Heatmap with Attrition_Flag

            ### 설명
            전체 주요 수치형 변수들과 이탈 여부(Attrition_Flag) 간의 상관관계를 한눈에 보여주는 히트맵입니다.

            ### 해석
            - `Total_Trans_Ct`는 이탈 여부와 **음의 상관관계(-0.37)**를 보여, 거래 횟수가 많을수록 이탈 가능성이 낮아지는 경향이 있습니다.
            - `Total_Ct_Chng_Q4_Q1(-0.29)`, `Total_Revolving_Bal(-0.26)`도 이탈과 음의 상관을 보여, 활발히 카드를 사용하는 고객일수록 유지될 가능성이 높습니다.
            - `Contacts_Count_12_mon(0.20)`, `Months_Inactive_12_mon(0.15)`는 이탈과 양의 상관을 보여, 비활성 기간이 길고 고객센터 접촉이 많을수록 이탈 가능성이 커집니다.
            - 전반적으로 이탈은 연령이나 가입기간보다 **카드 사용 패턴과 거래 활동성**과 더 관련이 큰 것으로 보입니다.
            """
        )

# EDA2
with st.container(border=True):
    _, sec_A, _, sec_B, _ = st.columns(width_ls, gap="large")
    with sec_A:
        # 설명
        st.markdown(
            """
            ### Distribution of Customer Churn (0: Existing, 1: Attrited)

            ### 설명
            전체 고객 중 기존 고객(0)과 이탈 고객(1)의 수를 비교한 막대그래프입니다.

            ### 해석
            - 기존 고객(0)의 수가 이탈 고객(1)보다 훨씬 많아, 데이터가 **불균형 클래스** 구조를 가지고 있음을 알 수 있습니다.
            - 즉, 이탈 고객은 전체 고객 중 일부에 해당하므로 모델링 시 단순 정확도만으로 평가하면 성능이 과대평가될 수 있습니다.
            - 따라서 향후 분류 모델에서는 **recall, precision, F1-score** 같은 지표를 함께 보는 것이 중요합니다.
            """
        )
    with sec_B:
        # 사진
        st.image(eda2, caption="", use_container_width=True)

# EDA3
with st.container(border=True):
    _, sec_A, _, sec_B, _ = st.columns(width_ls, gap="large")
    with sec_A:
        # 사진
        st.image(eda3, caption="", use_container_width=True)
    with sec_B:
        # 설명
        st.markdown(
            """
            ### 사용 비율에 따른 이탈 밀도도

            ### 설명
            평균 카드 사용 비율(`Avg_Utilization_Ratio`)에 따라 기존 고객과 이탈 고객의 분포 차이를 나타낸 밀도 그래프입니다.

            ### 해석
            - 기존 고객(0)은 낮은 사용 비율 구간뿐 아니라 중간 이상 사용 비율 구간에도 넓게 분포하고 있습니다.
            - 이탈 고객(1)은 전반적으로 **낮은 사용 비율 구간에 더 밀집**되어 있어, 카드를 적극적으로 사용하지 않는 고객일수록 이탈 가능성이 높다고 볼 수 있습니다.
            - 즉, 카드 활용도가 낮은 고객은 서비스 충성도나 이용 빈도 측면에서 위험 신호로 해석할 수 있습니다.
            """
        )

# EDA4
with st.container(border=True):
    _, sec_A, _, sec_B, _ = st.columns(width_ls, gap="large")
    with sec_A:
        # 설명
        st.markdown(
            """
            ### 이탈 여부에 따른 결제 횟수 차이

            ### 설명
            이탈 여부에 따라 총 거래 횟수(`Total_Trans_Ct`)의 분포를 비교한 박스플롯입니다.

            ### 해석
            - 기존 고객(0)의 중앙값이 이탈 고객(1)보다 뚜렷하게 높아, **거래 횟수가 많은 고객일수록 유지 가능성**이 높습니다.
            - 이탈 고객은 전반적으로 거래 횟수가 낮은 구간에 집중되어 있습니다.
            - 이는 고객 이탈을 설명하는 핵심 변수 중 하나가 거래 활동성임을 보여주며, 실제 상관분석 결과와도 일치합니다.
            """
        )
    with sec_B:
        # 사진
        st.image(eda4, caption="", use_container_width=True)
    

# EDA5
with st.container(border=True):
    _, sec_A, _, sec_B, _ = st.columns(width_ls, gap="large")
    with sec_A:
        # 사진
        st.image(eda5, caption="", use_container_width=True)
    with sec_B:
        # 설명
        st.markdown(
            """
            ### 소득 수준별 이탈 고객 분포

            ### 설명
            소득 구간(`Income_Category`)별로 기존 고객과 이탈 고객의 수를 비교한 막대그래프입니다.

            ### 해석
            - 전체적으로 `Less than $40K` 구간의 고객 수가 가장 많고, 이탈 고객 수도 함께 많이 나타납니다.
            - 다만 이는 해당 소득 구간의 **전체 고객 수 자체가 많기 때문**일 가능성이 있으므로, 단순 건수만으로 이탈 위험이 가장 높다고 단정하기는 어렵습니다.
            - 소득 수준은 이탈에 일부 관련이 있을 수 있으나, 거래 횟수나 비활성 기간 같은 행동 변수보다 영향력이 더 직접적이지는 않아 보입니다.
            """
        )

# EDA6
with st.container(border=True):
    _, sec_A, _, sec_B, _ = st.columns(width_ls, gap="large")
    with sec_A:
        # 설명
        st.markdown(
            """
            ### 학력과 소득 수준의 관계

            ### 설명
            학력 수준(`Education_Level`)과 소득 구간(`Income_Category`)의 조합별 고객 수를 나타낸 히트맵입니다.

            ### 해석
            - `Graduate`와 `High School` 집단에서 고객 수가 많고, 특히 `Less than $40K` 구간에 집중된 모습이 나타납니다.
            - 전반적으로 대부분의 학력 수준에서 저소득 구간 고객 비중이 크게 나타나며, 학력과 소득 사이에 어느 정도 분포 차이가 존재합니다.
            - 이 그래프는 고객 세그먼트를 이해하는 데 유용하며, 이후 학력·소득 조합별 이탈률 분석으로 확장할 수 있습니다.
            """
        )
    with sec_B:
        # 사진
        st.image(eda6, caption="", use_container_width=True)