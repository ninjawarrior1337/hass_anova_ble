"""Sensor platform for integration_blueprint."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription, SensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTime
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import AnovaDataUpdateCoordinator
from .entity import AnovaBluetoothEntity

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key=f"{SensorDeviceClass.DURATION}_{UnitOfTime.MINUTES}",
        name="Timer Duration",
        icon="mdi:clock",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.MINUTES
    ),
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        AnovaBluetoothSensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class AnovaBluetoothSensor(AnovaBluetoothEntity, SensorEntity):
    """integration_blueprint Sensor class."""

    def __init__(
        self,
        coordinator: AnovaDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self.coordinator = coordinator

    @property
    def native_value(self) -> float | None:
        """Return the native value of the sensor."""
        if self.coordinator.circulator.state:
            return self.coordinator.circulator.state.timer[0]
        else:
            return None
