# AquaBle - AI Coding Guidelines

IMPORTANT: This file contains instructions for automated coding assistants and contributors. Please read before making edits.

- Do NOT generate or add user-facing documentation files (guides, HOWTOs, tutorials) unless explicitly requested by the project owner. The project maintainers prefer documentation to be created intentionally and reviewed before inclusion.

## Architecture Overview

**Native Home Assistant Integration**: This project is a custom Home Assistant integration that manages Chihiros aquarium devices (lights/dosers) over BLE. Built using Home Assistant's integration patterns with `bleak` for Bluetooth communication.

**Key Components**:
- Device Classes (`device/`): `BaseDevice` with specific implementations (Doser, LightDevice, etc.) handling BLE connection lifecycle
- Command System (`commands/encoder.py`): Encodes BLE commands with message ID management (skipping 0x5A/90), checksums, and structured byte arrays
- Status Models (`storage/models.py`): Parse BLE notifications into `DoserStatus` and `LightStatus` dataclasses
- HA Entity Platforms (planned): Sensor, number, light, time, select, button platforms for device control
- HA Coordinator (planned): `DataUpdateCoordinator` for managing device state updates
- Config Flow (planned): Bluetooth device discovery and setup UI

**Data Flow**: BLE Device → `bleak` → `BaseDevice` → UpdateCoordinator → HA Entity State → HA Frontend

**BLE Protocol**: Reverse-engineered Chihiros UART service (`6E400001-B5A3-F393-E0A9-E50E24DCCA9E`) with RX/TX characteristics. Commands sent as notifications, responses received via notifications. Command structure: `[Command ID, Length, Message ID High/Low, Mode, Parameters..., Checksum]` with XOR checksum.

## Developer Workflows

**Local Development**:
- Install integration in HA development container or test instance
- Copy `custom_components/aquable/` to HA's `config/custom_components/`
- Restart Home Assistant to load integration
- Add devices via Integrations UI (auto-discovery or manual)
- Test with real BLE hardware nearby

**Quality Assurance**:
- `pytest tests/` - Run test suite
- `black custom_components/` - Format code
- `isort custom_components/` - Sort imports
- `flake8 custom_components/` - Lint code

**Installation for Users**:
- **HACS Custom Repository**: Users add repository URL to HACS manually
- No backward compatibility with old add-on (fresh start)

## Project Conventions

**Device Command Encoding**:
- Commands use structured byte arrays: `[Command ID, Length, Message ID High/Low, Mode, Parameters..., Checksum]`
- Message IDs increment per session, skipping 0x5A (90) in both bytes via `commands.next_message_id()`
- Checksum is XOR of all command bytes starting from second byte
- Example manual brightness: `commands.encode_manual_brightness(msg_id, channel, brightness)` → `[0x5A, length, msg_id_high, msg_id_low, 0x07, channel, brightness, checksum]`

**Device Class Hierarchy**:
```python
class BaseDevice(ABC):
    device_kind: ClassVar[str] = "device"
    # BLE connection management, message ID tracking, operation locking
    # Subclasses implement device-specific commands

class Doser(BaseDevice):
    device_kind = "doser"
    # Dosing pump control with lifetime tracking

class LightDevice(BaseDevice):
    device_kind = "light"
    # LED lighting control with color channel management
```

## Integration Points

**BLE Protocol Details**:
- UART service: `6E400001-B5A3-F393-E0A9-E50E24DCCA9E`
- RX characteristic: `6E400002-B5A3-F393-E0A9-E50E24DCCA9E` (send commands)
- TX characteristic: `6E400003-B5A3-F393-E0A9-E50E24DCCA9E` (receive notifications)
- Commands sent as BLE notifications, responses received via notifications

**Home Assistant Integration**:
- Uses HA's `bluetooth` integration for device discovery
- Config entries store device configuration (address, name, schedules)
- Entity platforms expose devices as standard HA entities
- Services provide bulk operations (full schedule updates)
- No custom frontend - uses standard HA Lovelace UI

## Common Patterns

**Device Connection**:
```python
async with device_session(address) as device:
    # Device automatically disconnected on context exit
    await device.send_command(command_bytes)
```

**Command Encoding**:
```python
from .commands import encoder as commands
msg_id = commands.next_message_id(current_id)
payload = commands.encode_manual_brightness(msg_id, channel, brightness)
```

**Status Updates**:
```python
# Request status, wait for notification, return parsed result
await device.request_status()
await asyncio.sleep(STATUS_CAPTURE_WAIT_SECONDS)
status = device.last_status  # DoserStatus or LightStatus dataclass
```

**HA Entity Update Pattern** (planned):
```python
# Coordinator fetches data on interval
async def _async_update_data(self):
    await self.device.request_status()
    await asyncio.sleep(1.5)
    return self.device.last_status

# Entities subscribe to coordinator
@property
def native_value(self):
    return self.coordinator.data.some_field
```

**HA Service Pattern** (planned):
```python
# Bulk operations via HA services
async def handle_set_schedule(call):
    device_id = call.data["device_id"]
    coordinator = get_coordinator(device_id)
    await coordinator.device.set_daily_dose(...)
    await coordinator.async_request_refresh()
```

## Guidelines for AI Assistant

**Do NOT create summary documentation or improvement reports** unless explicitly requested by the user. Focus only on:
- Fixing bugs or issues raised
- Implementing features requested
- Code quality improvements when asked
- Explanations of what was changed (inline, not as documents)

If changes are significant and deserve documentation, ask the user first before creating any files.
