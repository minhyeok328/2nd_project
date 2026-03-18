# Model Evaluation Report

## 1. 개요 (Overview)

- **모델명**: XGBoost Income Classification Model  
- **목적**: 고객 데이터 기반 **Income Level 예측 및 Unknown Income 보정**  
- **평가 일자**: 2026-03

본 모델은 고객의 속성 데이터를 활용하여 **Income 범주를 예측하기 위한 XGBoost 기반 분류 모델**이다.  
특히 데이터셋 내 존재하는 **Unknown Income 값을 추정하기 위한 모델링 과정의 성능 평가**를 주요 목적으로 한다.

모델링 과정은 다음과 같은 절차로 진행되었다.

1. 데이터셋에서 **Income 값이 존재하는 데이터(known)**와 **Income 값이 없는 데이터(unknown)**를 분리하였다.
2. **known 데이터만 사용하여 모델을 학습 및 평가**하였다.
3. 학습된 모델을 이용해 **unknown 데이터의 income을 예측**하는 방식으로 접근하였다.
4. 초기 **multi-class 분류 성능이 낮게 나타남**을 확인하였다.
5. Income 분포 시각화 결과 **1,2와 3,4,5 그룹 간 특성이 유사**하여 정확한 분류가 어려운 것으로 판단하였다.

이에 따라 **Income을 Low / High 두 그룹으로 재구성하는 방식의 모델링 전략**을 설계하였다.

- **Low Income** : 1, 2  
- **High Income** : 3, 4, 5  

단, 해당 전략은 **현재 개발 단계에서는 실험 수준으로만 검증되었으며 실제 모델 파이프라인에는 반영되지 않았다.**  
해당 개선 방식은 **2단계 모델 개발에서 반영될 예정**이다.

---

# 2. 평가 환경 및 데이터 (Environment & Data)

- **데이터셋**: Credit Card Customers Dataset (BankChurners 기반 전처리 데이터)
- **총 데이터 수**: 10,227건
- **학습 데이터**: 7,280건
- **테스트 데이터**: 1,820건
- **Feature 수**: 20개
- **타겟 변수**: `income_id`
- **모델**: XGBoost Classifier

---

## Train / Test Split

| Dataset | Size |
|---|---|
| Train | 7,280 |
| Test | 1,820 |

---

## Income Distribution (Train)

| Income Level | Count |
|---|---|
| 1 | 2859 |
| 2 | 1443 |
| 3 | 1142 |
| 4 | 1242 |
| 5 | 594 |

---

# 3. 평가 결과 (Evaluation Results)

## Multi-class Income Classification (Test Set)

| Metric | Score |
| :--- | :--- |
| **Accuracy** | **0.5989** |
| Precision | 0.8404 |
| Recall | 0.4704 |
| F1-Score | 0.4607 |
| ROC-AUC | 0.8428 |

---

## Multi-class Income Classification (Train Set)

| Metric | Score |
| :--- | :--- |
| Accuracy | 0.8044 |
| Recall | 0.7481 |
| F1-Score | 0.7615 |
| ROC-AUC | 0.9765 |
| PR-AUC | 0.9108 |

---

## Binary Income Classification (High vs Low Income) - Test Set *(실험 결과)*

| Metric | Score |
| :--- | :--- |
| **Accuracy** | **0.9027** |
| Precision | 0.9007 |
| Recall | 0.9489 |
| F1-Score | 0.8886 |
| ROC-AUC | 0.9676 |

---

## Binary Income Classification (Train Set)

| Metric | Score |
| :--- | :--- |
| Accuracy | 0.9514 |
| Recall | 0.9903 |
| F1-Score | 0.9434 |
| ROC-AUC | 0.9955 |
| PR-AUC | 0.9933 |

---

# 4. 결과 분석 (Analysis)

## 강점

- **Binary Income Classification 실험에서 높은 성능을 확인**
  - Test Accuracy **90% 이상**
  - ROC-AUC **0.96 이상**
- 고객 특성 데이터를 활용한 **Income 수준 예측 가능성 확인**
- **GridSearch 기반 XGBoost 하이퍼파라미터 튜닝 수행**

---

## 약점

- **Multi-class Income 분류 성능은 상대적으로 낮음**
  - Test Accuracy 약 **0.60 수준**
- Income 클래스 간 특성이 유사하여 **클래스 경계가 모호함**
- Train / Test 성능 차이가 존재하여 **일부 Overfitting 가능성**

---

# 5. 향후 개선 방향 (Future Work)

현재 개발 단계에서는 **Multi-class Income 예측 모델을 기준으로 평가가 진행되었다.**  
다만 실험 결과를 바탕으로 다음 개선 사항을 **2단계 모델 개발에 반영할 계획이다.**

### 1. Income 재구성 모델 적용

- Income 5단계 분류 대신  
  **Low / High Binary Classification 모델 적용**
- Unknown Income 예측 성능 향상 기대

---

### 2. Feature Engineering 강화

추가적으로 다음과 같은 고객 행동 기반 변수를 활용할 예정이다.

- 고객 소비 패턴
- 카드 사용 빈도
- 신용 한도 대비 사용 비율 (Utilization Ratio)

---

### 3. 모델 개선

- **LightGBM / CatBoost 모델 비교 실험**
- Ensemble 모델 적용 가능성 검토

---

### 4. 데이터 개선

- Income 클래스 **불균형 문제 완화**
- Unknown 데이터 **추가 학습 전략 적용**

---

## Summary

초기 Multi-class Income 분류에서는 성능이 제한적으로 나타났으나,  
Income을 Low / High로 재구성한 Binary Classification 실험에서는 높은 예측 성능을 확인하였다.

해당 접근 방식은 **2단계 모델 개발에서 실제 모델 파이프라인에 반영될 예정이다.**