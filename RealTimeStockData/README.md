Sending messages from producer to consumer using python code for consumer as well as producer
Kafka makes use of a tool called ZooKeeper which is a centralized service for a distributed environment like Kafka. It offers configuration service, synchronization service, and a naming registry for large distributed systems.

Thus, we need to first start the ZooKeeper server followed by the Kafka server. This can be achieved using the following commands:

# Start ZooKeeper Server
$bin/zookeeper-server-start.sh config/zookeeper.properties
# Start Kafka Server
$bin/kafka-server-start.sh config/server.properties

Starting kafka topics : Let us start by creating a python-kafka-test Kafka topic with a single partition and replica. This can be done using the following command:
$bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic StockData

Now, let us list down all of our Kafka topics to check if we have successfully created our StockData topic. We can make use of the list command here:
$bin/kafka-topics.sh --list --zookeeper localhost:2181

You can also make use of the describe topics command for more details on a particular Kafka topic:
$bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic StockData

Consumer code in python for kafka: consumer.py

Now that we have a consumer listening to us, we should create a producer which generates messages that are published to Kafka and thereby consumed by our consumer created earlier: producer.py

Sending the real time stock data from text file to the hadoop cluster using subprocess kafka-hdfs.py

After that we can check hadoop cluster that data got uploaded
