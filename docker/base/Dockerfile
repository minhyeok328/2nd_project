# =========================================================================
# Project:
# - (직접 입력)
#
# Module:
# - python 3.12 기반 공통 베이스 이미지
#
# File: docker/base/Dockerfile
#
# Purpose:
# - python:3.12-slim 기반 공통 베이스 제공
# - 각 컨테이너에서 WORKDIR / ENV / requirements를 별도로 관리
#
# Author: 조동휘
# Created: 2026-03-05
#
# Updated:
# - 2026-03-05: initial version (조동휘)
# - 2026-03-06: ipykernel 설치 제거 (조동휘)
# =========================================================================

# python:3.12-slim 이미지를 기반으로 컨테이너 환경 생성
FROM python:3.12-slim


# Python 캐시 파일(.pyc) 생성 방지 및 로그 버퍼링 비활성화
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONIOENCODING=UTF-8


# 공통 시스템 패키지 설치 (git: 일부 패키지 git 설치 대비)
# Python Package build를 위한 컴파일 도구 설치
# 일부 Package는 C/C++ 컴파일이 필요 (numpy, lightgbm)
RUN apt-get update \
    && apt-get install -y --no-install-recommends  \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*  # apt 캐시 제거로 이미지 용량 최소화


# 사전에 PIP 업데이트
RUN python -m pip install --upgrade pip