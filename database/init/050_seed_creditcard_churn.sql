/* =========================================================================
Project:
- (직접 입력)

Module:
- init

File: 050_seed_creditcard_churn

Purpose:
- (예: used_car_db 스키마 생성 / 인덱스 추가 / 마이그레이션)

Author: qazx9
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
    creditcard_churn (
        education_id,
        marital_id,
        income_id,
        card_type_id,
        age,
        gender,
        dependents,
        relationship_months,
        product_count,
        churn_status,
        inactive_months,
        contact_count,
        credit_limit,
        revolving_balance,
        available_credit,
        amount_change,
        count_change,
        transaction_amount,
        transaction_count,
        utilization_ratio
    )

SELECT
    FLOOR(1 + RAND() * 7), -- education
    FLOOR(1 + RAND() * 4), -- marital
    FLOOR(1 + RAND() * 6), -- income
    FLOOR(1 + RAND() * 5), -- card_type
    FLOOR(25 + RAND() * 40), -- age 25~65
    FLOOR(RAND() * 2), -- gender
    FLOOR(RAND() * 5), -- dependents
    FLOOR(6 + RAND() * 60), -- relationship months
    FLOOR(1 + RAND() * 6), -- product count
    FLOOR(RAND() * 2), -- churn
    FLOOR(RAND() * 6), -- inactive months
    FLOOR(1 + RAND() * 4), -- contact count
    ROUND(5000 + RAND() * 20000, 2),
    ROUND(RAND() * 4000, 2),
    ROUND(5000 + RAND() * 20000, 2),
    ROUND(0.5 + RAND(), 4),
    ROUND(0.5 + RAND(), 4),
    ROUND(500 + RAND() * 8000, 2),
    FLOOR(10 + RAND() * 90),
    ROUND(RAND(), 4)
FROM (
        SELECT 1
        UNION
        SELECT 2
        UNION
        SELECT 3
        UNION
        SELECT 4
        UNION
        SELECT 5
        UNION
        SELECT 6
        UNION
        SELECT 7
        UNION
        SELECT 8
        UNION
        SELECT 9
        UNION
        SELECT 10
        UNION
        SELECT 11
        UNION
        SELECT 12
        UNION
        SELECT 13
        UNION
        SELECT 14
        UNION
        SELECT 15
        UNION
        SELECT 16
        UNION
        SELECT 17
        UNION
        SELECT 18
        UNION
        SELECT 19
        UNION
        SELECT 20
        UNION
        SELECT 21
        UNION
        SELECT 22
        UNION
        SELECT 23
        UNION
        SELECT 24
        UNION
        SELECT 25
        UNION
        SELECT 26
        UNION
        SELECT 27
        UNION
        SELECT 28
        UNION
        SELECT 29
        UNION
        SELECT 30
        UNION
        SELECT 31
        UNION
        SELECT 32
        UNION
        SELECT 33
        UNION
        SELECT 34
        UNION
        SELECT 35
        UNION
        SELECT 36
        UNION
        SELECT 37
        UNION
        SELECT 38
        UNION
        SELECT 39
        UNION
        SELECT 40
        UNION
        SELECT 41
        UNION
        SELECT 42
        UNION
        SELECT 43
        UNION
        SELECT 44
        UNION
        SELECT 45
        UNION
        SELECT 46
        UNION
        SELECT 47
        UNION
        SELECT 48
        UNION
        SELECT 49
        UNION
        SELECT 50
        UNION
        SELECT 51
        UNION
        SELECT 52
        UNION
        SELECT 53
        UNION
        SELECT 54
        UNION
        SELECT 55
        UNION
        SELECT 56
        UNION
        SELECT 57
        UNION
        SELECT 58
        UNION
        SELECT 59
        UNION
        SELECT 60
        UNION
        SELECT 61
        UNION
        SELECT 62
        UNION
        SELECT 63
        UNION
        SELECT 64
        UNION
        SELECT 65
        UNION
        SELECT 66
        UNION
        SELECT 67
        UNION
        SELECT 68
        UNION
        SELECT 69
        UNION
        SELECT 70
        UNION
        SELECT 71
        UNION
        SELECT 72
        UNION
        SELECT 73
        UNION
        SELECT 74
        UNION
        SELECT 75
        UNION
        SELECT 76
        UNION
        SELECT 77
        UNION
        SELECT 78
        UNION
        SELECT 79
        UNION
        SELECT 80
        UNION
        SELECT 81
        UNION
        SELECT 82
        UNION
        SELECT 83
        UNION
        SELECT 84
        UNION
        SELECT 85
        UNION
        SELECT 86
        UNION
        SELECT 87
        UNION
        SELECT 88
        UNION
        SELECT 89
        UNION
        SELECT 90
        UNION
        SELECT 91
        UNION
        SELECT 92
        UNION
        SELECT 93
        UNION
        SELECT 94
        UNION
        SELECT 95
        UNION
        SELECT 96
        UNION
        SELECT 97
        UNION
        SELECT 98
        UNION
        SELECT 99
        UNION
        SELECT 100
    ) t;

COMMIT;

/* =======================
DOWN
======================= */
-- 주의: 운영에서는 DOWN이 위험할 수 있음. 필요할 때만 작성.
-- START TRANSACTION;
-- DROP TABLE IF EXISTS ...
-- COMMIT;