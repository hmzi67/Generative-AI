# Kafka Docker Image Usage Guide

https://github.com/apache/kafka/blob/trunk/docker/examples/README.md

https://github.com/apache/kafka/blob/trunk/docker/examples/jvm/single-node/plaintext/docker-compose.yml

### Single Node

    docker compose -f docker/examples/jvm/single-node/plaintext/docker-compose.yml up

Certainly! Here's the Docker Compose configuration in Markdown format:


# Kafka Docker Setup

This repository contains a Docker Compose configuration to set up Apache Kafka and Kafka UI.

## Services

### Broker

- **Image:** `apache/kafka:3.7.0`
- **Hostname:** `broker`
- **Container Name:** `broker`
- **Ports:** `9092:9092`

**Environment Variables:**

- `KAFKA_NODE_ID: 1`
- `KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: 'CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT'`
- `KAFKA_ADVERTISED_LISTENERS: 'PLAINTEXT_HOST://localhost:9092,PLAINTEXT://broker:19092'`
- `KAFKA_PROCESS_ROLES: 'broker,controller'`
- `KAFKA_CONTROLLER_QUORUM_VOTERS: '1@broker:29093'`
- `KAFKA_LISTENERS: 'CONTROLLER://:29093,PLAINTEXT_HOST://:9092,PLAINTEXT://:19092'`
- `KAFKA_INTER_BROKER_LISTENER_NAME: 'PLAINTEXT'`
- `KAFKA_CONTROLLER_LISTENER_NAMES: 'CONTROLLER'`
- `CLUSTER_ID: '4L6g3nShT-eMCtK--X86sw'`
- `KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1`
- `KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0`
- `KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1`
- `KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1`
- `KAFKA_LOG_DIRS: '/tmp/kraft-combined-logs'`

### Kafka UI

- **Image:** `provectuslabs/kafka-ui`
- **Container Name:** `kafka-ui`
- **Ports:** `8080:8080`

**Environment Variables:**

- `KAFKA_CLUSTERS_0_NAME: 'Local Kafka Cluster'`
- `KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: 'broker:19092'`
- `DYNAMIC_CONFIG_ENABLED: "true"`

**Depends On:**

- `broker`

## Networks

- **Driver:** `bridge`

## Usage

1. Ensure Docker and Docker Compose are installed on your machine.
2. Clone this repository.
3. Navigate to the directory containing the `docker-compose.yml` file.
4. Run the following command to start the services:
   ```sh
   docker compose up -d
   ```
   To see logs:
   ```sh
   docker compose logs -f
   ```
5. Access Kafka UI at `http://localhost:8080`.

## Stopping the Services

To stop and remove the containers, use:
```sh
docker-compose down
```

## Notes

- Kafka broker is configured with minimal replication for development purposes.
- Adjust the environment variables as needed for your setup.

Enjoy using Kafka with an easy-to-use UI for management and monitoring!

Feel free to use this Markdown content for your README.md file!

- Kafka store data in offsets and offset is start from 0 and so on (like array)