from market_price_spt.core.kafka import initProducer
from market_price_spt.core.websocket import MarketPriceSPTWebsocket
from market_price_spt.settings import KAFKA_HOST, KAFKA_PORT

def startWebsocket():
    kafka_producer = initProducer(host=KAFKA_HOST, port=KAFKA_PORT)
    mpws = MarketPriceSPTWebsocket(connection_string="wss://api.gemini.com/v1/marketdata/BTCUSD")
    def kafka_send(message):
        kafka_producer.send("gemini", message)

    # mpws.on("message", print_message)
    mpws.on("kafka_event", kafka_send)
    mpws.run()

# kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic gemini --replication-factor 1 --partitions 1
# kafka-run-class kafka.tools.GetOffsetShell --broker-list kafka:9092 --topic gemini | awk -F  ":" '{sum += $3} END {print sum}'