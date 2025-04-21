#!/bin/bash

# Create Tokens
mkdir -p ../log/tokens
http POST 127.0.0.1:8000/api/token/ username=ali   password=8423904@aut > ../log/tokens/ali.json
http POST 127.0.0.1:8000/api/token/ username=ahmad password=8423904@aut > ../log/tokens/ahmad.json
http POST 127.0.0.1:8000/api/token/ username=abdol password=8423904@aut > ../log/tokens/abdol.json

http GET 127.0.0.1:8000/users/