#!/bin/bash

# Install Fluvio if not already installed
if ! command -v fluvio &> /dev/null
then
    echo "Fluvio not found, installing..."
    curl -fsS https://hub.infinyon.cloud/install/install.sh | bash
fi

# Start a local Fluvio cluster
fluvio cluster start

# Create the Google Trends topic
fluvio topic create google-trends

# Build the Smart Module
cd smart_module
cargo build --release

# Deploy the Smart Module
fluvio smartmodule deploy target/release/google_trends_smart_module

# Go back to the main directory
cd ..

# Run the connector
python3 connector/connector.py