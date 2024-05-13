# Declarative Style:
- Docker file

# Imperative Style:

### Image

    docker build -t ImageName:Tag . 
    docker build -f Dockerfile -t ImageName:tag .
### Container

    docker run -d -p 8000:8000 ImageName
    docker run -d -p 8001:8000 ImgName


# compose.yaml  

    Compose allows you to define the different services (containers) that make
    up your application in a single YAML file. This file specifies things like the
    image to use for each container, any environment variables, ports to expose, 
    and how the containers should link together.
- For <b>Declarative Style</b> we use compose.yml
- Streamlined development experience

        By using Compose, you can set up a consistent development environment with all the
        dependencies your application needs. This makes it easier for developers to work on 
        the project and ensures everyone has the same environment.
- Start, stop, and manage services with a single command

        Once you've defined your services in the YAML file, you can use Docker Compose 
        commands to easily manage them. For instance, with a single command you can start up 
        all the containers required for your application, stop them all, or rebuild them.
- Simplified collaboration

        The Compose YAML file acts as a clear and shareable definition of your application's 
        infrastructure. This makes it easier for teams to collaborate on development and 
        deployment.
- YAML is a supper set of JSON

## JSON structure

    { 
        "name" : "fastapi" 
        "services": {
            "api":  {
                "build": {
                    "context": "."
                    "dockerfile": "Dockerfile"
                }
            }
            "container_name": "myDevContainer"
                "ports": ["8080:8080"] 
            }
    }

## YAML structure

    version: '1.0.0'
    name: "fastapi"
    services:
    api:
        build: 
            context: ./
            dockerfile: Dockerfile
        container_name: myDevContainer
        ports:
          - "8000:8000"


## Benefits:
- Reduced complexity
- Improved development workflow
- Enhanced collaboration

#### Docker Desktop already have docekr compose so there is no need to install docker compose
Use the following command to check which version is installed:

    docker compose version

## Docker Compose File

- Written in YAML format
- Defining and managing multi-container applications with Docker

### Structure of a Docker Compose File:

    version: "1.0.0"
    name: "fastapi"
    services:
    api:
        build: ./Dockerfile
        container_name: myDevContainer
        
        expose:
        - 8000:8000

## Explanation:
- version: This specifies the Docker Compose file version (here, version 3.9).
- services: This section defines only one service:

        api: This builds a container image from the todo directory with Dockerfile.dev file. 
        It exposes port 8000.

Note: Do not forget to add .env file with database credentials before building and running the api. 
## Running the application

- To run the application:

        docker compose up -d            -d: run in background

- To stop the application:

        docker compose stop

- To delete the container:

        docker compose down

- To see which container is running:

        docker ps
        docker ps -a        -a: to see all

- To delete image:

        docker rmi <image_id>

- To delete container:

        docker rm <container_id>

### Note: 
- The flag -d in the command docker-compose up -d instructs Docker Compose to run the containers in detached (background)

### Read format of docker file:

        docker compose config

## Data Types:

### YAML supports various data types, including:

- Scalars: Strings (e.g., "hello"), numbers (e.g., 42), booleans (e.g., true, false)
- Lists: Ordered collections of items, enclosed in square brackets [] (e.g., ["apple", "banana"])
- Mappings: Unordered collections of key-value pairs, enclosed in curly braces {} (e.g., {name: "Alice", age: 25})

### Tips and Best Practices:

- Use proper indentation for readability.
- Use comments (#) to explain sections of your YAML file.
- Leverage online YAML validators to check your syntax.
- Refer to the official Docker Compose documentation for a complete list of available options:

https://docs.docker.com/compose/compose-file/compose-file-v3/

By understanding YAML basics, you'll be well-equipped to write clear and effective Docker Compose files to manage your multi-container applications.


Docker container and Images are immutables and can't be changed. So If are we are working on a Image and suddenly we deleted the container and created a new container with the same image then the changes will not be reflected in the container.

For this we use Volumes that can store data and then we create new image data will be reflected in the container

## Creating storage

    volumes:
        postgres_db: 
            driver: local

## Now using that storage

    volumes:
        - postgres_db:/var/lib/postgresql/data

- "/var/lib/postgresql/data" path that postgres use to store data
