FROM python:3.8-alpine
LABEL maintainer="Xavier Francisco" 

ENV PYTHONUMBUFFERED 1
# ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip

#COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-buil-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
#RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app
# COPY ./scripts /scripts
# RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user