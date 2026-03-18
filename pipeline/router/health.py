"""
=========================================================================
Project:
- Credit Card Customers

Module:
- pipeline/router

File: health.py

Purpose:
- health check endpoint for pipeline 컨테이너의 상태를 확인하기 위한 라우터

Author: @조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@조동휘)
=========================================================================
"""
from fastapi import APIRouter

from pipeline.schemas.health import HealthResponse
from pipeline.services.health_service import get_health_status

router = APIRouter(
    prefix="/health",
    tags = ['Health'])

@router.get("/z",
            description="Pipeline 컨테이너가 정상적으로 실행 중이며 요청에 응답할 수 있는 상태인지 확인하기 위한 상태 확인 API입니다.",
            response_description="Pipeline 서비스의 정상 동작 여부를 나타내는 상태 정보입니다.",        
            response_model=HealthResponse)
def health_check() -> HealthResponse:
    """
    Pipeline 컨테이너의 상태를 확인하기 위한 API 엔드포인트입니다.
    
    Returns:
        HealthRespone: 컨테이너의 상태를 나타내는 응답 객체로, 'healthy' 상태 메시지와 서비스 이름, 상세 메시지를 포함합니다.
    """
    return get_health_status()