#!/bin/bash

# Each user can create a project
declare -A users=(
    ["ali"]="Ali's $RANDOM:Description of Ali's Project"
    ["ahmad"]="Ahmad's $RANDOM:Description of Ahmad's Project"
    ["abdol"]="Abdol's $RANDOM:Description of Abdol's Project"
)

for user in "${!users[@]}"; do
    IFS=":" read -r project_name project_description <<< "${users[$user]}"
    access_token=$(jq -r .access ~/workspace/log/tokens/${user}.json)
    http POST 127.0.0.1:8000/projects/ "Authorization: Bearer $access_token" title="$project_name" description="$project_description"        
done

access_token=$(jq -r .access ~/workspace/log/tokens/ali.json)
http GET 127.0.0.1:8000/projects/ "Authorization: Bearer $access_token"