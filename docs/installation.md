# Installation and Configuration

To install your solar router, you need to define the archtecture of your solution between [standalone](firmware.md#standalone-configuration) installation, installation working with [proxy](firmware.md#power-meter-proxy-configuration) or [multiple solar router](firmware.md#multiple-solar-router-configuration) installation.

### Step 1: Install and configure ESPHome firmware

Install [ESPHome](https://esphome.io) on your ESP as described into [Ready-Made Project](https://esphome.io/projects/) documentation.  
Select **"Empty ESPHome device"**.

Adopt it into [Home Assistant](https://home-assistant.io).

!!! important "Wifi reconnection"
    Remove `ap:` and `captive_portal:`.  
    *This will prevent the solar router from connecting to WiFi in case of loss of connection* 

### Step 2: Select packages

A **solar router** needs 3 packages: a **power meter**, a **regulator** and the **solar router engine**.

A **proxy** just need 1 **power meter** package

#### Step 2.1: Select a Power Meter 

* [Fronius](fronius.md)  
    Get power data from Fronius inverter (Tested on Gen24 Primo)
* [Proxy client](proxy_client.md)  
    Get power data from outside from solar router
!!! abstract "Contribute"
    You are developer and your power meter is missing fron this list, refer to [contributing](contributing.md) section to see how to contribute to this project.

#### Step 2.2: Select a Regulator

* [Triac](triac.md)  
  Regulate energy with a Triac
* [Relay](relay.md)  
  Regulate energy with a Solid State Relais or a Triac 
!!! abstract "Contribute"
    You are developer and your regulator is missing fron this list, refer to [contributing](contributing.md) section to see how to contribute to this project.


#### Step 2.3: Add the Solar Router Engine

* [Solar Router Engine](engine.md)  
  Read power exchange with the grid, determine and apply the percentage of regulator opening.

### Ster 3: Configure your solar router

Each package requires a configuration which is done in `substitution` section.  
*Refer to documentation of packages selected and add configuration to the end of your yaml file.*

You can refer to examples to see how to configure your yaml for a [standalone](standalone_example.md) installation a [proxy based](proxy_example.md) installation


### Step 4: Upload firmware

Install Solar Router on your ESP using OTA from Home Assistant.

