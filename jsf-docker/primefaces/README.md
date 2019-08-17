docker build -t prime-showcase .

docker run -d -p 8080:8080 --name myjsf prime-showcase  
docker start myjsf  
docker stop myjsf

http://localhost:8080/showcase-6.2/
