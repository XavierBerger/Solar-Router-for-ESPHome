# Installation and Configuration

To install your solar router, you need to define the archtecture of your solution between [standalone](firmware.md#standalone-configuration) installation; installation working with [proxy](firmware.md#power-meter-proxy-configuration) or [multiple solar router](firmware.md#multiple-solar-router-configuration) installation.

### Step 1: Install and configure ESPHome firmware

Install [ESPHome](https://esphome.io) on your ESP as described into [Ready-Made Project](https://esphome.io/projects/) documentation.  
Select **"Empty ESPHome device"**.

Adopt it into [Home Assistant](https://home-assistant.io).

!!! important "Wifi reconnection"
    Remove `ap:` and `captive_portal:`.  
    *This could prevent the solar router from connecting to WiFi in case of loss of connection* 

### Step 2: Select packages

A **solar router** needs 3 packages: a **power meter**, a **regulator** and the **engine**.

A **proxy** just need 1 **power meter** package

#### Step 2.1: Select a Power Meter 

* [Fronius](power_meter_fronius.md)  
    Get power data from Fronius inverter (Tested on Gen24 Primo)
* [Home Assistant](power_meter_home_assistant.md)  
    Get power data from Home Assistant sensor
* [Proxy client](power_meter_proxy_client.md)  
    Get power data from outside from solar router

!!! abstract "Contribute"
    You are developer and your power meter is missing fron this list, refer to [contributing](contributing.md) section to see how to contribute to this project.

#### Step 2.2: Select a Regulator

* For regulator which can be controlled from 0% to 100%
    * [Triac](regulator_triac.md)  
    Regulate energy with a Triac
    * [Solid State Relay](regulator_solid_state_relay.md)  
    Regulate energy with a Solid State Relais
* For regulator wich can only be switched ON/OFF
    * [Mecanical relay](regulator_mecanical_relay.md)  
    Regulate energy with mecanical relay


!!! abstract "Contribute"
    You are developer and your regulator is missing from this list, refer to [contributing](contributing.md) section to see how to contribute to this project.


#### Step 2.3: Add an Engine

* [Variable Engine](engine.md)  
  Read power exchange with the grid, determine and apply the percentage of regulator opening.

* [ON/OFF Engine](engine_on_off.md)  
  Read power exchange with the grid, and start to divert energy if a threshold is reached and stop if another threshold is reached.

#### Step 2.4: Add an Energy Counter (*Optional*)

* [Energy Saved Counter Theorical](energy_saved_counter_theorical.md)  
  Calculate energy savec base on energy diverted and load power.

### Step 3: Configure your solar router

Each package requires a configuration which is done in `substitution` section.  
*Refer to documentation of packages selected and add configuration to the end of your yaml file.*

You can refer to examples to see how to configure your yaml for a [standalone](standalone_example.md) installation a [proxy based](proxy_example.md) installation.

!!! example "More examples are available in [github](https://github.com/XavierBerger/Solar-Router-for-ESPHome)"


### Step 4: Upload firmware

Install Solar Router on your ESP using OTA from Home Assistant.
