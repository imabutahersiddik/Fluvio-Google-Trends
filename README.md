# Fluvio Google Trends Dataflow Application

This project demonstrates a real-time dataflow application that fetches Google Search Trends using Fluvio. It consists of a Python connector that pulls trends data from the Google Trends API, a Rust Smart Module for advanced processing, and a web interface for visualization.

## Features
- **Stateful DataFlow** for processing trends data.
- **Database integration** for storing processed data.
- **Drift detection** to monitor changes in data.
- **Web interface** for interactive visualization using Chart.js.
- **A/B testing** for keyword strategies.
- **Integration with social media** for comparative analysis.
- **Advanced data analysis** with Fluvio SQL engine.
- **Real-time alerts** for significant changes in trends.
- **User-defined filters** for customized views.
- **Data export functionality** for offline analysis.
- **Multi-query comparison** for side-by-side analysis of trends.
- **Enhanced visualization options** for better aesthetics and usability.

## Directory Structure
```
fluvio-google-trends/
├── connector/
│   ├── requirements.txt
│   └── connector.py
├── smart_module/
│   ├── Cargo.toml
│   └── src/
│       └── lib.rs
├── web_interface/
│   ├── index.html
│   ├── chart.js
│   ├── auth.js
│   └── dashboard.js
├── machine_learning/
│   ├── model.py
│   └── requirements.txt
├── notifications/
│   ├── notify.py
│   └── requirements.txt
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
   pip install -r machine_learning/requirements.txt
   pip install -r notifications/requirements.txt
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

3. **Open the web interface**:
   Open `web_interface/index.html` in a browser to visualize trends.

## CLI Usage
- **Create Multiple Topics**:
  ```bash
  fluvio topic create topic-name
  ```

- **Produce Data from Files**:
  ```bash
  fluvio produce topic-name < data-file.txt
  ```

- **Consume Data with Filters**:
  ```bash
  fluvio consume topic-name --filter "keyword"
  ```

- **Monitor Topic Offsets**:
  ```bash
  fluvio topic describe topic-name
  ```

- **Delete Topics**:
  ```bash
  fluvio topic delete topic-name
  ```

- **Run A/B Testing**:
  ```bash
  fluvio ab-test --group-a keywords_a --group-b keywords_b
  ```

- **Export Data to CSV**:
  ```bash
  fluvio export topic-name --format csv --output trends_data.csv
  ```

## Web Application
The web interface provides an interactive visualization of Google Trends data using Chart.js. It offers the following features:
- **Dynamic charts** for trending keywords.
- **Customizable time ranges** for trend analysis.
- **Comparison of multiple keywords** side-by-side.
- **Detailed tooltips** with search volume data.
- **Responsive design** for optimal viewing on various devices.
- **User-defined filters** to refine displayed trends.
- **Export options** for downloading trends data.

## Notes
- Make sure you have Fluvio installed and running.
- The connector fetches trends every 10 minutes by default. You can adjust this interval in the `connector.py` file.
- The Smart Module is located in the `smart_module` directory. You can modify the code to perform different data processing tasks.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

### Updates Made:
- Added new features such as A/B testing, data export functionality, and enhanced visualization options.
- Included CLI commands for A/B testing and exporting data.
- Expanded the web application section to reflect new capabilities.
