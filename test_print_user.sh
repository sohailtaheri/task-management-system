#!/bin/bash

http GET 127.0.0.1:8000/users/ > ~/workspace/log/users.json

jq -c '.[]' ~/workspace/log/users.json | while read -r user; do
    user_id=$(echo "$user" | jq -r .id)
    user_name=$(echo "$user" | jq -r .username)
    if [ "$user_id" -eq 1 ]; then
        continue
    fi

    access_token=$(jq -r .access ~/workspace/log/tokens/${user_name}.json)
    echo "User ID: $user_id"
    echo "User Name: $user_name"
    echo "Access Token: $access_token"
    echo "----------------------------------------"
    
    # Fetch user details
    http GET 127.0.0.1:8000/users/$user_id/ "Authorization: Bearer $access_token"
done