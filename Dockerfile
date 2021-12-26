FROM ubuntu

RUN apt update

RUN apt -y install software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt -y install python3.10

RUN apt-get -y install python3-pip

RUN apt -y install git
