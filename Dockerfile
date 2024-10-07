FROM python:3.11.6

RUN apt update -y && apt upgrade -y && \ 
    apt install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/* 
    
RUN git clone https://github.com/animeze/file-sharing/ /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD python3 main.py
