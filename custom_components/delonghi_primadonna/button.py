from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .device import DelonghiDeviceEntity, DelongiPrimadonna


async def async_setup_entry(
        hass: HomeAssistant, entry: ConfigEntry,
        async_add_entities: AddEntitiesCallback):
    delongh_device: DelongiPrimadonna = hass.data[DOMAIN][entry.unique_id]
    async_add_entities([
        DelongiPrimadonnaPowerButton(delongh_device, hass)
    ])
    return True


class DelongiPrimadonnaPowerButton(DelonghiDeviceEntity, ButtonEntity):
    """This button turns on the device"""
    _attr_name = 'Turn on ECAM'

    async def async_press(self):
        self.hass.async_create_task(self.device.power_on())

