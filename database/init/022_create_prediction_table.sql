/* =========================================================================
Project:
- creditcard_churn

Module:
- init

File: 022_create_prediction_table.sql

Purpose:
- ML 모델이 예측한 education / income 값을 저장하는 테이블

Author: 조동휘
Created: 2026-03-09

Updated:
- 2026-03-09: initial version
========================================================================= */

START TRANSACTION;

USE creditcard_churn_db;

CREATE TABLE IF NOT EXISTS creditcard_churn_predictions (
    prediction_id BIGINT UNSIGNED NOT NULL,
    creditcard_churn_id BIGINT UNSIGNED NOT NULL,
    prediction_education_id TINYINT UNSIGNED NULL,
    prediction_income_id TINYINT UNSIGNED NULL
) ENGINE = InnoDB;

COMMIT;