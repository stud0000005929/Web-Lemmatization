#!/bin/bash

sudo docker build -t streamlit .
sudo docker run -p 8501:8501 streamlit

$SHELL
