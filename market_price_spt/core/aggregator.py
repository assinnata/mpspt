import json
import time
from market_price_spt.core.exceptions import AggregatorException
from market_price_spt.core.kafka import initConsumer
from market_price_spt.settings import KAFKA_HOST, KAFKA_PORT
running = True

def aggregatorConsumerLoop(topics: list):
    consumer = initConsumer(host=KAFKA_HOST, port=KAFKA_PORT)
    try:
        consumer.subscribe(topics)

        while running:
            consumer.poll()
            for message in consumer:
                try:
                    json_message = json.loads(message.value.decode())
                    print('Datapoint from kafka: %s', json_message)
                except json.JSONDecodeError:
                    print("Failed to decode message from Kafka, skipping..")
                except Exception as e:
                    print("Generic exception while pulling datapoints from Kafka")
            time.sleep(0.2)

        print('Kafka datapoints puller thread shutting down..') 
            
    except Exception as e:
        raise AggregatorException(e)
    finally:
        consumer.close()

def shutdownAggregatorConsumerLoop():
    running = False