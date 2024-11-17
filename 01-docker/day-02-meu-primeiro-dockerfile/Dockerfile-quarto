FROM ubuntu:22.04
LABEL mainteiner="marcus.vbrangel@gmail.com"
RUN apt-get update && apt-get install nginx -y && apt-get install curl -y && rm -rf /var/lib/apt/lists/*
#COPY index.html /var/www/html
COPY ./acuas-1.0.0 /var/www/html 
WORKDIR /var/www/html
ENV APP_VERSION=1.0.0
EXPOSE 80
HEALTHCHECK --timeout=2s CMD curl -f localhost || exit 1
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
