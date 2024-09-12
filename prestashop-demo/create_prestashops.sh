#!/bin/bash

# Check if the number of prestashops is provided as an argument
if [ $# -lt 1 ]; then
    echo "Please provide the number of prestashops to deploy as an argument."
    exit 1
fi

num_prestashops=$1
start_port=8080

# Function to create the test
create_test() {
    # Loop through and deploy the specified number of prestashops
    for ((i=0; i<num_prestashops; i++)); do
        port=$((start_port + i))
        
        # Set the PORT environment variable
        echo "PORT=$port" > .env
        
        # Deploy the prestashop using docker compose
        sudo docker compose --project-name ps$port up -d
    done

    echo "Deployed $num_prestashops prestashop instances."
    # Print the URLs to reach the deployed prestashop instances
    for ((i=0; i<num_prestashops; i++)); do
        port=$((start_port + i))
        echo "Prestashop instance $((i+1)): http://web1.elemento.cloud:$port/"
    done
}

# Function to clean the test
clean_test() {
    for ((i=0; i<num_prestashops; i++)); do
        port=$((start_port + i))
        sudo docker compose --project-name ps$port down
    done
    echo "Cleaned up $num_prestashops prestashop instances."
}

if [ "$2" == "clean" ]; then
    clean_test
else
    create_test
fi
