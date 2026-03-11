/* =========================================================================
Project:
- project-name

Module:
- init

File: 080_indexes.sql

Purpose:
- description

Author: 조동휘
Created: 2026-03-09

Updated:
- 2026-03-09: initial version (조동휘)
========================================================================= */


START TRANSACTION;

USE creditcard_churn_db;

CREATE INDEX idx_creditcard_churn_education_id
    ON creditcard_churn (education_id);

CREATE INDEX idx_creditcard_churn_marital_id
    ON creditcard_churn (marital_id);

CREATE INDEX idx_creditcard_churn_income_id
    ON creditcard_churn (income_id);

CREATE INDEX idx_creditcard_churn_card_type_id
    ON creditcard_churn (card_type_id);

CREATE INDEX idx_creditcard_churn_predictions_churn_id
    ON creditcard_churn_predictions (creditcard_churn_id);

CREATE INDEX idx_creditcard_churn_predictions_predicted_education_id
    ON creditcard_churn_predictions (prediction_education_id);

CREATE INDEX idx_creditcard_churn_predictions_predicted_income_id
    ON creditcard_churn_predictions (prediction_income_id);

COMMIT;