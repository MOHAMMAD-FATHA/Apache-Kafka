from kafka import KafkaConsumer

consumer = KafkaConsumer('python-kafka-test')
for message in consumer:
    print (message)