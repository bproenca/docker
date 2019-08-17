FROM debian:stable
MAINTAINER bcp <bruno.cesar.proenca@gmail.com>

RUN apt-get update && apt-get upgrade -y && apt-get install -y apache2 telnet

ENV MYAVALUE my-value

EXPOSE 80

CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
