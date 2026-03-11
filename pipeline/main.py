"""
=========================================================================
Project:
- Credit Card Customers

Module:
- pipeline

File: main.py

Purpose:
- fastapi 애플리케이션의 진입점으로, API 라우터를 등록하고 애플리케이션을 실행하는 역할을 합니다.

Author: @조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@조동휘)
=========================================================================
"""

from fastapi import FastAPI

from pipeline.router.health import router as health_router

app = FastAPI(
    title="Credit Card Customers 파이프라인 API",
    description="Credit Card Customers 프로젝트의 데이터 파이프라인을 관리하고 상태를 모니터링하기 위한 API입니다.",
    version="0.1.0"
)

app.include_router(health_router)