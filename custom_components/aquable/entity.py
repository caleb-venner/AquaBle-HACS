"""Base entity for AquaBle devices."""
from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

if TYPE_CHECKING:
    from .coordinator import AquaBleCoordinator


class AquaBleEntity(CoordinatorEntity["AquaBleCoordinator"]):
    """Base entity for AquaBle devices."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: AquaBleCoordinator,
        entity_key: str,
    ) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        
        self._attr_unique_id = f"{coordinator.device.address}_{entity_key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.device.address)},
            name=coordinator.config_entry.title,
            manufacturer="Chihiros",
            model=coordinator.device_type.title(),
            sw_version=None,  # Could add firmware version if available
        )

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return super().available and self.coordinator.device.is_connected
