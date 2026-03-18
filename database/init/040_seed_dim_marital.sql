/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 040_seed_dim_marital

Purpose:
- dim_marital 테이블에 라벨링 데이터 입력

Author: 조동휘
Created: 2026-03-08

Updated:
- 2026-03-08: initial version
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

INSERT INTO
    dim_marital (
        marital_id,
        marital_label,
        sort_order
    )
VALUES (1, 'Single', 1),
    (2, 'Married', 2),
    (3, 'Divorced', 3),
    (4, 'Unknown', 99);

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;