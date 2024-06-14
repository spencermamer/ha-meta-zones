import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import area_registry as ar
from .const import DOMAIN, CONF_METAZONES, CONF_LABELS

_LOGGER = logging.getLogger(__name__)

class ZoneSensorsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Zone Sensors."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        _LOGGER.debug(f"User input at initial step: {user_input}")
        if user_input is not None:
            _LOGGER.debug(f"Creating entry with user input: {user_input}")
            return self.async_create_entry(title=user_input["metazone_name"], data=user_input)

        area_reg = await ar.async_get_registry(self.hass)
        areas = area_reg.areas
        area_labels = {area.name: area.name for area in areas.values()}
        _LOGGER.debug(f"Available area labels: {area_labels}")

        schema = vol.Schema({
            vol.Required("metazone_name"): str,
            vol.Required("area_label"): vol.In(area_labels)
        })

        return self.async_show_form(step_id="user", data_schema=schema)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return ZoneSensorsOptionsFlow(config_entry)


class ZoneSensorsOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Zone Sensors."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options for the custom component."""
        _LOGGER.debug(f"Options init step with user input: {user_input}")
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle the user options step."""
        _LOGGER.debug(f"Options user step with user input: {user_input}")
        if user_input is not None:
            _LOGGER.debug(f"Updating entry with user input: {user_input}")
            return self.async_create_entry(title="", data=user_input)

        area_reg = await ar.async_get_registry(self.hass)
        areas = area_reg.areas
        area_labels = {area.name: area.name for area in areas.values()}
        _LOGGER.debug(f"Available area labels for options: {area_labels}")

        schema = vol.Schema({
            vol.Required("metazone_name", default=self.config_entry.data.get("metazone_name")): str,
            vol.Required("area_label", default=self.config_entry.data.get("area_label")): vol.In(area_labels)
        })

        return self.async_show_form(step_id="user", data_schema=schema)