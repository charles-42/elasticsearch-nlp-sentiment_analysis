#!/bin/bash

docker run -d --name elastic \
    -v "/Users/charles/Documents/pythonProject/elasticsearch-nlp-sentiment_analysis/elastic_search/data" \
    -p 9200:9200 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10

