# =========================================================================
# Project:
# - Credit Card Churn
#
# Module:
# - 머신러닝 CPU 이용 개발환경
#
# File: Dockerfile
#
# Purpose:
# - python:3.12-slim 기반 ML 개발 환경 구축
#
# Author: 조동휘
# Created: 2026-03-05
#
# Updated:
# - 2026-03-05: initial version (조동휘)
# - 2026-03-10: 프로젝트 명 반영 및 image이름 수정 (조동휘)
# =========================================================================


# =========================================================================
# Stage 1: Builder
#
# Purpose:
# - Python 패키지를 wheel 형태로 빌드하는 단계
# - build-essential 등 컴파일 도구는 이 단계에서만 사용
# - 최종 이미지에는 포함되지 않음
#
# Flow:
# - requirements.txt → wheel build → /wheels
#
# Benefits:
# - 이미지 용량 감소
# - 빌드 도구 제거로 보안성 향상
# - 패키지 설치 속도 향상
# =========================================================================
FROM ccc_project_python_base:py312 AS builder

# 컨테이너 내부 작업 디렉토리 설정
WORKDIR /app

# Python Package list file (requirements.txt) copy
COPY requirements.txt .

# requirements.txt 기반 wheel 파일 생성
RUN python -m pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements.txt



# =========================================================================
# Stage 2: Runtime
#
# Purpose:
# - 실제 실행에 필요한 최소 환경 구성
# - builder 단계에서 생성된 wheel 파일만 설치
#
# Flow:
# - builder:/wheels → runtime:/wheels → pip install → site-packages
#
# Benefits:
# - 불필요한 빌드 도구 제거
# - 더 작은 Docker 이미지 생성
# =========================================================================
FROM ccc_project_python_base:py312

# 컨테이너 내부 작업 디렉토리 설정
WORKDIR /app

# builder 단계에서 생성된 wheel 파일 복사
# builder 컨테이너의 /wheels → runtime 컨테이너의 /wheels
COPY --from=builder /wheels /wheels

# wheel 파일을 이용해 Python 패키지 설치
# 설치 위치: /usr/local/lib/python3.12/site-packages
RUN python -m pip install --no-cache-dir /wheels/* \
 && rm -rf /wheels
# wheel 파일 제거로 이미지 용량 최소화