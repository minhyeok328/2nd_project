"""
=========================================================================
Project:
- Credit Card Customers

Module:
- pipeline

File: main.py

Purpose:
- fastapi 애플리케이션의 진입점으로, API 라우터를 등록하고 애플리케이션을 실행하는 역할을 합니다.

Author: @nobrain711
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@nobrain711)
- 2026-03-10: read_creditcard_dataset_router 추가 및 작업자 github 이름으로 변경 (@nobrain711)
=========================================================================
"""

from fastapi import FastAPI

from pipeline.router.health import router as health_router
from pipeline.router.read_creditcard_datset import router as read_creditcard_dataset_router

app = FastAPI(
    title="Credit Card Customers 파이프라인 API",
    description=("Credit Card Customers 프로젝트의 데이터 파이프라인을 관리하고"
                 "상태를 모니터링하기 위한 API입니다."),
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(read_creditcard_dataset_router)