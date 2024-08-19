# Fluvio Google Trends Dataflow Application

This project is a dataflow application that fetches Google Search Trends using Fluvio. It consists of a Python connector that pulls trends data from the Google Trends API and a Rust Smart Module that processes the data.

## Directory Structure


fluvio-google-trends/
├── connector/
│ ├── requirements.txt
│ └── connector.py
├── smart_module/
│ ├── Cargo.toml
│ └── src/
│ └── lib.rs
├── fluvio-setup.sh
└── README.md

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/imabutahersiddik/fluvio-google-trends.git
   cd fluvio-google-trends```

## Install Python dependencies:
```bash
pip install -r connector/requirements.txt```

## Run the setup script:
```bash
chmod +x fluvio-setup.sh
./fluvio-setup.sh```

## Consume data from the Fluvio topic:
Open a new terminal and run:
```bash
fluvio consume google-trends --smartmodule google_trends_smart_module```
## Create Multiple Topics:
You can create multiple topics for different data streams using:
```bash
fluvio topic create topic-name```

## Produce Data from Files:
You can produce data from a file to a topic:
```bash
fluvio produce topic-name < data-file.txt```

## Consume Data with Filters:
Apply filters while consuming data to process only specific messages:
```bash
fluvio consume topic-name --filter "keyword"```

## Use Smart Modules for Processing:
Create and deploy smart modules to process data in real-time as it flows through the topics.
## Monitor Topic Offsets:
Check the offsets of messages in a topic to track message consumption:
```bash
fluvio topic describe topic-name```

## Delete Topics:
Remove topics that are no longer needed:
```bash
fluvio topic delete topic-name```

## Notes
Make sure you have Rust and Cargo installed for building the Smart Module.
The connector fetches trends every 10 minutes. You can adjust this interval in the connector.py file.