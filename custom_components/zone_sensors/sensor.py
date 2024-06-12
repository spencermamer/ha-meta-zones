
import logging
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType = None):
    """Set up the zone sensors."""
    _LOGGER.debug("Setting up platform with config: %s", config)
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up sensors from a config entry."""
    _LOGGER.debug(f"Setting up entry sensors with config entry: {config_entry}")
    entities = []
    areas = hass.helpers.area_registry.async_get_areas()
    area_entities = {area.id: hass.helpers.entity_registry.async_get_area_entities(area.id) for area in areas}

    # Create sensors for each area
    for area in areas:
        sensors = area_entities[area.id]
        _LOGGER.debug(f"Creating sensor for area {area.name} with entities: {sensors}")
        entities.append(ZoneSensor(hass, area.name, sensors))

    # Create sensors for each metazone
    metazone_name = config_entry.data["metazone_name"]
    area_label = config_entry.data["area_label"]
    metazone_entities = []
    for area in areas:
        if area.name == area_label:
            metazone_entities.extend(area_entities[area.id])
    _LOGGER.debug(f"Creating metazone sensor {metazone_name} with entities: {metazone_entities}")
    entities.append(ZoneSensor(hass, metazone_name, metazone_entities))

    async_add_entities(entities)

class ZoneSensor(Entity):
    def __init__(self, hass: HomeAssistant, area: str, entities: list):
        """Initialize the zone sensor."""
        self._hass = hass
        self._area = area
        self._entities = entities
        self._state = None
        self._name = f"Zone {area}"
        _LOGGER.debug(f"Initialized ZoneSensor for {area} with entities: {entities}")

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        values = [self._hass.states.get(entity).state for entity in self._entities if self._hass.states.get(entity)]
        _LOGGER.debug(f"Updating sensor {self._name} with values: {values}")
        self._state = sum(map(float, values)) / len(values) if values else None
        _LOGGER.debug(f"New state for {self._name}: {self._state}")
