"""
=========================================================================
Project:
- Credit Card Customers

Module:
- pipeline/schemas

File: health.py

Purpose:
- health check endpoint for pipeline 컨테이너의 상태를 확인하기 위한 스키마

Author: @조동휘
Created: 2026-03-10

Updated:
- 2026-03-10: initial version (@조동휘)
=========================================================================
"""

from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    """
    Health check response schema.
    """
    
    status: str = Field(..., description="Health status message confirming the health of the pipeline container.")
    service: str = Field(..., description="Name of the service being checked for health.")
    message: str = Field(..., description="Detailed message about the health status of the pipeline container.")