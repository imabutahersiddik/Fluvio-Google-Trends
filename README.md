## Fluvio Google Trends Dataflow Application

This project demonstrates a dataflow application that fetches Google Search Trends using Fluvio. It consists of a Python connector that pulls trends data from the Google Trends API and a Rust Smart Module that processes the data.

## Directory Structure

```
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
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/imabutahersiddik/fluvio-google-trends.git
   cd fluvio-google-trends
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r connector/requirements.txt
   ```

3. **Install Rust dependencies**:
   ```bash
   cd smart_module
   cargo build --release
   ```

4. **Run the setup script**:
   ```bash
   chmod +x fluvio-setup.sh
   ./fluvio-setup.sh
   ```

## Running the Application

1. **Start the connector**:
   ```bash
   python connector/connector.py
   ```

2. **Consume data from the Fluvio topic**:
   Open a new terminal and run:
   ```bash
   fluvio consume google-trends --smartmodule google_trends_smart_module
   ```

## Additional Commands

* **Create Multiple Topics:**
   ```bash
   fluvio topic create topic-name
   ```

* **Produce Data from Files:**
   ```bash
   fluvio produce topic-name < data-file.txt
   ```

* **Consume Data with Filters:**
   ```bash
   fluvio consume topic-name --filter "keyword"
   ```

* **Monitor Topic Offsets:**
   ```bash
   fluvio topic describe topic-name
   ```

* **Delete Topics:**
   ```bash
   fluvio topic delete topic-name
   ```

## Notes

* Make sure you have Fluvio installed and running.
* The connector fetches trends every 10 minutes. You can adjust this interval in the `connector.py` file.
* The Smart Module is located in the `smart_module` directory. You can modify the code to perform different data processing tasks.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.