# Graph Indexer Latency Tester

A simple script to measure the latency of basic GraphQL requests to a given subgraph URL. It queries the subgraph for the latest block number. 

It will open a single TCP connection, reusing it for all requests.

## Usage

To run the script, use the following command:

```bash
python latency_tester.py [url] [options]
```

The script accepts the following arguments:

    url: The URL to send requests to.
    --auth (optional): An authorization token to include in the request headers.
    --n (optional): The number of requests to send. Default is 10.
    --x (optional): The number of seconds to wait between requests. Default is 1.

## Example

To send 10 requests to an with a 1 second delay between each request, use the following command:

```bash
   python latency_tester.py http://exampleindexer.net/subgraphs/id/QmbJzTd7DCAg9aP57DgLsYbokrX82BjE1ToKedPMMTRCf4 --n 10 --x 1
```

## Output

The script will output the following information:

    - The average latency of the requests.
    - The median latency of the requests.

It will also print the response text of each request.