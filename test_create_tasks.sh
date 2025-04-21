#!/bin/bash

# Create 10 random tasks
for i in {1..10}; do
    # Randomly select a user token
    user=$(shuf -n 1 -e ali ahmad abdol)
    access_token=$(jq -r .access ~/workspace/log/tokens/${user}.json)

    # Fetch the user's projects and randomly select one
    http GET 127.0.0.1:8000/projects/ "Authorization: Bearer $access_token" > ~/workspace/log/projects_${user}.json
    project_id=$(jq -r '.[].id' ~/workspace/log/projects_${user}.json | shuf -n 1)

    # Fetch user list to randomy assing tasks to
    http GET 127.0.0.1:8000/users/  > ~/workspace/log/users.json
    assignee=$(jq -r '.[].id' ~/workspace/log/users.json | shuf -n 1)
    
    # Generate random task data
    title="Task_$RANDOM"
    description="Description_$RANDOM"
    priority=$(shuf -n 1 -e low medium high)

    
    # Create the task
    http POST 127.0.0.1:8000/tasks/ \
        "Authorization: Bearer $access_token" \
        title="$title" \
        description="$description"\
        project="$project_id" \
        status="pending" \
        priority="$priority" \
        due_date="2025-04-22"\
        "assigned_to"="$assignee"
done

