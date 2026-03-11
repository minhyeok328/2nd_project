/* =========================================================================
Project:
- creditcard_churn

Module:
- init

File: 071_create_prediction_views.sql

Purpose:
- prediction 결과 조회용 view 생성

Author: 조동휘
Created: 2026-03-09

Updated:
- 2026-03-09: initial version
========================================================================= */

START TRANSACTION;

USE creditcard_churn_db;

-- =========================================================
-- CREATE VIEW: vw_creditcard_churn_predictions
-- description: 원본 label과 prediction 결과 비교용 view
-- =========================================================

CREATE OR REPLACE VIEW vw_creditcard_churn_predictions AS
SELECT
    c.creditcard_churn_id,
    c.education_id AS original_education_id,
    p.prediction_education_id AS predicted_education_id,
    c.income_id AS original_income_id,
    p.prediction_income_id AS predicted_income_id
FROM
    creditcard_churn c
    LEFT JOIN creditcard_churn_predictions p ON c.creditcard_churn_id = p.creditcard_churn_id;

COMMIT;