"""Storage package for device status models.

This package provides status parsing models for BLE device notifications.
For the Home Assistant integration, device configuration is stored in config entries.
"""

# Status models - these are kept for parsing BLE notifications
from .models import DoserStatus, LightStatus

__all__ = [
    "DoserStatus",
    "LightStatus",
]
