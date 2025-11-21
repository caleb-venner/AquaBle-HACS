# Local Home Assistant Development

Quick setup for testing the AquaBle integration locally.

## Quick Start

```bash
# Start Home Assistant
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

Access Home Assistant at: http://localhost:8123

## First Run

1. Start the container: `docker-compose up -d`
2. Wait ~30 seconds for HA to initialize
3. Open http://localhost:8123
4. Complete the onboarding wizard
5. Your AquaBle integration is automatically loaded at `/config/custom_components/aquable`

## Development Workflow

### After making changes to the integration:

```bash
# Restart Home Assistant to reload the integration
docker-compose restart

# Or if you need a full restart
docker-compose down && docker-compose up -d
```

### View logs:

```bash
# All logs
docker-compose logs -f

# Just Home Assistant
docker logs -f homeassistant-aquable
```

### Access the container:

```bash
docker exec -it homeassistant-aquable bash
```

## Bluetooth on macOS

⚠️ **Docker on macOS runs in a Linux VM and cannot directly access Bluetooth devices.**

### Solutions:

1. **ESPHome Bluetooth Proxy** (Recommended)
   - Use an ESP32 as a Bluetooth bridge
   - Guide: https://esphome.github.io/bluetooth-proxies/

2. **Test on Linux/Raspberry Pi**
   - Use this same docker-compose.yml on a Linux machine
   - Direct Bluetooth access works natively

3. **Remote HA Instance**
   - Point your development to a remote HA instance with Bluetooth

4. **Mock Testing**
   - Test integration logic without real Bluetooth devices
   - Use pytest with mocked BLE connections

## Directory Structure

```
├── docker-compose.yml              # This file
├── ha-config/                      # HA configuration (auto-generated)
│   ├── configuration.yaml
│   ├── .storage/
│   └── custom_components/
│       └── aquable/                # Your integration (symlink)
└── custom_components/aquable/      # Your actual integration code
```

## Useful Commands

```bash
# Check if HA is running
curl http://localhost:8123

# Follow logs in real-time
docker-compose logs -f homeassistant

# Restart just HA (faster than full restart)
docker-compose restart homeassistant

# Full cleanup (removes config - USE WITH CAUTION)
docker-compose down -v
rm -rf ha-config/

# Check container status
docker-compose ps
```

## Troubleshooting

### Integration not loading

1. Check the logs: `docker-compose logs -f`
2. Verify the mount: `docker exec homeassistant-aquable ls -la /config/custom_components/aquable`
3. Restart HA: `docker-compose restart`

### Port 8123 already in use

```bash
# Find what's using the port
lsof -i :8123

# Stop the conflicting service or change the port in docker-compose.yml
```

### Configuration errors

- Check `ha-config/home-assistant.log`
- Validate your integration's `manifest.json`
- Ensure all dependencies are listed in `manifest.json`

## Testing the Integration

```bash
# Run pytest from your host machine
pytest tests/

# Or install dependencies locally and test
pip install -r requirements-dev.txt
pytest
```

## Resources

- [HA Development Docs](https://developers.home-assistant.io/)
- [Integration Development](https://developers.home-assistant.io/docs/creating_integration_manifest)
- [Testing Integrations](https://developers.home-assistant.io/docs/development_testing)
