docker build -t ice-showcase .

docker run -d -p 8080:8080 --name icejsf ice-showcase  
docker start icejsf  
docker stop icejsf

http://localhost:8080/showcase/
