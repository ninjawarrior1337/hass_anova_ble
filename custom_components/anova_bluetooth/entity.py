"""AnovaBluetoothEntity class."""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, VERSION, NAME
from .coordinator import AnovaDataUpdateCoordinator


class AnovaBluetoothEntity(CoordinatorEntity):
    """AnovaBluetoothEntity class."""

    def __init__(self, coordinator: AnovaDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.unique_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self.unique_id)},
            name=NAME,
            model=VERSION,
            manufacturer="Anova Applied Electronics, Inc",
        )
