"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- common

File: config.py

Purpose:
- common 모듈에서 사용하는 환경변수 및 API 관련 설정을 관리하는 파일

Author: @Nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@Nobrain711)
- 2026-03-13: 파일 헤더 누락 된 사항 추가 (@Nobrain711)
=========================================================================
"""

from os import getenv

from dotenv import load_dotenv


load_dotenv()

PIPELINE_BASE_URL = getenv("PIPELINE_API_BASE_URL")

if not PIPELINE_BASE_URL:
    raise RuntimeError("환경변수 'PIPELINE_API_BASE_URL'가 설정되지 않았습니다.")

PIPELINE_DATASET_URL = f"{PIPELINE_BASE_URL}"
