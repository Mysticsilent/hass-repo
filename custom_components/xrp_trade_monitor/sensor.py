"""XRPUSDT transaction history"""

import requests
from homeassistant.helpers.entity import Entity

# Definieer een naam voor de sensor
DOMAIN = 'xrp_trade_monitor'

def setup_platform(hass, config, add_entities, discovery_info=None):
    """ Setup de sensor """
    add_entities([XrpTradeSensor()])

class XrpTradeSensor(Entity):
    """ Een sensor voor het volgen van de laatste XRP-transacties """

    def __init__(self):
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        """ De naam van de sensor """
        return 'XRP Trade Volume'

    @property
    def state(self):
        """ De status van de sensor """
        return self._state

    @property
    def extra_state_attributes(self):
        """ Extra attributen van de sensor """
        return self._attributes

    def update(self):
        """ Haal de laatste XRP-transacties op en update de status """
        url = "https://api.binance.com/api/v3/trades"
        params = {
            'symbol': 'XRPUSDT',  # Het handelspaar voor XRP/USDT
            'limit': 1  # Haal de meest recente transactie op
        }

        try:
            response = requests.get(url, params=params)
            trades = response.json()

            if trades:
                last_trade = trades[0]
                self._state = float(last_trade['qty'])  # Alleen de hoeveelheid (qty) in XRP
                self._attributes = {
                    'price': float(last_trade['price']),  # Prijs van de transactie
                    'currency': 'USD'
                }
            else:
                self._state = None
                self._attributes = {'error': 'No trades found'}
        except Exception as e:
            self._state = None
            self._attributes = {'error': str(e)}
