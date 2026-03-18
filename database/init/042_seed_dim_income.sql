/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 042_seed_dim_income

Purpose:
- dim income 테이블 seed 데이터

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
    dim_income (
        income_id,
        income_label,
        income_min,
        income_max,
        sort_order
    )
VALUES (
        1,
        'Less than $40K',
        0,
        40000,
        1
    ),
    (
        2,
        '$40K - $60K',
        40000,
        60000,
        2
    ),
    (
        3,
        '$60K - $80K',
        60000,
        80000,
        3
    ),
    (
        4,
        '$80K - $120K',
        80000,
        120000,
        4
    ),
    (5, '$120K +', 120000, NULL, 5),
    (6, 'Unknown', NULL, NULL, 99);

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;