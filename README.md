# SKN-2nd-1Team

---
## 💳머신러닝 기반 신용카드 가입 고객 이탈 예측 시스템

---
## 개발 기간
**2026.03.04 ~ 2026.03.16**

---

## 팀 소개
### **Team EXODIA**
<table align="center">
  <tr>
  <td align="center" width="160px"><img src="./notebooks/YounJeongYeon/data/images/2.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
  <td align="center" width="160px"><img src="./notebooks/YounJeongYeon/data/images/3.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
  <td align="center" width="160px"><img src="./notebooks/YounJeongYeon/data/images/5.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
  <td align="center" width="160px"><img src="./notebooks/YounJeongYeon/data/images/4.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
  <td align="center" width="160px"><img src="./notebooks/YounJeongYeon/data/images/1.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
  <td align="center" width="160px"><img src="./notebooks/YounJeongYeon/data/images/6.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
</tr>
  <tr>
    <td align="center"><b>서민혁</b></td>
    <td align="center"><b>유동현</b></td>
    <td align="center"><b>윤정연</b></td>
    <td align="center"><b>전종혁</b></td>
    <td align="center"><b>정영일</b></td>
    <td align="center"><b>조동휘</b></td>
  </tr>
  <tr>
    <td align="center">PM/FULL STACK</td>
    <td align="center">FRONT</td>
    <td align="center">FRONT</td>
    <td align="center">DB/BACK</td>
    <td align="center">FRONT</td>
    <td align="center">DB/BACK</td>
  </tr>
  <div align="center">
  <table>
    <div align="center">
  <table>
    <tr>
      <td align="center"><a href="https://github.com/minhyeok328"><img src="https://img.shields.io/badge/minhyeok328-34495e?style=flat&logo=github&logoColor=white"></a></td>
      <td align="center"><a href="https://github.com/Ocean-2930"><img src="https://img.shields.io/badge/Ocean--2930-34495e?style=flat&logo=github&logoColor=white"></a></td>
      <td align="center"><a href="https://github.com/dimolto3"><img src="https://img.shields.io/badge/dimolto3-34495e?style=flat&logo=github&logoColor=white"></a></td>
      <td align="center"><a href="https://github.com/jjonyeok2"><img src="https://img.shields.io/badge/jjonyeok2-34495e?style=flat&logo=github&logoColor=white"></a></td>
      <td align="center"><a href="https://github.com/wjdduddlf112"><img src="https://img.shields.io/badge/wjdduddlf112-34495e?style=flat&logo=github&logoColor=white"></a></td>
      <td align="center"><a href="https://github.com/nobrain711"><img src="https://img.shields.io/badge/nobrain711-34495e?style=flat&logo=github&logoColor=white"></a></td>
    </tr>
  </table>
</div>


---

## 1. 프로젝트 개요
### 1-1. 프로젝트 개요 (Project Overview)
본 프로젝트는 카드 고객 데이터를 기반으로 **고객 활동 패턴과 카드 이탈(Churn) 간의 관계**를 분석하고, 이를 바탕으로 고객 세그먼트별 맞춤형 카드 상품 전략을 도출하는 것을 목표로 한다. 현재 카드 산업은 신규 고객 확보 비용이 매우 높기 때문에, 기존 고객의 이탈을 방지하고 장기적인 고객 가치를 유지하는 것이 최우선 과제로 인식되고 있다.

이를 위해 본 프로젝트에서는 'BankChurners' 데이터셋을 활용하여 거래 횟수, 거래 금액, 카드 한도 활용도 등 고객 활동 지표를 중심으로 탐색적 데이터 분석(EDA)을 수행했다. 고객의 활동 수준을 기준으로 세그먼트를 도출한 후, 각 집단별 카드 이용 패턴과 이탈률을 비교하여 이탈 위험이 높은 타겟을 식별했다. 또한, 거래 활동의 변화 추이와 비활성 기간 등 동적인 행동 데이터를 함께 고려하여 **이탈의 주요 선행 신호**를 파악하였다.

분석 결과를 바탕으로 고객 세그먼트별 특성을 반영한 카드 상품 라인업 개편 및 리텐션(고객 유지) 전략을 제안하였다. 본 프로젝트는 단순한 데이터 분석을 넘어, 고객 행동 데이터 기반의 실효성 있는 금융 상품 전략을 수립함으로써 카드 산업 내 데이터 활용의 새로운 가능성을 탐색하는 것을 목표로 한다.

