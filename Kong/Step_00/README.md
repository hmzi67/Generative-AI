
# Handling Authentication and Authorization with Kong and FastAPI

https://emrah-t.medium.com/kong-api-gateway-with-microservices-part-ii-handling-authentication-and-authorization-with-kong-4f2471b899b0

https://konghq.com/blog/engineering/kong-gateway-oauth2

## Docker host for internel communication

    http://host.docker.internal:8085/

## Host:
    protocol    domain              path
    http://     codehuntspk.com   /index

## Microservice Hosts:
- http://service1Host:8000/index.html
- http://service2Host:8005/team.html
- http://service3Host:8002/portfolio.html

## Kong:
- https://codehuntspk.com/index.html
- https://codehuntspk.com/team.html
- https://codehuntspk.com/portfolio.html

### For Example:
When we hit

    >> https://codehuntspk.com/index.html

then request will send to `Kong`. Kong will check the request and apply `reverse proxy` and then send it to 

    >> http://service1Host:8000/index.html

## JSON Web Tokens 
- JSON Web Tokens (JWTs) are a standardized way to securely send data between two parties.
- The JWT plugin lets you verify requests containing HS256 or RS256 signed JSON Web Tokens, as specified in RFC 7519.

## Access control lists (ACLs)
Access control lists (ACLs) provide a means to filter packets by allowing a user to permit or deny specific IP traffic at defined interfaces. Access lists filter network traffic by controlling whether packets are forwarded or blocked at the router's interfaces based on the criteria you specified within the access list.

## Temporary File System (tmpfs)
A tmpfs is a file system that resides in memory. It is a temporary file system that is not stored on a physical disk. It is store data but locally but when container will removed or down then data will also delete.