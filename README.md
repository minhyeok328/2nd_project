## 💳머신러닝 기반 신용카드 가입 고객 이탈 예측 시스템


### 📅개발 기간 
#### 2026.03.04 ~ 2026.03.16

---

### 개발 스택
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-006699?style=for-the-badge&logoColor=white) ![EasyEnsemble](https://img.shields.io/badge/EasyEnsemble-imblearn-FF6F61?style=for-the-badge&logoColor=white) ![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logoColor=white)


---

### 👋🏻팀 소개
#### **Team EXODIA**
<table align="center">
  <tr>
    <td align="center" width="160px"><img src="./docs/images/2.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./docs/images/3.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./docs/images/5.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./docs/images/4.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./docs/images/1.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
    <td align="center" width="160px"><img src="./docs/images/6.png" width="100" style="object-fit: contain; aspect-ratio: 1/1;"></td>
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
    <td align="center"><b>Model</b><br>XGBoost<br>Income Modeling</td>
    <td align="center"><b>Model</b><br>HistGradientBoosting</td>
    <td align="center"><b>Model</b><br>XGBoost</td>
    <td align="center"><b>Model</b><br>EasyEnsemble</td>
    <td align="center"><b>Model</b><br>Logistic Regression</td>
    <td align="center"><b>Model</b><br>LightGBM</td>
  </tr>

  <tr>
    <td align="center"><b>Role</b><br>Data Pipeline</td>
    <td align="center"><b>Role</b><br>Streamlit</td>
    <td align="center"><b>Role</b><br>Docs</td>
    <td align="center"><b>Role</b><br>Streamlit</td>
    <td align="center"><b>Role</b><br>Presentation</td>
    <td align="center"><b>Role</b><br>Data Pipeline</td>
  </tr>

  <tr>
    <td align="center"><a href="https://github.com/minhyeok328"><img src="https://img.shields.io/badge/minhyeok328-34495e?style=flat&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/Ocean-2930"><img src="https://img.shields.io/badge/Ocean--2930-34495e?style=flat&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/dimolto3"><img src="https://img.shields.io/badge/dimolto3-34495e?style=flat&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/jjonyeok2"><img src="https://img.shields.io/badge/jjonyeok2-34495e?style=flat&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/wjdduddlf112"><img src="https://img.shields.io/badge/wjdduddlf112-34495e?style=flat&logo=github&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/nobrain711"><img src="https://img.shields.io/badge/nobrain711-34495e?style=flat&logo=github&logoColor=white"></a></td>
  </tr>
</table>

---

## 1. 프로젝트 개요📑
### 1-1. 프로젝트 개요 (Project Overview)
본 프로젝트는 카드 고객 데이터를 기반으로 **고객 활동 패턴과 카드 이탈(Churn) 간의 관계**를 분석하고, 이를 바탕으로 고객 세그먼트별 맞춤형 카드 상품 전략을 도출하는 것을 목표로 합니다. 현재 카드 산업은 신규 고객 확보 비용이 매우 높기 때문에, 기존 고객의 이탈을 방지하고 장기적인 고객 가치를 유지하는 것이 최우선 과제로 인식되고 있습니다.

동적인 행동 데이터를 기반으로 **이탈의 주요 선행 신호**를 도출하여 고객 세그먼트별 맞춤형 카드 상품 라인업 개편과 리텐션 전략을 제안했습니다. 본 프로젝트는 단순한 데이터 분석을 넘어, 고객 행동 데이터 기반의 실효성 있는 금융 상품 전략을 수립함으로써 카드 산업 내 데이터 활용의 새로운 가능성을 탐색하는 것을 목표로 합니다.

### 1-2. 문제 정의
**높은 유지보수 중요성:** 카드 산업 특성상 신규 고객 확보 비용(CAC)이 매우 높아, 기존 고객의 이탈(Churn) 방지가 핵심 비즈니스 과제입니다.

**이탈 징후 파악의 한계:** 고객마다 거래 빈도, 결제 금액, 한도 활용도 등 사용 패턴이 크게 달라 일원화된 잣대로 이탈을 예측하기 어렵습니다.

**해결 과제:** 고객의 복잡한 행동 차이 중 어떤 특정 패턴이 이탈의 결정적 신호로 작용하는지 명확히 규명할 필요가 있습니다.

---

## 2. 실행 방법 (Quick Start / How to Run)
### 1. 사전 요구사항
Docker가 PC에 설치가 되어있어야지 프로젝트가 구동됩니다.

### 2. 저장소 클론
```bash
git clone https://github.com/SKN26-2nd-1st/2nd_project.git
cd 2nd_project
```
### 3. 환경 변수 설정
`.env.example` 파일을 복사하여 `.env` 파일을 생성합니다.
```bash
cp config/.env.example config/.env
```
`.env.example` 파일을 참고하여 `.env` 파일을 수정합니다.
### 4. Docker 실행
```
docker compose up --build
```

### 5. 서비스 접속
* Streamlit Dashboard
    ```text
    http://localhost:18501
    ```
* MLflow
    ```text
     http://localhost:15000
    ```
* Pipeline API
    ```
    http://localhost:18000/docs
    ```

---

## 3. 🖥️화면 구현
**분석 대시보드 + 모델별 확률**
<div align="center">
  <img src="./docs/gif/Animation1.gif" width="800px" alt="Streamlit Dashbaord Preview">
</div>

**전략 보고서**
<div align="center">
  <img src="./docs/gif/Animation2.gif" width="800px" alt="Streamlit Dashbaord Preview">
</div>

**데이터 분석 결과 페이지**
<div align="center">
  <img src="./docs/gif/Animation3.gif" width="800px" alt="Streamlit Dashbaord Preview">
</div>


---
## 4. 분석 목표📌
본 프로젝트는 단순한 '카드 사용 감소 = 이탈'이라는 평면적인 공식을 넘어, 고객이 처한 **맥락**을 데이터로 증명하고 이해하는 것을 중심으로 하여 다음 세가지 목표를 달성하고자 합니다.

1. **'미사용 기간'의 입체적 재해석:**    
비활성 기간을 단일한 잣대로 평가하지 않습니다. 고객이 보유한 카드 등급, 연령대, 그리고 이용 중인 금융 상품의 개수를 복합적으로 고려합니다. 이를 통해 동일한 미이용 기간이라도 고객의 소비 성향과 카드 보유 구조(주거래 vs 서브)에 따라 이탈 위험도가 어떻게 달라지는지 다각도로 해석합니다.

2. **행동 변화 기반의 진짜 이탈 시그널 포착:**    
단순한 변수 간의 정적인 차이가 아니라, **거래 감소 -> 카드 사용 감소 -> 비활성 고객 -> 이탈**라는 동적인 흐름에 집중합니다. 특정 카드 등급이나 세그먼트에서 이탈 직전에 공통적으로 나타나는 치명적이고 결정적인 선행 신호가 무엇인지 실제 데이터로 규명합니다.

3. **맥락 기반의 맞춤형 상품 및 리텐션 전략 도출:**    
도출된 인사이트를 바탕으로 천편일률적인 마케팅이 아닌, 타겟 집단의 특성(예: 소액 다결제 vs 고액 소결제)에 딱 맞는 실효성 있는 카드 상품 라인업 개편 및 고객 유지 전략을 제안합니다.


---
## 5. 데이터 소개 및 데이터 베이스 설계🪄
### Kaggle datasets
https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers


### ERD(Feature Table)
[erdcloud](https://www.erdcloud.com/d/uKmdsevxvwYpTqAFk)

#### 논리 모델링

* 테이블
    ```mermaid
    erDiagram
        dim_education {
            TINYINT education_id PK
            VARCHAR education_label UK
            INT sort_order
        }

        dim_marital {
            TINYINT marital_id PK
            VARCHAR marital_label UK
            INT sort_order
        }

        dim_income {
            TINYINT income_id PK
            VARCHAR income_label UK
            INT income_min
            INT income_max
            INT sort_order
        }

        dim_card_type {
            TINYINT card_type_id PK
            VARCHAR card_type_label UK
            INT sort_order
        }

        creditcard_churn {
            BIGINT creditcard_churn_id PK
            TINYINT education_id FK
            TINYINT marital_id FK
            TINYINT income_id FK
            TINYINT card_type_id FK
            TINYINT age
            TINYINT gender
            TINYINT dependents
            SMALLINT relationship_months
            TINYINT product_count
            TINYINT churn_status
            TINYINT inactive_months
            TINYINT contact_count
            DECIMAL credit_limit
            DECIMAL revolving_balance
            DECIMAL available_credit
            DECIMAL amount_change
            DECIMAL count_change
            DECIMAL transaction_amount
            SMALLINT transaction_count
            DECIMAL utilization_ratio
        }


        dim_education ||--o{ creditcard_churn : "education_id" 
        dim_marital ||--o{ creditcard_churn : "marital_id" 
        dim_income ||--o{ creditcard_churn : "income_id" 
        dim_card_type ||--o{ creditcard_churn : "card_type_id" 
    ```

* 테이블 관계도
    ```mermaid
    flowchart LR
        DE[dim_education]
        DM[dim_marital]
        DI[dim_income]
        DC[dim_card_type]
        CC[creditcard_churn]
        
        DE -->|education_id| CC
        DM -->|marital_id| CC
        DI -->|income_id| CC
        DC -->|card_type_id| CC
    ```

### 물리 모델링
<div align="center">
  <img src="./docs/erd/physical_model_creditcard_churn.png" width="800px" alt="Credit Card Churn ERD">
</div>

본 프로젝트는 Kaggle 원본 데이터를 기반으로 고객 이탈 분석에 필요한 주요 피처를 관리할 수 있도록 데이터베이스 구조를 설계했습니다.  
ERD는 고객 기본 정보, 카드 이용 정보, 거래 관련 지표, 그리고 이탈 여부를 중심으로 분석 및 예측에 필요한 컬럼을 구조화한 형태입니다.

특히 머신러닝 학습과 예측에 활용되는 피처를 일관된 기준으로 관리할 수 있도록 구성했으며,  
향후 파이프라인을 통해 CSV 적재, 데이터 조회, 모델 입력 데이터 생성이 가능하도록 설계했습니다.

---

## 6. 분석 방법🔎
1. **탐색적 데이터 분석 (EDA):**   
Kaggle에서 제공하는 데이터셋을 사용하여 단순 통계 확인을 넘어, 이탈 고객과 유지 고객 간의 행동 패턴(거래 횟수, 거래 금액, 비활성 기간 등) 차이를 시각화하고 세그먼트별 특징을 도출했습니다.

2. **데이터 전처리 (Data Preprocessing):**   
머신러닝 모델의 성능을 극대화하기 위해 결측치 및 이상치를 처리하고, 범주형 변수 인코딩과 스케일링을 진행했습니다. (특히, 유지 고객과 이탈 고객 간의 클래스 불균형 문제를 해결하기 위한 가중치/샘플링 기법을 적용했습니다.)

3. **머신러닝 모델링 및 성능 비교:**   
고객 이탈 여부를 빠르고 정확하게 예측하기 위해, 6명의 팀원이 각각 머신러닝 모델을 구현하고 성능을 다각도로 비교했습니다.
특히 신용카드 이탈 데이터 특유의 '클래스 불균형(Class Imbalance)' 문제를 극복하고, 향후 Streamlit 기반의 웹 서비스 배포 환경까지 고려하여 아래와 같이 6가지 모델 라인업을 구성했습니다.

- Logistic Regression: 연산이 매우 빠르고 변수 해석력이 뛰어난 선형 모델로, 전체 예측 성능의 '하한선(Baseline)'을 설정했습니다.

- XGBoost (XGB): 정형 데이터 분석에 강력한 부스팅(Boosting) 모델로, 정교한 잔차 학습을 통해 타 모델들과 성능을 비교하는 핵심 기준점이 되었습니다.

- LightGBM (LGBM): 리프 중심 트리 분할 방식을 통해 압도적인 학습 속도와 가벼운 용량을 자랑하며, 리소스가 제한된 배포 환경에 최적화된 성능을 구현했습니다.

- HistGradientBoosting: Scikit-learn 환경에서 대용량 데이터를 고속으로 처리하기 위해 도입했으며, 전처리 의존도를 낮추고 빠른 학습을 진행했습니다.

- EasyEnsemble: 압도적으로 많은 유지 고객 데이터에 모델이 편향되는 것을 막기 위해 도입한 '불균형 데이터 특화 모델'로, 숨어있는 이탈 고객을 찾아내는 능력(Recall)을 극대화했습니다.

4. **변수 중요도 파악 및 비즈니스 전략 도출 (Insight & Strategy):**   
단순히 예측 정확도를 높이는 데 그치지 않고, 최종 선정된 모델이 이탈을 판단할 때 가장 중요하게 작용한 핵심 변수를 추출했습니다.
이렇게 데이터 알고리즘이 찾아낸 '결정적 이탈 시그널(거래 횟수 감소, 고객센터 접촉 등)'을 바탕으로, 앞서 정의한 고객 세그먼트별 특성에 딱 맞는 실효성 있는 리텐션(고객 유지) 마케팅 전략과 맞춤형 카드 상품 라인업을 수립했습니다.


---

## 7. 주요 분석 결과💡
전체 고객 중 약 15%가 이탈하는 것으로 나타났으며, 무작위 타겟 마케팅보다는 이탈 위험군 방어가 훨씬 효율적임을 확인했습니다. 데이터 탐색 결과, **카드 이탈은 고객의 우발적 단절이 아닌, 점진적인 행동 변화에 의해 발생한다**는 결론을 도출했습니다.

1. **이탈은 '갑작스러운 사건'이 아닌 '점진적 과정'**
   * **거래량 급감**: 유지 고객의 연간 거래 횟수 중앙값은 약 70회인 반면, 이탈 고객은 약 43회로 **뚜렷한 감소(약 25~30회 차이)**를 보입니다.
   * **사용률 추락**: 이탈 고객의 대다수는 한 번에 카드를 해지하는 것이 아니라, 신용한도 대비 카드 사용률을 **0~20%대까지 서서히 줄여나간 뒤** 최종 이탈하는 패턴을 보입니다.

2. **'누구(Who)'인지보다 '어떻게(How)' 쓰는지가 핵심**
   * 나이, 학력, 소득, 가입 기간 등 고객 특성과 이탈간의 상관관계는 유의미하지 않았습니다. *(데이터의 주 고객층은 연소득 $40K 이하의 대중적인 타겟임이 확인됨)*
   * 반면, **거래 횟수(-0.37), 거래 증가율(-0.29)** 등 실제 카드 사용 행동 지표가 이탈을 예측하는 압도적인 요인임이 입증되었습니다.

3. **고객센터 연락은 강력한 '이탈 전조 증상'**
   * 비활성 기간이 길어지는 것과 더불어, 최근 12개월 내 **고객센터 접촉 횟수(Contacts_Count)가 늘어날수록 이탈 가능성이 상승(+0.20)**합니다.
   * 이는 혜택 불만, 연회비 혹은 해지 관련 문의가 이탈의 직접적인 시그널로 작용함을 의미합니다.


### 🎯 핵심 이탈 예측 변수

#### [절대적 사용량]

* 매우 중요: Total_Trans_Ct (연간 총 거래 횟수)
* 매우 중요: Total_Trans_Amt (연간 총 거래 금액)
* 중요: Avg_Utilization_Ratio (평균 신용한도 대비 사용률)

#### [행동의 변화 흐름]
* Total_Ct_Chng_Q4_Q1 (1분기 대비 4분기 거래량 증감률)

#### [강력한 위험 신호]
* Months_Inactive_12_mon (최근 12개월 내 비활성 개월 수)
* Contacts_Count_12_mon (최근 12개월 내 고객센터 연락 횟수)

---

## 8. 인사이트 및 전략 제안⭐
앞서 도출된 분석 결과에 따르면, 고객의 이탈은 어느 날 갑자기 일어나는 우발적 사건이 아니라 **'결제 빈도의 뚜렷한 감소'** 그리고 **'고객센터 문의 증가'**라는 명확한 전조 증상을 동반하는 점진적인 과정이었습니다.

따라서 본 프로젝트는 고객의 카드 이탈 전조 증상인 '사용 감소 흐름'을 사전에 끊어내기 위해, 실제 행동 패턴(How)에 직접 개입하여 사용 습관을 재고정하고 고객 생애 가치(LTV)를 극대화하는 것을 핵심 방향으로 설정했습니다. 이를 실현하고자 이용 가치 상승을 위한 **'업셀 구조'**와 결제 장벽 완화를 위한 **'행동 기반 구조'**를 결합한 데이터 기반 맞춤형 카드 라인업 전략을 수립하여, 이탈률 하락과 수익성 제고를 동시에 달성하고자 합니다.

#### 1. 리워드 기반 카드 라인업 (고객 가치 상승 & 업셀링 전략)
고객의 현재 이용 수준에 맞춰 혜택을 제공하고, 점진적으로 상위 카드로의 전환(업셀링)을 유도하여 고객 생애 가치(LTV)를 극대화합니다.

| 콘셉트 | 목적 | 혜택 골자 | 가격 / 조건 | 자격 기준 / (게이팅) | 리스크 통제 | KPI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Entry** | 고객 활성화 | 첫 결제 보너스, 자동납부 혜택, 웰컴 포인트 | 저 / 무연회비, 웰컴 혜택 | 신규 / 저이용 고객 | 낮은 초기 한도, 사용 모니터링 | 30일 활성화율 |
| **Cashback** | 일상 소비 카테고리 고정 | 생활 카테고리 할인 / 캐시백 | 실적 조건 + 월 혜택 캡 | 안정적 이용 패턴 고객 | 혜택 캡, 제휴 비용 분담 | 월 이용 횟수 |
| **Points** | 이용액 확대 / 업셀 | 기본 포인트 적립 + 선택 카테고리 추가 적립 | 실적 조건 상향, 적립 캡 | 일정 이용액 이상 고객 | 오퍼 과다 지급 방지 | 이용액 증가 |
| **Premium** | 핵심 고객 유지 | 여행 / 라운지 / 다이닝 혜택 | 고연회비 + 선택 혜택 | 고이용 / 고가치 고객 | 쿠폰형 혜택 구조 | 갱신율 / ARPU / 이용액 |

#### 2. 행동 기반 카드 라인업 (결제 장벽 완화 & 관계 확장 전략)
고객의 구체적인 소비 행동과 금융 니즈를 타겟팅하여 카드사의 가맹점 수수료 외 추가적인 금융 수익을 창출합니다.

| 콘셉트 | 목적 | 혜택 골자 | 가격 / 조건 | 자격 기준 / (게이팅) | 리스크 통제 | KPI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Co-brand** | 선호 기반 소비 확대 | 항공 마일리지 / 브랜드 할인 | 제휴 연회비 구조 | 브랜드 충성 고객 확보 | 제휴 정산 관리 | 제휴 이용 비중 |
| **Installment** | 고액 결제 장벽 완화 | 무 / 저이자 할부 | 할부 기간 / 업종별 조건 | 고액 결제 고객 | 업종별 한도 관리 | 할부 전환율 |
| **Revolving** | 상환 유연성 제공 | 부분 결제 / 상환 옵션 | 조건부 금리 | 일정 신용도 이상 | 이용률 / 연체 관리 | 리볼빙 이용률 |
| **Bundle / Family** | 고객 관계 확장 | 가족 / 구독 / 자동납부 혜택 | 번들 혜택 구조 | 다상품 이용 고객 | 혜택 누수 방지 | 상품 보유 수 증가 |

#### 3. 고객 세그먼트별 매칭 전략
앞서 구성한 리워드 및 행동 기반 카드 라인업을 각 고객군의 특성과 이용 패턴에 맞춰 매칭하여, 초기 활성화부터 고가치 고객 유지까지 단계별 이탈 방어 전략을 실행합니다.

| Segment | 주요 상품 전략 | 전략 목적 | 카드 상품 유형 |
| :--- | :--- | :--- | :--- |
| **Dormant** | Entry | 초기 카드 사용 활성화 | Entry |
| **Casual** | Cashback | 생활 소비 카드 고정 | Cashback |
| **Active** | Points / Co-brand | 이용액 확대 및 제휴 소비 유도 | Points / Co-brand |
| **Premium** | Premium | 고가치 고객 유지 | Premium |
| **High utilization** | Revolving | 고사용 고객 결제 부담 완화 및 상환 유연성 제공 | Revolving |



---

## 9. 기술 스택 🛠️

### Data Pipeline & Backend

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/MySQL%208.0.45-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

- Python 기반 데이터 처리 및 머신러닝 파이프라인 구현  
- FastAPI를 활용한 예측 API 서버 구축  
- MySQL을 통한 고객 데이터 및 분석 결과 저장

---


### Data Analysis
<img src="https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white">

- Pandas 기반 데이터 전처리 및 탐색적 데이터 분석(EDA)

---

### Machine Learning
<img src="https://img.shields.io/badge/scikit--learn-1.8-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
<img src="https://img.shields.io/badge/XGBoost-3.2-EB5E28?style=for-the-badge">
<img src="https://img.shields.io/badge/LightGBM-4.5-9ACD32?style=for-the-badge">
<img src="https://img.shields.io/badge/EasyEnsemble-imbalanced--learn-blue?style=for-the-badge">

- scikit-learn 기반 머신러닝 모델 구현  
- XGBoost / LightGBM 부스팅 모델을 활용한 성능 비교  
- EasyEnsemble을 활용한 클래스 불균형 문제 대응  

---

### Experiment Tracking
<img src="https://img.shields.io/badge/MLflow-3.10-0194E2?style=for-the-badge&logo=mlflow&logoColor=white">

- MLflow를 통한 모델 실험 관리 및 성능 추적

---

### Visualization / Dashboard
<img src="https://img.shields.io/badge/Streamlit-1.5-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">

- Streamlit 기반 분석 대시보드 및 예측 결과 시각화  
- Figma를 활용한 UI 설계


---

### Environment & Infrastructure
<img src="https://img.shields.io/badge/Docker-27.x-2496ED?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/Docker%20Compose-2.x-2496ED?style=for-the-badge&logo=docker&logoColor=white">

- Docker Compose 기반 서비스 환경 구성
> Docker Iamge는 [nobrain711](https://hub.docker.com/repositories/nobrain711)에서 참조

---

### Collaboration
<img src="https://img.shields.io/badge/Git-2.x-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white">

- GitHub 기반 협업 및 버전 관리
---

## 10. 프로젝트 구조 📁

본 프로젝트는 **데이터 파이프라인, 머신러닝 실험, 서비스 레이어를 분리한 MLOps 스타일 구조**로 구성되어 있습니다.

```text
📦 Root Directory
 ┣ 📂 database/         # 데이터베이스 초기 스키마 및 SQL 스크립트
 ┣ 📂 config/           # 시스템 환경 변수 및 설정 관리
 ┣ 📂 docs/             # 프로젝트 문서, ERD, 아키텍처 및 산출물
 ┣ 📂 mlflow/           # MLflow 실험 결과 및 모델 아티팩트 저장
 ┣ 📂 notebooks/        # EDA 및 모델 실험용 Jupyter Notebook
 ┣ 📂 pipeline/         # 데이터 ETL 및 FastAPI 기반 파이프라인 서버
 ┣ 📂 streamlit/        # Streamlit 기반 예측 서비스 UI
 ┣ 📜 docker-compose.yml # Docker 기반 서비스 오케스트레이션
 ┣ 📜 README.md         # 프로젝트 메인 문서
 ┣ 📜 LICENSE           # 프로젝트 라이선스
 ┣ 📜 model_evaluation.md # 모델 성능 평가 결과 문서
 ┗ 📜 .gitignore        # Git 추적 제외 파일 설정
```

---

## 11. 시스템 아키텍처
<div align="center">
  <img src="./docs/images/Architecture.png" width="800px" alt="Credit Card Churn ERD">
</div>

자세한 구조 및 설명은 [Project Wiki]()를 참고하세요.

---

## 12. 결론
🚀 기대 효과   
본 프로젝트는 머신러닝 알고리즘을 통해 고객의 '조용한 이탈 시그널'을 사전에 포착하고, 이를 실제 비즈니스 전략으로 연결하는 엔드투엔드(End-to-End) 파이프라인을 구축해 본 것에 큰 의의가 있습니다. 제안된 **'세그먼트별 맞춤형 카드 라인업 전략'**이 도입될 경우 다음과 같은 성과를 기대할 수 있습니다.

- 고객 생애 가치(LTV) 보존 및 수수료 방어:   
 리워드 기반 라인업(Entry → Cashback → Premium)을 통해 고객의 일상 소비를 자사 카드로 고정시켜 이탈을 방어하고, 안정적인 가맹점 수수료 수익을 확보할 수 있습니다.

- 핵심 금융 수익 극대화:   
 행동 기반 라인업(Installment, Revolving)을 통해 고액 결제 부담을 느끼는 위험군 고객에게 상환 유연성을 제공함으로써, 연체 리스크를 관리하는 동시에 카드사의 주요 수익원인 이자 수익을 극대화하는 선순환 구조를 완성합니다.

🏁 결론    
본 프로젝트는 5개의 다양한 머신러닝 모델을 직접 학습하고 비교 분석하여, 고객 정보를 입력하면 실시간으로 이탈 확률(%)을 확인할 수 있는 예측 시스템을 구현해 냈습니다. 이는 단순히 모델의 '예측 정확도'를 높이는 기술적 성취에만 머물지 않고, 우리가 배운 데이터 기술을 실제 비즈니스 문제 해결에 어떻게 적용할 것인가를 치열하게 고민해 본 시간이었습니다.

우리는 구축된 예측 모델과 데이터 분석을 통해, 고객의 이탈이 어느 날 갑자기 일어나는 우발적 변심이 아니라 '거래 빈도 감소'와 '비활성 기간 증가'라는 명확하고 점진적인 시그널을 동반한다는 사실을 데이터로 입증했습니다. 즉, 머신러닝 알고리즘을 활용해 단순한 확률 계산을 넘어 고객 행동 이면에 숨겨진 맥락을 짚어내고자 노력했습니다.

결론적으로 이번 프로젝트는 머신러닝 모델로 이탈률을 예측해보고, 그 결과를 바탕으로 세그먼트별 고객 전략을 직접 고민해 본 의미 있는 시도였습니다. 비록 마스킹된 데이터를 활용한 실험이었지만, 데이터 분석이 어떻게 실제 서비스 아이디어로 연결될 수 있는지 그 가능성을 직접 체감해 볼 수 있었던 값진 경험이었습니다.

⚠️ 한계점 및 향후 과제   
본 프로젝트는 데이터 기반의 유의미한 이탈 방어 전략을 도출해냈으나, 데이터의 특성과 분석 환경에 따른 아래와 같은 한계점이 존재하며 이를 향후 과제로 남겨두고 있습니다.

- 실제 금융 환경과의 간극 (마스킹 데이터의 한계):     
본 프로젝트에 사용된 데이터셋은 비식별화(Masking) 처리된 오픈 데이터입니다. 따라서 도출된 임계치나 전략을 실제 카드사의 비즈니스 환경에 그대로 적용하기에는 한계가 있으며, 실무 도입 시 실제 고객 데이터를 활용한 추가 검증 및 미세 조정(Calibration) 과정이 필수적입니다.

- 결측치(Unknown) 보간 및 고도화 작업의 진행:     
현재 고객의 인구통계학적 특성 중 소득(Income)과 학력(Education) 피처에 존재하는 'Unknown' 값들을 단순히 삭제하지 않고, 머신러닝을 통해 유의미한 값으로 예측하여 채워 넣는 작업을 진행 중입니다.

해당 결측치 예측 모델링이 최종 완료되면, 앞서 유의미하지 않다고 판단되었던 '고객 특성' 변수들이 이탈에 미치는 잠재적 영향을 조금 더 정교하게 재평가할 수 있을 것으로 기대합니다.

---

## 13. 프로젝트 회고

### 개인 회고
<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 20%; border: 1px solid #ddd; padding: 10px;">이름</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">서민혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">데이터 파이프라인 구축과 XGBoost 기반 Income 모델링을 수행하며 안정적인 데이터 흐름을 설계하고, 예측 성능 향상에 기여할 수 있었다. 또한 Unknown 결측치에 대해 클러스터링 등 다양한 방법을 적용해 클래스 예측을 시도하며 데이터 품질 개선에도 의미 있는 경험을 쌓았다.
이번 프로젝트를 통해 개념 설계, 논리 설계, 물리 설계 단계에서 각각 무엇을 고려해야 하는지에 대한 이해가 크게 향상되었다. 특히 모델 성능이 기대만큼 나오지 않을 때, 단순히 파라미터 조정에 집중하기보다 feature를 시각화하며 데이터의 구조를 직접 해석하는 과정이 중요하다는 것을 깨달았다. 이를 통해 예측이 어려운 원인을 분석하고, 보다 나은 모델링 방향을 도출할 수 있다는 점에서 큰 성장을 느낄 수 있었다.
다음 프로젝트에서는 보다 적극적으로 가설을 수립하고, 시각화를 기반으로 모델링 결과를 사전에 예측해보는 과정을 반복해보고자 한다. 이러한 접근을 통해 모델 성능에 대한 이해도를 높이고, 보다 개선된 결과를 도출할 수 있을 것이라 기대한다.
</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">유동현</td>
            <td style="border: 1px solid #ddd; padding: 10px;">HistGradientBoosting 기반 예측 모델과 streamlit frontend 구축에 기여하였습니다. 이번 프로젝트에서 다양한 분야의 구현을 접할 수 있었습니다. 또한 Git을 다루는 방법을 팀원으로부터 배울 수 있어서 스스로의 협업 환경의 개발 능력을 강화할 수 있었던 것 같습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">XGBoost 모델 구축에 참여하며 끈기와 협업의 가치를 배웠습니다. 팀원 간 운영체제가 달라 기존에 익숙했던 것과 전혀 다른 환경을 세팅해야 했고, 이 과정에서 예상치 못한 어려움과 마주했습니다. 심리적으로 지치기도 했지만, 조원들과 소통하고 도움을 받으며 끝까지 모델 구축을 해냈습니다.이후 README 작성하며, 개발 단계에서 미처 따라가지 못했던 전체적인 파이프라인과 데이터 흐름을 숙지할 수 있었습니다. 
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">전종혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">초기 Streamlit 디자인부터(Figma), 환경 구축에 사용되는 기술이 무엇인지를 팀원들에게 간단히 설명하고, 기능 개발과 점점 자리를 잡아가는 프로젝트의 흐름에 따라, Streamlit(프론트)에 대한 구성 요소들을 정리하고, 구현했으며, EDA와 상관관계 분석을 통해 데이터셋에 대해 전반적인 이해가 필요했는데, 이 부분을 EDA하는 과정에서 많이 이해하게 되었고, 이를 통해서 데이터 전처리(One-Hot Encoding)를 진행하게 되었습니다. 전처리 이후에는, EasyEnsemble 모델을 통해 정확도에 집중하기 보다는 Recall에 집중하여 해보고 싶은 욕심에, EasyEnsemble 모델을 선택하게 되었습니다. 비록 파라미터 값의 조정 실패로 제출 시에는 99에서 90으로 하락했지만, 아직 보완할 점이 많다는 것을 느꼈습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">정영일</td>
            <td style="border: 1px solid #ddd; padding: 10px;">이번 프로젝트에서 전체 흐름을 설계하고 방향성을 구체화하는 역할을 맡아 수행했다. 단순히 개별 분석 결과를 정리하는 데 그치지 않고, 프로젝트가 어떤 문제를 다루고 어떤 메시지를 전달해야 하는지에 대해 지속적으로 고민하며 전체 구조를 잡아가고자 했다. 특히 이탈 분석을 단순한 현상 분석으로 끝내지 않고, 고객 유지 중심의 관점으로 확장하여 프로젝트의 방향성을 설정한 점이 주요 기여라고 생각한다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">조동휘</td>
            <td style="border: 1px solid #ddd; padding: 10px;">이번 프로젝트를 진행을 하면서 개인적으로는 실패한 프로젝트라고 회고를 남기고 싶다 구체적인 이유는 기술을 도입하는 입장에서 기술에 대한 설명을 해야되는 입장에서 선조치후보고식으로 도입을 해와서 개발 난이도를 조절을 해야되는 입장에서 가장 큰 실수를 저질렀다고 말할 수가 있었다. 그리고 연락을 신경을 써야되는 입장에서 연락을 자주 못해서 개발의 진척도 공유와 현재 개발단계에서 완료되었다는 것을 알려주지 못해서 남들이 완벽한 프로젝트라고 평을해도 개인적으로는 실패한 프로젝트라고 평을 내리고 싶다.
            팀원들이 믿고 따라와 주셔서 감사할 따름이다.</td>
        </tr>
    </tbody>
</table>


---


### 팀원 회고

<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">서민혁</td>
            <td style="text-align: center; border: 1px solid #ddd;">유동현</td>
            <td style="border: 1px solid #ddd; padding: 10px;">XGBoost를 활용해서 Income 예측과 EDA streamlit을 하는 파트를 담당하였습니다. 데이터 탐색부터 모델링까지 일관된 흐름으로 작업을 구성한 점이 좋았습니다. 예상치 못한 문제 상황에서도 침착하게 대응하여 프로젝트 진행에 안정적으로 기여했습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">XGBoost를 활용한 Income 예측 모델링과 Streamlit 기반의 EDA 파트를 담당하시며, 데이터 탐색부터 모델링까지 일관되고 완성도 높은 작업 흐름을 보여주셨습니다. 배움의 열정이 남다르셔서 정규 시간이 끝난 후에도 남아서 동휘님, 동현님께 적극적으로 질문하며 하나라도 더 알아가려 하시는 모습은 저에게도 긍정적인 자극이 되었습니다. 또한, 특유의 밝고 활달한 성격으로 서먹했던 팀원들 사이의 든든한 다리 역할을 해주셔서 프로젝트 내내 즐거운 분위기 속에서 협업할 수 있었습니다.
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">전종혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 과정에서 결측치라고 생각될 수 있는 부분에 대해 모델 개발(XGBoost)을 하면서, 필요한 정보를 얻을 수 있게 되었습니다. 모델 개발을 하면서 스스로 모델 개발에 대해서 사고해보고, 모르는 부분을 공부하는 모습이 인상 깊었습니다. 부족하지만 따라오려고 노력하는 모습이 매우 인상깊었습니다. 협업 도구가 익숙치 않은데도, 잘 사용해주셨습니다.
</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">정영일</td>
            <td style="border: 1px solid #ddd; padding: 10px;">서민혁님은 프로젝트 전반에서 능동적으로 참여하며 팀의 흐름을 주도적으로 이끌어간 팀원이었다. 특히 프로젝트 초반 단계에서 다양한 아이디어를 빠르게 제시하며 전체 방향성을 설정하는 데 기여한 점이 인상적이었다. 이러한 태도는 팀이 초기 방향 설정에서 머뭇거리지 않고 빠르게 실행 단계로 넘어갈 수 있도록 만드는 데 중요한 역할을 했다고 생각한다. 또한 단순히 아이디어 제시에 그치지 않고 실제 작업에도 적극적으로 참여하며 프로젝트 진행 속도를 높이는 데 기여하였다. 논의 과정에서도 활발하게 의견을 공유하며 팀원 간의 대화를 자연스럽게 이끌었고, 이러한 점은 협업 환경에서 긍정적인 분위기를 형성하는 데 도움이 되었다. 전반적으로 프로젝트의 추진력과 실행력을 높이는 데 의미 있는 역할을 수행한 팀원이었다고 생각한다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">조동휘</td>
            <td style="border: 1px solid #ddd; padding: 10px;">
            요번 프로젝트를 하시면서 보이지 않는 개발 단계에서 많이 노력하신 팀원이라고 평가를 내려주고 싶다.
            처음 배우고 활용하는 부분에서 주도적으로 도입을 해야되나 망설여 지는 부분을 옆에서 도움을 많이 주셔서 환경 설정 및 개발의 난이도를 결정하는데 큰 도움이 되었고
            또한 Known Columns에 대해서 Clustring, Classification을 도맡아서 하겠다 하셔서
            모델을 분류해야되는 어려움이 조금은 떨어져서 도움이 되셨다.
            </td>
        </tr>
    </tbody>
</table>
<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">유동현</td>
            <td style="text-align: center; border: 1px solid #ddd;">서민혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">Streamlit 기반 UI 구현과 HistGradientBoosting 모델 적용을 통해 사용자 접근성과 모델 활용성을 향상시킴. 담당 영역을 넘어 팀 전반을 지원하며 프로젝트 전반에 걸쳐 높은 기여도를 보임.
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">HistGradientBoosting 예측 모델과 Streamlit 기반 UI를 성공적으로 구현하여, 저희 프로젝트의 사용자 접근성과 모델 활용도를 크게 높여주셨습니다. 본인의 담당 영역을 완벽하게 소화하는 것을 넘어, 프로젝트 전반에 걸쳐 팀원들을 기꺼이 지원해 주신 덕분에 전체적인 완성도가 훌쩍 높아졌습니다. 특히 본인의 개발 분량만으로도 벅차고 바쁘셨을 텐데, 비전공자인 저에게 어려운 부분들을 항상 친절하고 알기 쉽게 설명해 주셨습니다. </td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">전종혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 도중 발생한 모델 개발(HistGradientBoosting)과 상관관계 분석을 하며, 단순하게 생각하기보다는 논리적으로 파고들어 데이터의 결측치라고 생각할 수 있는 것들을 모두에게 이해할 수 있도록 도움을 주셨습니다. 프론트 구조를 얘기하면서 보조해주셔서 많은 것을 개선해 나갈 수 있었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">정영일</td>
            <td style="border: 1px solid #ddd; padding: 10px;">유동현님은 프로젝트 결과를 효과적으로 전달하는 데 있어 중요한 역할을 수행한 팀원이었다. 특히 분석 결과를 시각적으로 구조화하여 표현하는 과정에서 높은 완성도를 보여주었으며, PPT 전반의 흐름을 자연스럽게 구성하는 데 기여한 점이 인상적이었다. 기술 설명 파트에서도 내용을 안정적으로 정리하여 전달함으로써, 프로젝트의 핵심 내용을 청중이 이해하기 쉽게 만드는 데 도움을 주었다. 단순한 자료 정리에 그치지 않고, 전체적인 발표 흐름을 고려하여 구성 요소를 조정하는 모습에서 높은 책임감과 완성도를 느낄 수 있었다. 또한 팀원 간의 의견을 조율하고 흐름을 연결하는 역할도 수행하며 협업 과정에서 긍정적인 영향을 주었다. 결과적으로 프로젝트의 ‘보여지는 완성도’를 높이는 데 중요한 기여를 한 팀원이었다고 생각한다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">조동휘</td>
            <td style="border: 1px solid #ddd; padding: 10px;">유동현님은 본인이 맞은 모델링과 개발 범위 이외에 다른 부분도 솔선수범해서 진행을 해주셔서 개발 진척이 조금은 빠르게 진행이 되도록 해주셔서 좋았습니다.
            HistGradientBoosting모델링을 하시면서 여러번의 하이퍼 파라미터 튜닝을 해주셔서
            mlflow를 도입하는 프로젝트에서 왜 도입을 해야되는지를 명확하게 보여줄 수 있어서 큰 도움이 되어주셨습니다.
            Streamlit을 진행을 하시면서 디자인을 제시해주시면서 UI/UX를 이용자에게 친화적으로 설계를 해주셔서 프로젝트를 발표하는데 다른 조와는 다르게 접근이 가능하게 만들어 주셨습니다.
            발표를 하실 때 기술적인 부분을 처음 사용하는 부분이 있었지만 다른 분들에게 전달을 해야되는 내용을 전달을 해주셔서 "프로젝트를 완벽하게 전달이 되었다."라고 말할 수 있게 만들어 주신 팀원이였다.
            </td>
        </tr>
    </tbody>
</table>
<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">윤정연</td>
            <td style="text-align: center; border: 1px solid #ddd;">서민혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트 문서화 및 XGBoost 모델 정리를 통해 결과 해석과 협업 효율을 체계적으로 지원함. EDA 과정에서 데이터 간 관계를 명확히 도출하여 모델링 방향 설정에 기여함.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">유동현</td>
            <td style="border: 1px solid #ddd; padding: 10px;">XGBoost를 활용해서 Churn 예측을 하는 파트를 담당하여 정확도 높은 모델을 정제해냈습니다. 하이퍼파라미터 튜닝과 feature importance 분석을 통해 모델 성능을 개선하려는 노력이 돋보였습니다. 결과의 신뢰도를 높이기 위한 검증 과정도 성실하게 수행한 점이 인상적이었습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">전종혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트를 진행하면서 이해가 안되는 부분들을 이해하려고 하면서 질문들도 많이 해주시고, 덕분에 저도 정립이 되지 않던 것들을 확실히 하게 되었습니다. 협업 도구에 대해서 많이 배우려고 하셨고, 어려운 모델 개발(XGBoost)을 다 한 명씩 도맡아 하다보니, 많이 버거우셨을 수도 있을텐데, 이 부분을 따라오려고 혼자 공부하고 노력해주셨습니다. 서류 작업 전반을 담당해주셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">정영일</td>
            <td style="border: 1px solid #ddd; padding: 10px;">윤정연님은 프로젝트의 내용을 정리하고 구조화하는 과정에서 중요한 역할을 수행한 팀원이었다. 특히 분석 결과와 한계점, 그리고 전반적인 흐름을 논리적으로 정리하여 프로젝트의 메시지가 명확하게 전달될 수 있도록 기여한 점이 인상적이었다. 복잡한 내용을 단순히 나열하는 것이 아니라, 흐름에 맞게 재구성하여 전달력을 높이려는 노력이 돋보였으며, 이러한 부분은 전체 결과물의 완성도를 높이는 데 큰 도움이 되었다. 또한 작업 과정에서 어려움이 있었을 것으로 보이는 상황에서도 끝까지 책임감을 가지고 맡은 부분을 완수하려는 태도가 인상 깊었다. 프로젝트 후반까지 안정적으로 결과물을 정리해낸 점에서 팀에 대한 기여도가 높았다고 생각한다.
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">조동휘</td>
            <td style="border: 1px solid #ddd; padding: 10px;">윤정연님은 프로젝트에서 Xgboost를 모델링과 EDA를 진행해 주시면서 처음 코딩을 배우고 프로젝트를 하시는 팀원이였는데 조금은 무리한 내용을 부탁드려도 대충해서 완료했다고 말하기보다는 못하는 부분을 팀원들에게 물어보면서 진행을 해주셔서 개발룰을 작성한 작성자의 입장에서는 죄송하고 감사한 마음이 들었습니다.
            프로젝트의 후반으로 들어옴에 따라서 문서화를 부탁드렸는데 기본적인 틀과 내용이 최소한으로 수정을 하면 될 정도로 높은 완성도를 보여주었습니다.
            그 덕분에 README를 작성하는 기간이 수월하게 줄어들어서 큰 도움이 되셨습니다.</td>
        </tr>
    </tbody>
</table>
<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">전종혁</td>
            <td style="text-align: center; border: 1px solid #ddd;">서민혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">Streamlit 화면 구성과 EasyEnsemble 적용으로 불균형 데이터 문제를 효과적으로 해결하고 서비스 시각화를 담당함. 물리 설계 단계에서 팀원들의 이해를 도우며 프로젝트가 원활하게 진행되도록 기여함.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">유동현</td>
            <td style="border: 1px solid #ddd; padding: 10px;">streamlit을 활용한 front 구축을 주도하였습니다. HTML과 Figma를 활용해 UI/UX를 체계적으로 설계하고 서비스 형태로 구현한 점이 인상적이었습니다. 사용자 관점에서 직관적인 인터페이스를 고민한 부분이 잘 드러났습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">데이터 모델링부터 UI/UX 기획까지, 프로젝트 전반을 아우르는 종혁님의 폭넓은 기술적 역량 덕분에 서비스의 완성도가 크게 높아졌습니다. Figma와 Streamlit을 활용해 직관적이고 깔끔한 화면 구성을 도맡아 주셨습니다. 또한 팀원들이 어려움을 겪고 있을 때면 세심하게 관찰하시다가, 조용히 다가와 실질적인 해결책을 제시해 주시는 훌륭한 모습을 보여주셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">정영일</td>
            <td style="border: 1px solid #ddd; padding: 10px;">전종혁님은 프로젝트의 기술적 구현과 분석 과정 전반에 걸쳐 적극적으로 참여한 팀원이었다. 데이터 특성을 고려하여 적절한 모델을 적용하고, 결과를 해석하는 과정에서도 의미 있는 의견을 제시하며 프로젝트의 방향성을 구체화하는 데 기여하였다. 단순히 맡은 작업을 수행하는 것을 넘어, 결과에 대한 해석과 개선 방향에 대해서도 지속적으로 고민하는 모습을 보여주었으며, 이러한 점은 전체 프로젝트의 완성도를 높이는 데 중요한 역할을 했다고 생각한다. 또한 팀원들과의 소통 과정에서도 자신의 의견을 명확하게 전달하며 논의의 깊이를 더하는 데 기여하였다. 전반적으로 기술적인 완성도와 논리적인 접근 모두에서 긍정적인 영향을 준 팀원이었다고 생각한다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">조동휘</td>
            <td style="border: 1px solid #ddd; padding: 10px;">전종혁님은 프로젝트 진행 과정에서 제가 부족한 부분을 채워주시는 역할도 같이 수행해주셔서
            팀에서 목표로 했던 개발 단계를 안정적으로 완수하는 데 가장 큰 기여를 해주셨습니다.
            특히 유동현님과 함께 Streamlit 개발을 지속적으로 이어가며,
            중간에 발생한 긴급한 디자인 요청에도 빠르게 대응해 주셔서
            프로젝트의 완성도와 사용자 경험을 높이는 데 큰 도움이 되었습니다.
            또한 EasyEnsemble 모델링을 진행하면서 Mlflow 환경의 문제점을 함께 찾아주셔서,
            제가 수정해야 할 부분을 명확하게 파악할 수 있었고
            전체적인 개발환경에 문제점을 빠르게 알려주어서 환경을 설정하는 입장에서 많은 도움을 받았습니다.
            </td>
        </tr>
    </tbody>
</table>
<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">정영일</td>
            <td style="text-align: center; border: 1px solid #ddd;">서민혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">Logistic Regression 기반 모델링과 발표를 통해 프로젝트 결과를 명확하게 전달하고 방향성을 제시함. 특히 결론 도출 과정에서 논리적 흐름을 정리하여 의사결정에 중요한 역할을 수행함.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤동현</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트를 경영적으로 분석할 수 있는 새로운 관점을 제시하는 것으로 프로젝트가 단순 공학의 영역에서 머물지 않고 경영적인 확장을 고려할 수 있도록 해주었습니다. 기술 중심으로 흐르기 쉬운 논의를 비즈니스 가치 중심으로 정리해주는 역할이 인상적이었습니다. 데이터 결과를 실제 의사결정에 연결하려는 시도가 프로젝트 완성도를 높이는 데 기여했습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">단순한 모델링을 넘어, 프로젝트가 가져다줄 '사용자 가치'와 '비즈니스적 의미'를 끊임없이 고민하게 만들어주신 분입니다. 탄탄한 인문학적 소양을 바탕으로 프로젝트의 기획적 완성도를 크게 높여주셨고, 덕분에 기술이 실제 서비스로 어떻게 이어져야 하는지 깊이 있게 배울 수 있었습니다. 더불어 청중의 눈높이에 맞춘 흡입력 있는 발표 능력은, 우리 프로젝트의 매력을 최대로 전달해주셨습니다. </td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">전종혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트때 사용하는 데이터에 대해 접근하는 방법을 새로이 제시해주셨습니다. 덕분에 EDA를 풍부하게 할 수 있었던 것 같습니다. 금융이나 카드사 데이터의 변수를 읽을 때 이해가 되지 않던 부분들이 많았는데, 이 부분이 덕분에 해소되었습니다. 확장해서 서비스를 하게 될 때, 이 부분이 많은 도움이 될 것 같습니다. 모델 개발(Logistic Regression)에도 도움을 주셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">조동휘</td>
            <td style="border: 1px solid #ddd; padding: 10px;">
                정영일님은 프로젝트의 전반적인 기획 방향을 제시하고,
                발표를 체계적으로 준비하여 프로젝트를 효과적으로 전달하는 데 기여하셨습니다.
                프로젝트의 EDA를 하시면서 모델링을 어떠한 방향으로 해야되는지를 명확하게 지목을 해주셔서 모델링을 하는 입장에서 가장 큰 도움을 받았습니다.
                체계적으로 준비가 되어서 프로젝트가 어떠한 방향성을 가지고 있으며 어떠한 개발을 했는지를 원하는대로 전달이 되었으며,
                프로젝트의 사업성과 해당 프로젝트로 뭘 할 수 있는지를 함께 보여줄 수 있도록 발표를 구성하여서 프로젝트의 발표가 성공적으로 되게 큰 도움을 주셨습니다.
                또한 Logistic Regression을 프로젝트의 목표에 맞께금 모델링을 해주셔서 
                개발을 하는 부분에서도 도움이 많이 되셨습니다.
            </td>
        </tr>
    </tbody>
</table>
<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd; margin-bottom: 30px;">
    <thead>
        <tr style="background-color: #f8f9fa;">
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">대상자</th>
            <th style="width: 15%; border: 1px solid #ddd; padding: 10px;">작성자</th>
            <th style="border: 1px solid #ddd; padding: 10px;">회고 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5" style="text-align: center; font-weight: bold; border: 1px solid #ddd;">조동휘</td>
            <td style="text-align: center; border: 1px solid #ddd;">서민혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">데이터 파이프라인 설계 및 LightGBM 모델링을 통해 안정적인 데이터 처리와 성능 개선에 기여함. 프로젝트 초기 환경설정과 개념·논리 구조를 정립하여 전체적인 방향성을 잡는 데 핵심적인 역할을 수행함.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">유동현</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트의 환경을 전담으로 구축하였습니다. Docker Compose와 FastAPI를 활용해 안정적인 개발 및 실행 환경을 구성했습니다. 팀원들이 개발에 집중할 수 있도록 인프라 기반을 탄탄하게 마련한 점이 큰 기여였습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">윤정연</td>
            <td style="border: 1px solid #ddd; padding: 10px;">LightGBM 예측 모델링을 훌륭하게 수행하셨을 뿐만 아니라, 프로젝트의 초기 환경 구축부터 전체적인 리딩까지 팀의 기둥 역할을 해주셨습니다. 커밋을 올릴 때마다 꼼꼼한 피드백을 남겨주신 덕분에 제 코드의 퀄리티도 한층 높아질 수 있었습니다. 특히 프로젝트 막바지에 체력적으로 많이 지치고 컨디션이 안 좋으셨음에도 불구하고 끝까지 잘 마무리 할 수 있도록 도와주셨습니다</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">전종혁</td>
            <td style="border: 1px solid #ddd; padding: 10px;">프로젝트의 전반적인 환경 구축, 인프라를 담당해주셨습니다. 개발 도중 환경의 미스매치로 인한 딜레이가 생기지 않도록 해주셔서, 편리하게 개발할 수 있었습니다. 다양한 기술들을 활용 하다보니, 구축한 환경에 대해 세부적인 설명이 더 있었다면 좋았을 것 같습니다. 새로운 기술들을 많이 알게 되어 좋았습니다. 인프라 구축과 동시에 모델 개발(LightGBM)까지 하셨습니다.</td>
        </tr>
        <tr>
            <td style="text-align: center; border: 1px solid #ddd;">정영일</td>
            <td style="border: 1px solid #ddd; padding: 10px;">조동휘님은 데이터 전처리와 모델링을 중심으로 프로젝트의 핵심적인 분석을 안정적으로 수행한 팀원이었다. 데이터의 특성을 고려하여 체계적으로 작업을 진행하였으며, 분석 결과를 기반으로 의미 있는 인사이트를 도출하는 과정에서 중요한 역할을 수행하였다. 특히 다양한 지표를 활용하여 모델의 성능을 검증하고 결과를 비교하는 등 분석 과정 전반에서 꼼꼼한 접근이 인상적이었다. 또한 자신이 수행한 내용을 팀원들과 공유하는 과정에서도 이해하기 쉽게 설명하려는 노력이 돋보였으며, 이는 협업 과정에서 전체적인 이해도를 높이는 데 도움이 되었다. 전반적으로 프로젝트의 ‘분석 기반’을 안정적으로 구축하는 데 기여한 팀원이었다고 생각한다.</td>
        </tr>
    </tbody>
</table>
