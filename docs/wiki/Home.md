# 📊 Project Overview
본 프로젝트는 **신용카드 고객 데이터를 기반으로 고객 이탈(Churn)을 예측하는 Machine Learning 시스템**을 구축하는 것을 목표로 합니다.

## 🎯 프로젝트 주요 기능
* 고객 행동 패턴 분석 및 세그먼트 분석 (Clustering)
* 고객 이탈 예측 모델 개발
* Streamlit 기반 예측 서비스 제공
* MLflow 기반 실험 관리

---

## 💾 Dataset
본 프로젝트는 Kaggle에서 제공하는 [Credit Card Customers 데이터셋](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)을 사용합니다.

### 📌 Target Variable
`Attrition_Flag` (이탈 여부)
* **Existing Customer** (유지 고객)
* **Attrited Customer** (이탈 고객)

### 📊 주요 Feature
| Feature | 설명 |
| :--- | :--- |
| `Customer_Age` | 고객 나이 |
| `Income_Category` | 소득 수준 |
| `Months_on_book` | 고객 유지 기간 |
| `Total_Trans_Amt` | 총 거래 금액 |
| `Total_Trans_Ct` | 총 거래 횟수 |
| `Avg_Utilization_Ratio` | 카드 사용 비율 |

---

## 🚀 Project Development Phases

* **Phase 0 (Baseline System):** 데이터 EDA, Feature Engineering, 기본 Churn 예측 모델, Streamlit 기본 구현
* **Phase 1 (System Extension):** GPU 학습 실험, MLflow 도입, 모델 성능 비교 및 최적화
* **Phase 2 (Production-ready):** 모델 해석(SHAP), Threshold 최적화, 파이프라인 정리, Streamlit 서비스 고도화