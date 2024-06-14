
# Zone Sensors

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Zone Sensors is a custom integration for [Home Assistant](https://home-assistant.io/) that creates aggregate sensors for defined zones and metazones based on Home Assistant labels.

## Features

- Automatically creates aggregate sensors for each defined area.
- Supports metazones, which are custom zones defined by user-selected labels.
- Easy configuration through the Home Assistant UI.

## Installation

### Manual Installation

1. Download the `zone_sensors` zip file and extract it.
2. Copy the `custom_components/zone_sensors` directory to your Home Assistant configuration directory.
3. Ensure the directory structure is as follows:
    ```text
    config/
    ├── custom_components/
    │   └── zone_sensors/
    │       ├── __init__.py
    │       ├── config_flow.py
    │       ├── const.py
    │       ├── manifest.json
    │       └── sensor.py
    ```

### HACS Installation

1. Ensure you have [HACS](https://hacs.xyz/) installed.
2. Add this repository as a custom repository in HACS settings.
3. Search for "Zone Sensors" in HACS and install it.

## Configuration

### Configuration via UI

1. Go to `Configuration` > `Integrations`.
2. Click on the `+` button and search for `Zone Sensors`.
3. Follow the setup wizard to define your metazones by selecting available labels.

### Example Configuration in `configuration.yaml`

To enable debug logging for this component, add the following to your `configuration.yaml`:

```yaml
logger:
  default: warning
  logs:
    custom_components.zone_sensors: debug
```

## Usage

Once configured, the component will automatically create sensors for each area and metazone. These sensors will aggregate data from all entities within the respective areas and metazones.

## Support

For issues, feature requests, and other support, please use the [GitHub issues](https://github.com/your-repo/zone_sensors/issues) page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request.

---

Developed with ❤️ by [Your Name](https://github.com/your-github-username).
