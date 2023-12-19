FROM ubuntu:latest
MAINTAINER Sultan Lenvu 'slenvu@mail.ru'
RUN apt-get update -qy
RUN apt-get install -qy python3 python3-pip python3-dev
RUN apt-get install -qy libpq-dev
EXPOSE 5000
WORKDIR /work
COPY sources /work
RUN pip install -r requirements.txt
CMD ["python3","app.py"]
