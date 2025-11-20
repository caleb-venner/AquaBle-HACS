# AquaBle Native Integration - Implementation Plan

**Timeline:** 91 hours (6 phases)  
**Current Status:** Core BLE code ported to `custom_components/aquable/`, ready for Phase 1

---

## Phase 1: Foundation

- ✅ Create `manifest.json` with domain, version, bluetooth service UUID
- ✅ Create `const.py` with DOMAIN and device type constants  
- ✅ Port device classes (`device/`, `commands/`, `storage/models.py`, `constants.py`, `errors.py`)
- ⬜ Create `coordinator.py` - DataUpdateCoordinator wrapping device status updates
- ⬜ Create `__init__.py` - Integration setup/teardown, coordinator initialization
- ⬜ Create `config_flow.py` - Bluetooth discovery + manual device entry
- ⬜ Create `strings.json` - UI translations for config flow

---

## Phase 2: Sensor Platform

- ⬜ Create `entity.py` - Base entity class with device_info and unique_id
- ⬜ Create `sensor.py` - Sensor platform setup
- ⬜ Doser sensors: dosed_today, lifetime_total (per head)
- ⬜ Light sensors: status, per-channel brightness
- ⬜ Test sensor state updates via coordinator refresh

---

## Phase 3: Number Platform

- ⬜ Create `number.py` - Number entity platform
- ⬜ Doser volume control (0-100 mL per head)
- ⬜ Light brightness control (0-100% per channel)
- ⬜ Implement config entry storage for settings
- ⬜ Wire up `async_set_native_value()` to device commands
- ⬜ Test value persistence across restarts

---

## Phase 4: Advanced Controls

- ⬜ Create `time.py` - Schedule time entities (doser heads, light start/end)
- ⬜ Create `select.py` - Mode selection (doser modes, light modes)
- ⬜ Create `button.py` - Manual dose trigger buttons
- ⬜ Create `light.py` - Native HA light entity (on/off/brightness/RGB)
- ⬜ Test all control entities with real hardware

---

## Phase 5: Services & Discovery

- ⬜ Create `services.yaml` - Define doser_set_schedule and light_set_schedule services
- ⬜ Implement service handlers in `__init__.py`
- ⬜ Add device type detection in config flow (from name/service data)
- ⬜ Enhance bluetooth discovery with filtering
- ⬜ Test services in automations

---

## Phase 6: Testing & HACS

- ⬜ Comprehensive testing with real doser + light devices
- ⬜ Test error handling (offline devices, connection failures)
- ⬜ Test multiple devices simultaneously
- ⬜ Create `hacs.json` for HACS metadata
- ⬜ Create `info.md` for HACS info panel
- ⬜ Write installation and setup documentation
- ⬜ Tag v3.0.0 release

---

## Entity Structure

**Doser (per device):**

- `sensor.doser_{name}_head_{n}_dosed_today` - mL dosed today
- `sensor.doser_{name}_head_{n}_lifetime_total` - Lifetime mL
- `number.doser_{name}_head_{n}_volume` - Daily volume (0-100 mL)
- `time.doser_{name}_head_{n}_schedule` - Daily dose time
- `select.doser_{name}_head_{n}_mode` - Mode (daily/24h/custom/timer/disabled)
- `button.doser_{name}_head_{n}_dose_now` - Manual dose trigger

**Light (per device):**

- `light.light_{name}` - Main light entity (on/off/brightness)
- `sensor.light_{name}_status` - Current status
- `number.light_{name}_channel_{color}_brightness` - Per-channel control
- `select.light_{name}_mode` - Mode (manual/auto/off)
- *Also need some kind of data structure for auto mode schedules*

---

## Success Criteria

- ✅ All 6 entity platforms functional
- ✅ Bluetooth auto-discovery working
- ✅ YAML services for bulk schedule updates
- ✅ Config persists across restarts
- ✅ Real hardware tested (both device types)
- ✅ HACS installable from custom repository
