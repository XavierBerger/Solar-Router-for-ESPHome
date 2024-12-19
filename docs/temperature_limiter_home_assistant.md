# Temperature limiter Home Assistant

This package is designed to monitor a temperature coming from a sensor in Home Assistant and determines if a temperature threshold as been reached or not.

When safety limit is reached, it is possible to turn on a LED. LED configuration has to be added in `substitutions` section as explained bellow.

!!! danger "WARNING: Conduct some tests before letting the system regulate alone"
    This temperature limit monitoring and safety limit may have some bug. It is strongly advised to validate the behaviour of your system carefully before letting the system working by its own.

To use this package, add the following lines to your configuration file:

```yaml linenums="1"
packages:
  temperature_limiter:
    url: http://github.com/XavierBerger/ESPHome-Solar-Router/
    file: solar_router/temperature_limiter_home_assistant.yaml
```

This package needs to know the sensor to use to get the temperature to monitor. This sensor has to be defined by `temperature_sensor` into `subtsitutions` section of your configuration as in example ballow:

```yaml linenums="1"
substitutions:
  # Sensor in home assistant gathering the temperature
  temperature_sensor: sensor.hot_water_temperature
 # Safety limit LED configuration
  red_led_inverted: "False"
  red_led_pin: GPIO4
```
!!! warning "Data availability and refresh rate"
    This temperature limiter rely on Home Assistant to gather the temperature. It also depends on the rate of sensor update. If a sensor is updated too slowly, the regulation may not work as expected.
