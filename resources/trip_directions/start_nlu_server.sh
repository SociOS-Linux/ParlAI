#!/bin/bash

MODEL_PATH=$1

rasa run --enable-api -m $MODEL_PATH/rasa-v1.9.6_nlu-trip_directions.tar.gz -p 5026 &