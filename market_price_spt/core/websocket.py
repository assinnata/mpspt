from typing import Any
import websocket
import time
from market_price_spt.core.kafka import initProducer
import rel

class MarketPriceSPTWebsocket():
    def __init__(self, connection_string) -> None:
        self.callbacks = {}
        def on_open(ws):
            print("Opened connection")

        def on_message(ws, message):
            if self.callbacks:
                for event_method in self.callbacks:
                    self.callbacks[event_method](message)

        def on_error(ws, error):
            raise error

        def on_close(ws, close_status_code, close_msg):
            print("### closed ###")


        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(connection_string,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close)

    def on(self, event_name, callback):
        print("registering", event_name)
        if self.callbacks is None:
            self.callbacks = {}

        if event_name not in self.callbacks:
            self.callbacks[event_name] = callback
        else:
            self.callbacks[event_name] = callback
        print("registered", event_name)

    def run(self):
        self.ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()