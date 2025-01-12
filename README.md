# XRP Trade Monitor - Homeassistant Integration
Home assistant custom integration for getting the latest XRP-USD transaction from the Binance API.

### Install using HACS (recommended)
If you do not have HACS installed yet visit https://hacs.xyz for installation instructions.
In HACS go to the Integrations section hit the big + at the bottom right and search for **xrp_trade_monitor**.

### Install manually
Clone or copy this repository and copy the folder 'custom_components/xrp_trade_monitor' into '<homeassistant config>/custom_components/xrp_trade_monitor'

### Configuration
Add a sensor to configuration.yaml

``` yaml
sensor:
  - platform: xrp_trade_monitor
```

### Configure a automation 

``` yaml
- alias: Notify bij grote XRP trade
  id: 'notify_bij_grote_xrp_trade'
  trigger:
    - platform: numeric_state
      entity_id: sensor.xrp_trade_volume
      above: 100000000
  condition: []
  action:
    - service: notify.mobile_app_iphone
      data:
        title: "🚨 Grote XRP Trade Gedetecteerd"
        message: >
          Er is een XRP-transactie uitgevoerd met een handelsvolume van meer dan 100M XRP!
        data:
          push:
          badge: 0
          sound: "default"
  mode: single
```