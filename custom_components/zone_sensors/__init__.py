
import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the zone sensors component.""" 
    _LOGGER.debug("Setting up zone sensors component") 
    return True 

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry): 
    """Set up zone sensors from a config entry.""" 
    _LOGGER.debug(f"Setting up entry: {entry}") 
    hass.async_create_task( 
        hass.config_entries.async_forward_entry_setup(entry, "sensor") 
    ) 
    return True 

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry): 
    """Unload a config entry.""" 
    _LOGGER.debug(f"Unloading entry: {entry}") 
    await hass.config_entries.async_forward_entry_unload(entry, "sensor") 
    return True
