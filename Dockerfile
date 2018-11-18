FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/services/web/src

WORKDIR /opt/services/web/src

ADD . /opt/services/web/src

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]