### 1-2. 문제 정의
**높은 유지보수 중요성**: 카드 산업 특성상 신규 고객 확보 비용(CAC)이 매우 높아, 기존 고객의 이탈(Churn) 방지가 핵심 비즈니스 과제입니다.

**이탈 징후 파악의 한계**: 고객마다 거래 빈도, 결제 금액, 한도 활용도 등 사용 패턴이 크게 달라 일원화된 잣대로 이탈을 예측하기 어렵습니다.

**해결 과제**: 고객의 복잡한 행동 차이 중 어떤 특정 패턴이 이탈의 결정적 신호로 작용하는지 명확히 규명할 필요가 있습니다.

---

## 2. 데이터 소개
https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

---

## 3. 분석 목표
본 프로젝트는 단순한 '카드 사용 감소 = 이탈'이라는 평면적인 공식을 넘어, 고객이 처한 **맥락(Context)**을 데이터로 증명하고 이해하는 것을 핵심 목표로 합니다. 실제 데이터에 존재하는 **'카드 등급(Card_Category)'**과 '고객 결속도(보유 상품 수, Total_Relationship_Count)' 등의 명확한 지표를 고객의 거래 패턴 변화와 결합하여, 다음 세 가지 목표를 달성하고자 합니다.

'미이용 기간'의 입체적 재해석
비활성 기간을 단일한 잣대로 평가하지 않습니다. 고객이 보유한 카드 등급, 연령대, 그리고 이용 중인 금융 상품의 개수를 복합적으로 고려합니다. 이를 통해 동일한 미이용 기간이라도 고객의 소비 성향과 카드 보유 구조(주거래 vs 서브)에 따라 이탈 위험도가 어떻게 달라지는지 다각도로 해석합니다.

행동 변화(Trend) 기반의 진짜 이탈 시그널 포착
단순한 변수 간의 정적인 차이가 아니라, **'거래 횟수 변화, 거래 금액 변화, 고객 활동성 변화'**라는 동적인 흐름(Trend)에 집중합니다. 특정 카드 등급이나 세그먼트에서 이탈 직전에 공통적으로 나타나는 치명적이고 결정적인 선행 신호가 무엇인지 실제 데이터로 규명합니다.

맥락 기반의 맞춤형 상품 및 리텐션 전략 도출
도출된 인사이트를 바탕으로 천편일률적인 마케팅이 아닌, 타겟 집단의 특성(예: 단일 상품 보유 이탈 위험군 vs 다중 상품 보유 이탈 위험군, 소액 다결제 vs 고액 소결제)에 딱 맞는 실효성 있는 카드 상품 라인업 개편 및 고객 유지 전략을 제안합니다.

---

## 4. 분석 방법
1. 탐색적 데이터 분석 (EDA):
Kaggle에서 제공하는 데이터셋을 사용하여 단순 통계 확인을 넘어, 이탈 고객과 유지 고객 간의 행동 패턴(거래 횟수, 거래 금액, 비활성 기간 등) 차이를 시각화하고 세그먼트별 특징을 도출했습니다.

2. 데이터 전처리 (Data Preprocessing):
머신러닝 모델의 성능을 극대화하기 위해 결측치 및 이상치를 처리하고, 범주형 변수 인코딩과 스케일링을 진행했습니다. (특히, 유지 고객과 이탈 고객 간의 클래스 불균형 문제를 해결하기 위한 가중치/샘플링 기법을 적용했습니다.)

3. 머신러닝 모델링 및 성능 비교 (Machine Learning Modeling):
고객 이탈(Churn) 여부를 빠르고 정확하게 예측하기 위해, 6명의 팀원이 각자 다른 알고리즘을 전담하여 구현하고 성능을 다각도로 비교했습니다. 이탈 데이터 특유의 '클래스 불균형(Imbalance)' 문제를 극복하고 향후 웹 서비스(Streamlit) 배포 환경까지 고려하여 아래의 6가지 모델 라인업을 구성했습니다.

- Logistic Regression: 연산이 매우 빠르고 변수 해석력이 뛰어난 선형 모델로, 전체 예측 성능의 '하한선(Baseline)'을 설정했습니다.

- Random Forest: 다수의 결정 트리를 활용하는 배깅(Bagging) 앙상블의 정석으로, 과적합을 방지하고 안정적인 성능을 확보했습니다.

- XGBoost (XGB): 정형 데이터 분석에 강력한 부스팅(Boosting) 모델로, 정교한 잔차 학습을 통해 타 모델들과 성능을 비교하는 핵심 기준점이 되었습니다.

