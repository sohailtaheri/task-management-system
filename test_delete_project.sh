#!/bin/bash

access_token=$(jq -r .access ~/workspace/log/tokens/abdol.json)
http GET 127.0.0.1:8000/projects/ "Authorization: Bearer $access_token" > ../log/projects.json

project_ids=$(jq -r '.[].id' ../log/projects.json)

for project_id in $project_ids; do
    http DELETE 127.0.0.1:8000/projects/$project_id/ "Authorization: Bearer $access_token"
done

http GET 127.0.0.1:8000/projects/ "Authorization: Bearer $access_token"

