#!/bin/bash

# The following script is modified from the RbSyn artifact
set -e
IMG_NAME="absent-artifact-img"
CONTAINER_NAME="absent-artifact"
DIR="/root/absynthe"
Z3RB_DIR="/root/z3rb-lazy"
STARTSCRIPT="/root/startup.sh"

if [[ "$(docker images -q $IMG_NAME 2> /dev/null)" == "" ]]; then
    docker build -t $IMG_NAME .
fi

echo "[0] starting container with name $CONTAINER_NAME ..."
if [ "$(docker ps -a | grep $CONTAINER_NAME)" ]; then
    echo "docker $CONTAINER_NAME already exist, remove it now"
    docker rm $CONTAINER_NAME
fi
docker run -v "$(pwd)/absynthe":$DIR \
           -v "$(pwd)/z3rb-lazy":$Z3RB_DIR \
           -v "$(pwd)/startup.sh":$STARTSCRIPT \
           -w $DIR --name=$CONTAINER_NAME \
           -it $IMG_NAME bash -l -c \
           "bundle config --global silence_root_warning true && \
           bundle install && \
           git config --global --add safe.directory /root/absynthe && \
           git config --global --add safe.directory /root/z3rb-lazy && \
           exec bash -l "
