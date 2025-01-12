# XRP Trade Monitor - Homeassistant Integration
Home assistant custom integration for getting the latest XRP-USD transaction from the Binance API.

### Install using HACS (recommended)
If you do not have HACS installed yet visit https://hacs.xyz for installation instructions.
1. In HACS click the three dots in the top right corner and click "Custom repositories".
2. Add the repository address "https://github.com/Mysticsilent/xrp_trade_monitor" and choose type to "Integration".
3. Close the repository screen.
4. Search for "xrp_trade_monitor" and choose Download.

### Install manually
Clone or copy this repository and copy the folder 'custom_components/xrp_trade_monitor' into '<homeassistant config>/custom_components/xrp_trade_monitor'

### Configuration
Add a sensor to configuration.yaml

``` yaml
sensor:
  - platform: xrp_trade_monitor
```

### Example automation
The automation below sends a notification to my iPhone when a trade bigger than 100M XRP has been detected.
To test the automation, go to developer tools. Set manually set a value bigger than 100M XRP.

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

![WhatsApp Image 2025-01-12 at 02 04 06_c3acf583](https://github.com/user-attachments/assets/9555ba7c-2974-42cd-83f7-d47b07feadca)
