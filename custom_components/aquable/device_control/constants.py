"""Application constants including BLE protocol and timing definitions.

Centralized constants to ensure consistency across frontend, backend, and device layers.
"""

from __future__ import annotations

from enum import Enum

# ============================================================================
# BLE UART Protocol Constants
# ============================================================================

UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"


class DeviceType(Enum):
    """Device type enumeration for unified storage."""

    DOSER = "doser"
    LIGHT = "light"


# ============================================================================
# Timeout Constants
# ============================================================================

# Command execution timeouts (seconds)
COMMAND_TIMEOUT_DEFAULT = 10.0  # Default timeout for most commands
COMMAND_TIMEOUT_AUTO_SETTINGS = 15.0  # Timeout for auto setting operations (add/delete/reset)

# BLE operation timeouts (seconds)
BLE_STATUS_CAPTURE_WAIT = 1.5  # Wait time after sending commands before reading status
BLE_DOSER_SCHEDULE_WAIT = 2.0  # Wait time for doser schedule confirmation

# Frontend API timeouts (seconds) - should match backend defaults
FRONTEND_COMMAND_TIMEOUT_DEFAULT = 10
FRONTEND_COMMAND_TIMEOUT_AUTO_SETTINGS = 15

# ============================================================================
# BLE Connection and Retry Constants
# ============================================================================

# Connection retry behavior
DEFAULT_ATTEMPTS = 3  # Number of retry attempts for BLE operations

# Connection timing
DISCONNECT_DELAY = 120  # Seconds to wait before auto-disconnecting idle device
BLEAK_BACKOFF_TIME = 0.25  # Seconds to wait before retrying after BLE error

# ============================================================================
# Message ID Session Management
# ============================================================================

# Message ID session management constants
MESSAGE_ID_RESET_INTERVAL_HOURS = 24.0  # Hours before resetting message ID session
MESSAGE_ID_MAX_SESSION_COMMANDS = 1000  # Max commands before resetting message ID session
