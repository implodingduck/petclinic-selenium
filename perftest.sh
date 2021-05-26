#!/bin/bash
for i in {1..5}
do
    docker run --env-file=.env --rm -d petclinicselenium:latest
done