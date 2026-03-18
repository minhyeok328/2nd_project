"""
=========================================================================
Project:
- Credit Card Customerss

Module:
- pipeline/services

File: health_service.py

Purpose:
- health check service for pipeline 컨테이너의 상태를 확인하기 위한 서비스

Author: @조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@조동휘)
=========================================================================
"""

from pipeline.schemas.health import HealthResponse

def get_health_status() -> HealthResponse:
    """
    pipeline 컨테이너의 상태를 확인하기 위한 서비스 함수
    이 함수를 호출하면 컨테이너가 정상적으로 작동 중인지 확인할 수 있는 메시지를 반환

    :return HealthResponse: health status response containing status, service name, and detailed message
    """
    return HealthResponse(
        status="healthy",
        service="pipeline",
        message="Pipeline container is healthy and responsive."
    )
