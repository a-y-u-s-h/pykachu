FROM ubuntu

ADD . app/
WORKDIR app/

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN pip3 install -r requirements.txt

EXPOSE 4000