# =========================================================================
# Project:
# - Credit Card Churn
#
# Module:
# - docker/streamlit
#
# File: Dockerfile
#
# Purpose:
# - streamlit service를 정의하는 Dockerfile
#
# Author: @조동휘
# Created: 2026-03-10
#
# Updated:
# - 2026-03-10: initial version (@조동휘)
# - 2026-03-10: 프로젝트 명 반영 및 이미지 이름 수정 (@조동휘)
# =========================================================================

# =========================================================================
# Stage 1: Builder
#
# Purpose:
# - requirements.txt 기반 wheel 파일 생성
# - 런타임 이미지에는 wheel만 넘겨서 용량 최소화
# =========================================================================
FROM ccc_project_python_base:py312 AS builder

# Container 작업 경로
WORKDIR /app

# streamlit package 목록 복사
COPY requirements.txt .

# requirements.txt 기반 wheel 파일 생성
RUN python -m pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements.txt

# =========================================================================
# Stage 2: Runtime
#
# Purpose:
# - builder에서 만든 wheel만 설치하여 실행 환경 구성
# - 빌드 단계 파일/캐시 제거로 이미지 용량 최소화
# =========================================================================
FROM ccc_project_python_base:py312

# Container 작업 경로
WORKDIR /app

# wheel 파일 복사
COPY --from=builder /wheels /wheels

# wheel 파일로 패키지 설치 후 wheel 제거
RUN python -m pip install --no-cache-dir /wheels/* \
 && rm -rf /wheels

 # Streamlit Container Port 노출
EXPOSE 8501