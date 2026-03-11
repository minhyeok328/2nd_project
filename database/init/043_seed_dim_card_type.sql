/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 043_seed_dim_card_type

Purpose:
- dim card type 테이블 seed 데이터

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
    dim_card_type (
        card_type_id,
        card_type_label,
        sort_order
    )
VALUES (1, 'Blue', 1),
    (2, 'Silver', 2),
    (3, 'Gold', 3),
    (4, 'Platinum', 4),
    (5, 'Unknown', 99);

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;