# printbot
PrintBot - an intelligent ink-excreting friend for the 21st century home.

## Description

In the long term - this project will contain all the logic for the brain that controls PrintBot. For the first version - this will be a simple web application which allows users to enter values to a list, which is printed by PrintBot

This project is loaded with dank tech. It aims to use:
* Docker for microservices architecture
* Python-Flask for the main application server
* Elasticsearch for document store and search
* React for the front-end

## SetUp
1. Clone this repository
2. [Install docker on your machine](https://docs.docker.com/engine/installation/)
3. From your local instance of this repo, run `docker-compose build` to build our docker image
4. Run `docker-compose up -d` to start our services in docker containers
