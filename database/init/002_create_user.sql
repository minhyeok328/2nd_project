/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 002_create_user

Purpose:
- 프로젝트에서 사용할 user 생성

Author: 조동휘
Created: 2026-03-07

Updated:
- 2026-03-07: initial version
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

--
USE creditcard_churn_db;

-- DB 전체 관리자 권한 유저
CREATE USER IF NOT EXISTS 'dev_admin'@'%'
    IDENTIFIED BY 'dev_admin_pw';

-- pipeline 적재용
CREATE USER IF NOT EXISTS 'pipeline_insert_user'@'%'
    IDENTIFIED BY 'pipeline_insert_pw';

-- pipeline 출력용
CREATE USER IF NOT EXISTS 'pipeline_select_user'@'%'
    IDENTIFIED BY 'pipeline_select_pw';

COMMIT;

FLUSH PRIVILEGES;

/* =======================
   DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;
