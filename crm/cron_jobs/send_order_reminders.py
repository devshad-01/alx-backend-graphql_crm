import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime, timedelta

# GraphQL endpoint
GRAPHQL_ENDPOINT = "http://localhost:8000/graphql"

# Define the GraphQL query
QUERY = gql("""
query {
  allOrders(filter: {orderDateGte: """ + (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d') + """}) {
    edges {
      node {
        id
        customer {
          email
        }
      }
    }
  }
}
""")

# Set up the transport and client
transport = RequestsHTTPTransport(url=GRAPHQL_ENDPOINT)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Query the GraphQL hello field to verify the endpoint is responsive
hello_query = gql("""
query {
  hello
}
""")
hello_response = client.execute(hello_query)
print(f"GraphQL endpoint response: {hello_response['hello']}")

# Execute the query
response = client.execute(QUERY)

# Log the results
with open("/tmp/order_reminders_log.txt", "a") as log_file:
    for order in response['allOrders']['edges']:
        log_file.write(f"{datetime.now()} - Order ID: {order['node']['id']}, Customer Email: {order['node']['customer']['email']}\n")

print("Order reminders processed!")
