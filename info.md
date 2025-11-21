# AquaBle Integration for Home Assistant

Control Chihiros aquarium devices (LED lights and dosing pumps) directly from Home Assistant via Bluetooth Low Energy.

## Features

- **Bluetooth Discovery**: Automatically discovers Chihiros devices on your network
- **Doser Control**: Monitor dosing volumes, set schedules, and trigger manual doses
- **Light Control**: Adjust brightness per color channel, switch between manual/auto modes
- **Native Integration**: Built as a Home Assistant custom component with full UI support

## Supported Devices

### Dosing Pumps

- Chihiros Doser series

### LED Lights

- WRGB series (WRGB, WRGB II, WRGB II Pro, WRGB II Slim)
- Commander series (Commander 1, Commander 4)
- Other models (A2, C2, C2 RGB, Z-Light Tiny, Universal WRGB, Tiny Terrarium Egg)

## Installation

### Via HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to **Integrations**
3. Click the **⋮** menu in the top-right corner
4. Select **Custom repositories**
5. Add this repository URL: `https://github.com/caleb-venner/AquaBle-dev`
6. Select category: **Integration**
7. Click **Add**
8. Find **AquaBle** in the integration list and click **Download**
9. Restart Home Assistant

### Manual Installation

1. Download the latest release
2. Copy the `custom_components/aquable` folder to your Home Assistant `config/custom_components/` directory
3. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for **AquaBle**
4. Select your device from the discovered Bluetooth devices (or enter manually)
5. Complete the setup wizard

## Entities

### Doser Entities (per pump head)

- **Sensor**: Today's volume, lifetime total
- **Button**: Manual dose trigger
- **Services**: Set schedule, configure dosing parameters

### Light Entities (per device)

- **Sensor**: Current mode and status
- **Services**: Set brightness, configure auto schedules, switch modes

## Services

The integration provides YAML services for advanced automation:

### `aquable.doser_set_head_schedule`

Configure dosing schedule for a pump head.

### `aquable.light_set_manual_mode`

Set light to manual mode with specific brightness values.

### `aquable.light_set_auto_schedule`

Configure automatic lighting schedule with keyframes.

### `aquable.light_set_mode`

Switch between manual, auto, and off modes.

## Support

For issues, questions, or feature requests, please visit:

- [GitHub Issues](https://github.com/caleb-venner/AquaBle-dev/issues)
- [Documentation](https://github.com/caleb-venner/AquaBle-dev)

## Legal Notice

This project is not affiliated with, endorsed by, or approved by Chihiros Aquatic Studio or Shanghai Ogino Biotechnology Co., Ltd. This is an independent, open-source software project developed through reverse engineering and community contributions.

## License

MIT License - see LICENSE file for details.

Based on [Chihiros LED Control](https://github.com/TheMicDiet/chihiros-led-control) by Michael Dietrich.
