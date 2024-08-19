import time
from fluvio import Fluvio
from pytrends.request import TrendReq

# Initialize Fluvio client
fluvio = Fluvio.connect()
producer = fluvio.producer("google-trends")

# Initialize Google Trends API
pytrends = TrendReq()

# Function to fetch and send Google Trends data
def fetch_and_send_trends():
    while True:
        # Fetch trending searches
        trending_searches_df = pytrends.trending_searches(pn='united_states')
        trends_list = trending_searches_df[0].tolist()
        
        # Produce data to Fluvio topic
        for trend in trends_list:
            producer.send(trend.encode('utf-8'))
        
        print("Sent trends data:", trends_list)
        time.sleep(600)  # Fetch every 10 minutes

if __name__ == "__main__":
    fetch_and_send_trends()