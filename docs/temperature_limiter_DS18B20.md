# Temperature limiter DS 18B20

This package is designed to monitor a temperature coming from a DS18B20 sensor connected on ESP32 and determines if a temperature threshold as been reached or not.

When safety limit is reached, it is possible to turn on a LED. LED configuration has to be added in `substitutions` section as explained bellow.

!!! danger "WARNING: Conduct some tests before letting the system regulate alone"
    This temperature limit monitoring and safety limit may have some bug. It is strongly advised to validate the behaviour of your system carefully before letting the system working by its own.

The following schematic is representing the wiring of the temperature sensor:

![DS18B20](images/DS18B20_wiring.png){width=400}

To use this package, add the following lines to your configuration file:

```yaml linenums="1"
packages:
  temperature_limiter:
    url: http://github.com/XavierBerger/ESPHome-Solar-Router/
    file: solar_router/temperature_limiter_DS18B20.yaml
```

This package needs to know the GPIO used by the temperature to get the temperature. This GPIO has to be defined by `DS18B20_pin` into `subtsitutions` section of your configuration as in example ballow:

```yaml linenums="1"
substitutions:
  # Sensor in home assistant gathering the temperature
  DS18B20_pin: GPIO13
  # Safety limit LED configuration
  red_led_inverted: "False"
  red_led_pin: GPIO4

```

Additionnal optional parameters can be set into `substitutions` section such as `DS18B20_address` (which is optional) and `temperature_update_interval` (which is set by default to `5s`).