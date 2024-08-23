import time
import json
from fluvio import Fluvio
from pytrends.request import TrendReq

# Initialize Fluvio client
fluvio = Fluvio.connect()
producer = fluvio.producer("google-trends")

# Initialize Google Trends API
pytrends = TrendReq(hl='en-US', tz=360)

# Function to fetch and send Google Trends data
def fetch_and_send_trends():
    while True:
        trending_searches_df = pytrends.trending_searches(pn='united_states')
        trends_list = trending_searches_df[0].tolist()

        # Create a structured record
        record = {
            "timestamp": time.time(),
            "trends": trends_list
        }
        
        # Produce data to Fluvio topic
        producer.send(json.dumps(record).encode('utf-8'))
        
        print("Sent trends data:", record)
        time.sleep(600)  # Fetch every 10 minutes

if __name__ == "__main__":
    fetch_and_send_trends()
