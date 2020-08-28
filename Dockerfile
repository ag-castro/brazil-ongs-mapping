FROM python:3.8-alpine
LABEL maintainer="Andre Gustavo Castro - castro@webappsagency.com.br"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev libffi-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /ressonantes
WORKDIR /ressonantes
COPY ./ressonantes /ressonantes

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D userDevRessonantes
RUN chown -R userDevRessonantes:userDevRessonantes /vol/
RUN chmod -R 755 /vol/web
USER userDevRessonantes
