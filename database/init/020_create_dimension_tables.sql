/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 020_create_dimension_tables

Purpose:
- creditcard_churn의 label관련 tables

Author: 조동휘
Created: 2026-03-07

Updated:
- 2026-03-07: initial version
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

CREATE TABLE IF NOT EXISTS dim_education (
    education_id TINYINT UNSIGNED NOT NULL,
    education_label VARCHAR(30) NOT NULL,
    sort_order INT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS dim_card_type (
    card_type_id TINYINT UNSIGNED NOT NULL,
    card_type_label VARCHAR(20) NOT NULL,
    sort_order INT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS dim_marital (
    marital_id TINYINT UNSIGNED NOT NULL,
    marital_label VARCHAR(30) NOT NULL,
    sort_order INT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS dim_income (
    income_id TINYINT UNSIGNED NOT NULL,
    income_label VARCHAR(30) NOT NULL,
    income_min INT NULL,
    income_max INT NULL,
    sort_order INT NULL
) ENGINE = InnoDB;

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;