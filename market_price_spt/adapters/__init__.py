
from market_price_spt.adapters import gemini


def startAdapterWebsocket( exchange: str ):
    if exchange == "gemini":
        return gemini.startWebsocket()

    raise Exception("Unknown Exchange Adapter")