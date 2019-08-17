# ecs_python_webapp

Docker image used to test AWS ECS.  
Simple python web application.  
ECS: You can stress this app by calling `/stress?minutes=1` and check if auto-scaling is working properly.

[Image Repository](https://hub.docker.com/r/bproenca/ecs_python_webapp/)

To run this container (locally):
```
docker pull bproenca/ecs_python_webapp
docker run -d -p 80:80 bproenca/ecs_python_webapp
```
