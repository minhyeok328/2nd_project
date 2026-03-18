/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 012_grant_privileges

Purpose:
- 011_create_user에서 생성된 유저들 권한 부여

Author: qazx9
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

-- =========================================================
-- dev_admin : DB 전체 관리자 권한
-- =========================================================
GRANT ALL PRIVILEGES ON creditcard_churn_db.* TO 'dev_admin' @'%';

-- =========================================================
-- pipeline_insert_user : 데이터 적재용
-- ETL / 크롤링 / 파이프라인 insert
-- =========================================================
GRANT
INSERT
,
UPDATE ON creditcard_churn_db.* TO 'pipeline_insert_user' @'%';

-- =========================================================
-- pipeline_select_user : 데이터 조회용
-- ML / 분석 / 조회
-- =========================================================
GRANT
SELECT ON creditcard_churn_db.* TO 'pipeline_select_user' @'%';

FLUSH PRIVILEGES;

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;