#!/bin/bash

# Build the Docker image
docker build . -t bot_telegram_img
# Remove previous container
docker rm -f bot_telegram_container
# Run container
docker run -itd --name bot_telegram_container bot_telegram_img 
