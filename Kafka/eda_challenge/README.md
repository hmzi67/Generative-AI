# A Challenge: FastAPI Event Driven Microservices Development With Kafka, KRaft, Docker Compose, and Poetry

- **Kafka 3.5 use zookeeper**. Zookeeper is a 3rd party tool providing highly reliable distributed coordination of cloud applications. It handle all metadata of kafka.

- **Kafka 3.7 use KRaft**. KRaft is a new distributed coordination system for Kafka. So we don't need to install or use third party tools for handling metadata. Kakfa has now its own.


## Kafka 3.7 Docker Images
Follow this Quick Start with Docker and KRaft:
https://kafka.apache.org/quickstart

Get the docker image
```
docker pull apache/kafka:3.7.0
```
Start the kafka docker container
```
docker run -p 9092:9092 --name kafka-cont apache/kafka:3.7.0
```
Open another console and check to see if container running:
```
docker ps
```
Copy the container name, and give the following command to attach:
```
docker exec -it <container_name> /bin/bash/
```
**Note:** you can also use first four digit of *container_id*

After getting in intractive mode check your position:
```
ls
```
Note: Kafka commands are in this directory in the container
```
cd /opt/kafka/bin
```
then:
```
ls
```
## Create a Topic to store your Events
Ready to store your events in Kafka? Here's what you need to do first:

- Create a Topic:  In Kafka, events are organized into categories called topics. You'll need to create a topic specifically for the events you want to store.

- Use the Kafka Command-Line Tools: The exact command will vary depending on your Kafka version and desired topic configuration.

So before you can write your first events, you must create a topic. Run:
```
/opt/kafka/bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```
All of Kafka's command line tools have additional options:

Note: run the kafka-topics.sh command without any arguments to display usage information. For example, it can also show you details such as the partition count of the new topic:
```
/opt/kafka/bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
```
## Write events to a Kafka topic
A Kafka client communicates with the Kafka brokers via the network for writing (or reading) events. Once received, the brokers will store the events in a durable and fault-tolerant manner for as long as you need—even forever.

Run the console producer client to write a few events into your topic. By default, each line you enter will result in a separate event being written to the topic.

```
/opt/kafka/bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
```

Generate enents:
>Hello this is my event

>I'm Hamza Waheed

## Read the Event

Open another terminal session and run the console consumer client to read the events you just created:
```
/opt/kafka/bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```
You should see the events you just created:
>Hello this is my event

>I'm Hamza Waheed

Because events are durably stored in Kafka, they can be read as many times and by as many consumers as you want. You can easily verify this by opening yet another terminal session and re-running the previous command again.

# Kafka UI 
This is a popular open-source web UI specifically designed for viewing Kafka topics, messages, brokers, consumer groups, and even lets you create new topics. It's known for being lightweight, easy to set up, and supports secure connections. You can find the project on Github here:

https://github.com/provectus/kafka-ui

https://github.com/provectus/kafka-ui?tab=readme-ov-file#getting-started

Creating Network:
```
docker network create -d bridge <network-name>
```
Check runnning network:
```
docker network ls
```

Run Kafka:
```
docker run -p 9092:9092 --network <network-name> --name <container-name> apache/kafka:3.7.0
```

Run Kafka UI:
```
docker run -it -p 8080:8080 --network <network-name> -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui
```

Note: It will run for few second and then goes offline. We'll configure it in compose

