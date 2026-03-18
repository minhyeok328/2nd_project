/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 021_create_feature_table

Purpose:
- ML의 모델 훈련에 직접 사용되는 Table의 생성문

Author: 조동휘
Created: 2026-03-07

Updated:
- 2026-03-07: initial version
- 2026-03-07: creditcard_chur
- 2026-03-09: init SQL 파일 넘버링 재정리 및 헤더 포맷 통일 (조동휘)
=========================================================================
*/

-- -------------------------------------------------
-- MIGRATION INFO
-- id: (예: 2026-02-09_01_init_schema)
-- apply: up section 실행
-- rollback: down section 실행(가능한 범위에서)
-- -------------------------------------------------

/* =======================
UP
======================= */
START TRANSACTION;

USE creditcard_churn_db;

CREATE TABLE creditcard_churn (
    creditcard_churn_id BIGINT UNSIGNED NOT NULL,
    education_id TINYINT UNSIGNED NOT NULL,
    marital_id TINYINT UNSIGNED NOT NULL,
    income_id TINYINT UNSIGNED NOT NULL,
    card_type_id TINYINT UNSIGNED NOT NULL,
    age TINYINT UNSIGNED NOT NULL,
    gender TINYINT UNSIGNED NOT NULL,
    dependents TINYINT UNSIGNED NOT NULL,
    relationship_months SMALLINT UNSIGNED NOT NULL,
    product_count TINYINT UNSIGNED NOT NULL,
    churn_status TINYINT UNSIGNED NOT NULL,
    inactive_months TINYINT UNSIGNED NOT NULL,
    contact_count TINYINT UNSIGNED NOT NULL,
    credit_limit DECIMAL(12, 2) NOT NULL,
    revolving_balance DECIMAL(12, 2) NOT NULL,
    available_credit DECIMAL(12, 2) NOT NULL,
    amount_change DECIMAL(8, 4) NOT NULL,
    count_change DECIMAL(8, 4) NOT NULL,
    transaction_amount DECIMAL(12, 2) NOT NULL,
    transaction_count SMALLINT UNSIGNED NOT NULL,
    utilization_ratio DECIMAL(6, 4) NOT NULL
) ENGINE = InnoDB;

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;