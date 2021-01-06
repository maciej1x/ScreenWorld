#!/bin/sh
echo Building image
docker build -t screenworld .

echo Starting container
docker container run  -t -d --privileged --cap-add=NET_ADMIN -p 56777:56777 --name screenworld screenworld