/* =========================================================================
Project:
- creditcard_churn

Module:
- init

File: 010_create_database

Purpose:
- creditcard_churn_db 생성

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

CREATE DATABASE IF NOT EXISTS creditcard_churn_db DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;