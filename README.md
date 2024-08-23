# Fluvio Google Trends Project

## Overview
This project processes Google Trends data in real-time using Fluvio. It fetches trending keywords, processes them, and visualizes the data through an interactive web interface.

## Features
- **Stateful DataFlow** for processing trends data.
- **Database integration** for storing processed data.
- **Drift detection** to monitor changes in data.
- **Web interface** for visualization using Chart.js.
- **A/B testing** for keyword strategies.
- **Integration with social media** for comparative analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/imabutahersiddik/fluvio-google-trends.git
   cd fluvio-google-trends
   ```

2. Install Python dependencies:
   ```bash
   pip install -r connector/requirements.txt
   ```

3. Install Rust dependencies:
   ```bash
   cd smart_module
   cargo build --release
   ```

4. Run the setup script:
   ```bash
   chmod +x fluvio-setup.sh
   ./fluvio-setup.sh
   ```

## Running the Application
1. Start the connector:
   ```bash
   python connector/connector.py
   ```

2. Open the web interface:
   Open `web_interface/index.html` in a browser to visualize trends.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.
