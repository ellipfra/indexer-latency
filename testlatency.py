import time
import requests
import statistics
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("url", help="the URL to send requests to")
parser.add_argument("--auth", required=False, help="Authorization token")
parser.add_argument("--n", type=int, required=False, default=10, help="the number of requests to send")
parser.add_argument("--x", type=float, required=False, default=1, help="the number of seconds to wait between requests")
args = parser.parse_args()

# Get the URL and request parameters from the command line arguments
URL = args.url
N = args.n
X = args.x

# Create a persistent HTTP/2 connection
session = requests.Session()
headers = {'Authorization': args.auth,
           'Content-Type': 'application/json'}
# Set up a list to store the latencies of each request
latencies = []

# Send the requests and measure the latencies
for i in range(N):
    # Send the request
    start_time = time.perf_counter()
    response = session.post(URL, headers=headers, json={'query': '{_meta{block{number}}}'})
    end_time = time.perf_counter()
    print(response.text)

    # Calculate the latency of the request
    latency = (end_time - start_time) * 1000

    # Add the latency to the list
    latencies.append(latency)

    # Wait for X seconds before sending the next request
    time.sleep(X)

# Calculate the average and median latencies
average_latency = statistics.mean(latencies)
median_latency = statistics.median(latencies)

# Print the results
print(f"Average latency: {average_latency:.2f} ms")
print(f"Median latency: {median_latency:.2f} ms")

# Close the connection
session.close()