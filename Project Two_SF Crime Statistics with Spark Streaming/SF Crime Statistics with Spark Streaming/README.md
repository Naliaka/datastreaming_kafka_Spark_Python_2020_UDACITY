# SF Crime Statistics with Spark Streaming

In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you've learned in this course to create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

You can try to answer the following questions with the dataset

*  What are the top types of crimes in San Fransisco?
*  What is the crime density by location?


## Development Environment

The following are required to complete this project:

* Spark 2.4.3
* Scala 2.11.x
* Java 1.8.x
* Kafka build with Scala 2.11.x
* Python 3.6.x or 3.7.x

## Description
Files You Need to Edit in Your Project Work
These starter code files should be edited:

*  producer_server.py
*  data_stream.py
*  kafka_server.py

The following file should be created separately for you to check if your kafka_server.py is working properly:

*  consumer_server.py

## The Project
This project requires creating topics, starting Zookeeper and Kafka servers, and your Kafka bootstrap server. You’ll need to choose a port number (e.g., 9092, 9093..) for your Kafka topic, and come up with a Kafka topic name and modify the zookeeper.properties and server.properties appropriately.

## Setup Environment

Install requirements using `./start.sh`  if you use conda for Python. If you use pip rather than conda, then use `pip install -r requirements.txt.`

Use the commands below to start the Zookeeper and Kafka servers. You can find the bin and config folder in the Kafka binary that you have downloaded and unzipped.

`bin/zookeeper-server-start.sh config/zookeeper.properties`
`bin/kafka-server-start.sh config/server.properties`

You can start the bootstrap server using this Python command: `python producer_server.py.`

## Workspace Environment

Modify the zookeeper.properties and producer.properties given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands:

`/usr/bin/zookeeper-server-start zookeeper.properties`
`usr/bin/kafka-server-start producer.properties`

### Step 1: Start the Zookeeper and Kafka Server

`/usr/bin/zookeeper-server-start config/zookeeper.properties`
`/usr/bin/kafka-server-start config/server.properties`

### Step 1.1  Create Kafka Topic

`/usr/bin/kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 2 --topic police.service.calls`

### Step 1.2  Produce data into topic by kafka Producer

`python kafka_server.py`

### Step 1.3  Run Kafka consumer to test if Kafka Producer is correctly implemented and producing data

Option 1: /usr/bin/kafka-console-consumer --topic "topic-name" --from-beginning --bootstrap-server localhost:9092 
Option 2: python consumer_server.py

Step 2. Submit Spark Streaming Job :
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

### Example Kafka Consumer Console Output

### Progress Reporter

### Spark UI

## Question 1
How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

## Question 2
What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?


