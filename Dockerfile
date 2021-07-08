FROM pypy:slim

LABEL maintainer="Saeid Bostandoust <ssbostan@linuxmail.org>"

EXPOSE 9909

ENV NETMETER_TARGET_ADDR=http://localhost:8080
ENV NETMETER_POLLING_INTERVAL=5

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python app.py
