from ensurepip import bootstrap
from kafka import KafkaProducer, KafkaConsumer
import json
from market_price_spt.settings import KAFKA_HOST, KAFKA_PORT

def initProducer(host=KAFKA_HOST, port=KAFKA_PORT):
    return KafkaProducer(
        bootstrap_servers='%s:%s'%(host, port),
        api_version=(0, 10, 1),
        value_serializer=lambda v: v.encode('utf-8')
        )


def initConsumer(host=KAFKA_HOST, port=KAFKA_PORT):
    return KafkaConsumer(
        bootstrap_servers='%s:%s'%(host, port),
        api_version=(0, 10, 1)
        )
    