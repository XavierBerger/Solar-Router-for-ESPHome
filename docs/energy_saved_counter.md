# Energy Saved Counter

Energy saved counters are designed to count the energy diverted to the load. **This component is mandatory.**

This counter can be provided by a power meter or not. If the power meter deosn't provide such information, it is then required to add one specifically.

!!! tip
    Read the documentation of power meter to see if it provide a power meter or not.

### Energy Saved Counter ***Theorical***

```yaml
packages:
  counter:
    url: https://github.com/XavierBerger/Solar-Router-for-ESPHome/
    file: solar_router/energy_saved_counter_theorical.yaml
```


### Energy Saved Counter ***None***

If you don't care about energy saved counter (because you already have this measure somewhere else), you can use `energy_saved_counter_none.yaml`. 

```yaml
packages:
  counter:
    url: https://github.com/XavierBerger/Solar-Router-for-ESPHome/
    file: solar_router/energy_saved_counter_none.yaml
```

This counter just do nothing.