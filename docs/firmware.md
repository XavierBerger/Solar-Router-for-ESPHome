# Firmware

Firmware has been split in several packages which can be assemble to the needs of user.

Packages are :

* **Power meters** : design to measure the energy exchanged with the grid.
* **Regulator** : design to channel the surplus of energy to a designated load.
* **Solar Router Engine** : design to determine how much of energy and when surplus of energy should be diverted to the load.
* **Energy saved counter** : design to report the amount of energy dicvrted to the load (on daily bases).

## Packages

Packages can be combined to create a variaty of solar router as in following examples.

### Standalone configuration

In this standalone configuration, only one ESP32 is doing the job and is running all the 3 packages.

![hardware connection](images/standalone.drawio.png){width=374}

### Power Meter Proxy configuration

In this proxy configuration, two ESP is doing the job. The first one (which coud be located into the electrical panel) gather the power meter information. The second one (which could be located close to the water heater) is getting the power meter information from the first ESP through the network and perfom the regulation.

![hardware connection](images/with_proxy.drawio.png){width=535}

!!! Note
    A Power Meter Proxy doesn't require a lot of CPU power and could then be executed on an ESP8285 or ESP8286.

### Multiple Solar Router configuration

In this multiple Solar Router configuration, two solar router are installed. The first one is reading the power exchanged with the grid and is diverting surplus to a wather heater. The second one is reading power exchange information from the first one using a proxy power meter. Base on the information collected, it will divert the surplus of energy to an anti frost system.

![hardware connection](images/multiple_routers.drawio.png){width=756}

!!! Note
    `reactivity` and `target grid exchange` will have to be adjusted carefully on both solar routers to avoid regulation conflicts.
