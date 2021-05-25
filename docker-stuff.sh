#!/bin/bash
docker build -t petclinicselenium .
docker run --env-file=.env --rm petclinicselenium:latest
#docker ps