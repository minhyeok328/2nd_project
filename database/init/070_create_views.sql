/* =========================================================================
Project:
- project-name

Module:
- init  

File: 070_create_views.sql

Purpose:
- view를 생성하는 SQL 스크립트입니다.

Author: 조동휘
Created: 2026-03-09

Updated:
- 2026-03-09: initial version (조동휘)
========================================================================= */

START TRANSACTION;

USE creditcard_churn_db;

-- =========================================================
-- CREATE VIEW: Credit Card Churn
-- description: 신용카드 해지 고객의 정보를 담은 뷰입니다. (ML 모델링에 사용)
-- =========================================================
CREATE OR REPLACE VIEW vw_creditcard_churn_ml AS
SELECT
    creditcard_churn_id,
    churn_status AS churn,
    age,
    gender,
    dependents,
    education_id,
    marital_id,
    income_id,
    card_type_id,
    relationship_months,
    product_count,
    inactive_months,
    contact_count,
    credit_limit,
    revolving_balance,
    available_credit,
    amount_change,
    count_change,
    transaction_amount,
    transaction_count,
    utilization_ratio
FROM creditcard_churn;

COMMIT;