- LightGBM (LGBM): 리프 중심 트리 분할 방식을 통해 압도적인 학습 속도와 가벼운 용량을 자랑하며, 리소스가 제한된 배포 환경에 최적화된 성능을 구현했습니다.

- HistGradientBoosting: 사이킷런(Scikit-learn) 환경에서 대용량 데이터를 고속으로 처리하기 위해 도입했으며, 전처리 의존도를 낮추고 빠른 학습을 진행했습니다.

- EasyEnsemble: 압도적으로 많은 유지 고객 데이터에 모델이 편향되는 것을 막기 위해 도입한 '불균형 데이터 특화 모델'로, 숨어있는 이탈 고객을 찾아내는 능력(Recall)을 극대화했습니다.

이후 각 모델별로 GridSearchCV 등을 활용한 최적의 하이퍼파라미터 튜닝을 거쳤으며, 단순 정확도(Accuracy)가 아닌 불균형 데이터에 적합한 평가지표(F1-score, Recall 등)를 기준으로 최종 챔피언(이탈 예측) 모델을 선정했습니다.

4. 변수 중요도 파악 및 비즈니스 전략 도출 (Insight & Strategy):
단순히 예측 정확도를 높이는 데 그치지 않고, 최종 선정된 모델이 이탈을 판단할 때 가장 중요하게 작용한 핵심 변수(Feature Importance)를 추출했습니다.
이렇게 데이터 알고리즘이 찾아낸 '결정적 이탈 시그널(예: 특정 거래 금액의 급감, 비활성 기간 임계치 돌파 등)'을 바탕으로, 앞서 정의한 고객 세그먼트별 특성에 딱 맞는 실효성 있는 리텐션(고객 유지) 마케팅 전략과 맞춤형 카드 상품 라인업을 수립했습니다.


---

## 5. 주요 분석 결과
전체 고객 중 약 15%가 이탈하는 것으로 나타났으며, 무작위 타겟 마케팅보다는 이탈 위험군 방어가 훨씬 효율적임을 확인했습니다. 데이터 탐색 결과, **"카드 이탈은 고객의 우발적 단절이 아닌, 점진적인 행동 변화에 의해 발생한다"**는 결론을 도출했습니다.

💡 1. 이탈은 '갑작스러운 사건'이 아닌 '점진적 과정'

거래량 급감: 유지 고객의 연간 거래 횟수 중앙값은 약 70회인 반면, 이탈 고객은 약 43회로 뚜렷한 감소(약 25~30회 차이)를 보입니다.

사용률 추락: 이탈 고객의 대다수는 한 번에 카드를 해지하는 것이 아니라, 신용한도 대비 카드 사용률을 0~20%대까지 서서히 줄여나간 뒤 최종 이탈하는 패턴을 보입니다.

💡 2. '누구(Who)'인지보다 '어떻게(How)' 쓰는지가 핵심

나이, 학력, 소득, 가입 기간 등 인구통계학적 변수는 이탈과 유의미한 상관관계가 없었습니다. (데이터의 주 고객층은 연소득 $40K 이하의 대중적인 타겟임이 확인됨)

반면, 거래 횟수(-0.37), 거래 증가율(-0.29) 등 실제 사용 행동 지표가 이탈을 예측하는 압도적인 요인임이 입증되었습니다.

💡 3. 고객센터 연락은 강력한 '이탈 전조 증상'

비활성 기간(Months_Inactive)이 길어지는 것과 더불어, 최근 12개월 내 **고객센터 접촉 횟수(Contacts_Count)가 늘어날수록 이탈 가능성이 상승(+0.20)**합니다. 이는 혜택 불만, 연회비 혹은 해지 관련 문의가 이탈의 직접적인 시그널로 작용함을 의미합니다.

🎯 Top 6 핵심 이탈 예측 변수

[절대적 사용량]
- Total_Trans_Ct: 연간 총 거래 횟수

- Total_Trans_Amt: 연간 총 거래 금액

- Avg_Utilization_Ratio: 평균 신용한도 대비 사용률

[행동의 변화 흐름]
- Total_Ct_Chng_Q4_Q1: 1분기 대비 4분기 거래량 증감률

[강력한 위험 신호]
- Months_Inactive_12_mon: 최근 12개월 내 비활성 개월 수

- Contacts_Count_12_mon: 최근 12개월 내 고객센터 연락 횟수


---

## 6. 인사이트 및 전략 제안


---

## 7. 사용 기술


---


