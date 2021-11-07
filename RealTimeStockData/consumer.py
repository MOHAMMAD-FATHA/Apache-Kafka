from kafka import KafkaConsumer
import os
import sys
from dotenv import load_dotenv
load_dotenv('.env')

TOPIC_NAME = os.getenv('TOPIC_NAME')

consumer = KafkaConsumer(TOPIC_NAME,auto_offset_reset = 'earliest',group_id = None,
                    )


with open('stock.txt','w') as f:
    for message in consumer:
        values = message.value
        values = str(values)
        f.write(values)
        f.write('\n')
        print(values)
sys.stdout.close()

sys.stdout=open('StockData2.txt','w+')
for message in consumer:
    values = message.value
    print(values)
sys.stdout.close()