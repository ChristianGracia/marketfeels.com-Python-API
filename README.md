# Python API

This repo contains a Dockerized flask app that is part of a many pods in a Kubernetes cluster

## Functions

**machine Learning**

**Scraping websites**

**Sending data to my Java API**

## Installation

build docker image

`docker build -t stock-site-python-api .`

run docker container

`docker container run --publish 8080:8080 --detach stock-site-python-api`



## Google GKE


build

`docker build -t py-api .`

tag

`docker tag py-api us.gcr.io/marketfeels/py-api:latest`

pusuh

`docker push us.gcr.io/marketfeels/py-api`

push
