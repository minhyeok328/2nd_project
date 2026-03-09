# =========================================================================
# Project:
# - (직접 입력)
#
# Module:
# - docker
#
# File: docker/database/Dockerfile
#
# Purpose:
# - MySQL 8.0.45 기반 DB 컨테이너
# - utf8mb4 인코딩 / KST 시간대 설정
#
# Author: 조동휘
# Created: 2026-03-05
#
# Updated:
# - 2026-03-05: initial version (조동휘)
# - 2026-03-06: mysql 8.0.45 base + config  (조동휘)
# - 2026-03-09: appleslicon 대응 (조동휘)
# =========================================================================

# MySQL 공식 이미지 사용 (재현성 확보를 위한 버전 명시적 지정)
FROM mysql:8.0.45

# MySQL 서버 설정 (encoding / timezone / sql_mode 등)
COPY my.cnf /etc/mysql/conf.d/my.cnf
