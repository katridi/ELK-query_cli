# Task description

Develop simple console or web app (up to you) application, that would connect to Elasticsearch and would provide ability to use at least 7 different types of queries that you either learned in this section or in the Elasticsearch documentation

Ideally reuse practice task from module 6 and select appropriate dataset which would provide you ability to try several types of queries, not just text, but also range and distance

# The implementation

1. match
2. fuzzy
3. raw
4. geo
5. regexp
6. time/number range
7. prefix


# Run it with suitable env

``` bash
# local setup
docker-compose -f ./docker/docker-compose.yml up -d
```

# Add data

## Go to [localhost:5061](localhost:5061)

![image](./screenshots/add_data.png)
![image](./screenshots/add_data2.png)

## Add `opensearch_dashboards_sample_data_ecommerce` or whatever index you like
## NB
Default terms for queries are from `opensearch_dashboards_sample_data_ecommerce` and it's a default index to search.



# Build docker image

``` bash
sudo docker build -t cli_es -f docker/Dockerfile .
```

# Run image

``` bash
docker run --network=host -it cli_es
```

# Usage within container

## For simplicity `search` alias is used to run the app in container



## Will give you an overview for possible commands and basic desription

![image](./screenshots/search.png)

``` bash
search
```

To change index type 
``` bash
search index "index_name"
```
You should see message if index exists
``` bash
Index set to "index_name"
```

Otherwise
``` python
ValueError: Index 'index_name' doesn't exist.
```

## Run every command `search command --help` to find out more

## 1. Match 

![image](./screenshots/match_help.png)

## Example

``` bash 
search match --term="geoip.city_name" --value="Cairo"
```