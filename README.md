# Task description

Develop simple console or web app (up to you) application, that would connect to Elasticsearch and would provide ability to use at least 7 different types of queries that you either learned in this section or in the Elasticsearch documentation

Ideally reuse practice task from module 6 and select appropriate dataset which would provide you ability to try several types of queries, not just text, but also range and distance

# The implementation

1. term
2. fuzzy
3. raw
4. geo
5. regexp
6. time?


# Run it with suitable env

``` bash
# local setup
docker-compose -f ./docker/docker-compose.yml up -d
```

# Build docker image

``` bash
sudo docker build -t cli_es -f docker/Dockerfile .
```

# Run image

``` bash
docker run --network=host -it cli_es
```

# Usage within container

## For simplicity `search` alias is used to run the app

