FROM purplelemons/http-docker:latest

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app

CMD [ "python", "-m", "server.py" ]
