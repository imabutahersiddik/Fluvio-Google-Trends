#!/bin/bash

if ! command -v fluvio &> /dev/null
then
    echo "Fluvio not found, installing..."
    curl -fsS https://hub.infinyon.cloud/install/install.sh | bash
fi

fluvio cluster start
fluvio topic create google-trends
cd smart_module
cargo build --release
fluvio smartmodule deploy target/release/google_trends_smart_module
cd ..
python3 connector/connector.py
