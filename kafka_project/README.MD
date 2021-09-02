# Transaction Streaming and Parsing with Apache Kafka

## Overview

The purpose of this project is to design a basic streaming application for a simple fraud detection system.  In this setup, random transactions will be generated and written to a Kafka topic, which will then be consumed, categorized, and written to either a *legitimate* or *fraudulent* topic stream.



![kafka_mini](https://github.com/Aaron-O-Gonzalez/springboard/blob/main/kafka_project/kafka_mini.png)



All components of the streaming application and respective dependencies can be executed by running the ***docker-compose.yml*** file.

## Code Components

The project code is divided into the following components:

- docker-compose.kafka2.yml: Docker compose file used to run the zookeeper and kafka services independently by establishing a network that is created by the user (in this case kafka-network). 

- docker-compose.yml: runs the *generator* and *detector* files as microservices. 

- generator: Folder which contains ***generator.py***, ***app.py***, ***Dockerfile***, and ***requirements.txt*** . The ***generator.py*** files generates random transactions, whereas the ***app.py*** file instantiates the Kafka producer, which will publish the ouput of *create_random_transaction()* into the queueing.transactions.

- detector: folder which contains ***detector.py***, ***appy.py***, ***Dockerfile***, and ***requirements.txt***. The ***detector.py*** file inspects each transaction, and categorizes the transaction as either legitimate (< 900 USD) or fraudulent (>= 900 USD). The ***app.py*** file instantiates the Kafka consumer, which reads messages from the queueing.transactions stream, and Kafka Producer, which publishes to either the ***streaming.transactions.legit*** or ***streaming.transactions.fraud*** streams.

  

## Code Execution

1. Ensure that Docker is running.

2. Create a network which will be used for corresponding docker compose files: 

   ```docker network create <network_name>```

   Note: Specific to this file, the docker network was named "kafka-network". Should the network be named differently, please ensure the changes added in both compose files.

3. Create the standalone Kafka ecosystem:

   ```docker-compose -f docker-compose.kafka2.yml up```

4. Run the generator and detector services:

   ```docker-compose up```

   To ensure that the messages are being properly published:

   ```docker-compose -f docker-compose.kafka2.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic queueing.transactions --from-beginning```

   The output should look similar in structure to the following image:

![All_transactions](/Users/aarongonzalez/Desktop/kafka_project/All_transactions.png)



5. To ensure that the messages are properly sorted into fraudulent topics:

   ```docker-compose -f docker-compose.kafka2.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud --from-beginning```



![Screen Shot 2021-09-02 at 12.55.49 AM](/Users/aarongonzalez/Desktop/kafka_project/Screen Shot 2021-09-02 at 12.55.49 AM.png)

6. To ensure that the messages are properly sorted into legitimate topics:

   ```docker-compose -f docker-compose.kafka2.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit--from-beginning```

   

![Screen Shot 2021-09-02 at 12.57.55 AM](/Users/aarongonzalez/Desktop/kafka_project/Screen Shot 2021-09-02 at 12.57.55 AM.png)
