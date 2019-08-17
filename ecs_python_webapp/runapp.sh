#!/bin/bash
VALOR=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)
export EC2IP=$VALOR
python app.py
