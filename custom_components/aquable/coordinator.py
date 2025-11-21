"""DataUpdateCoordinator for AquaBle devices."""
from __future__ import annotations

import asyncio
import logging
from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DEVICE_TYPE_DOSER, DEVICE_TYPE_LIGHT, DOMAIN
from .device_control.status_parser import DoserStatus, LightStatus

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry

    from .device_control.device.base_device import BaseDevice

_LOGGER = logging.getLogger(__name__)


class AquaBleCoordinator(DataUpdateCoordinator[DoserStatus | LightStatus]):
    """Coordinator to manage data updates from AquaBle devices."""

    def __init__(
        self,
        hass: HomeAssistant,
        device: BaseDevice,
        device_type: str,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{device.address}",
            update_interval=None,  # No automatic polling - update on-demand only
        )
        self.device = device
        self.device_type = device_type
        self.config_entry = entry
        # Track active light auto schedules (max 24 per device)
        self.active_schedules: list[dict] = entry.options.get("active_schedules", [])

    async def _async_update_data(self) -> DoserStatus | LightStatus:
        """Fetch data from device."""
        try:
            # Request status update (handles connection internally via _ensure_connected)
            _LOGGER.debug("Requesting status from device %s", self.device.address)
            await self.device.request_status()

            # Wait for notification to arrive and be processed
            await asyncio.sleep(1.5)

            # Return parsed status
            if self.device.last_status is None:
                raise UpdateFailed(f"No status received from {self.device.address}")

            _LOGGER.debug("Status update successful for %s", self.device.address)
            return self.device.last_status

        except Exception as err:
            _LOGGER.error("Error updating device %s: %s", self.device.address, err)
            raise UpdateFailed(f"Error communicating with {self.device.address}: {err}") from err
