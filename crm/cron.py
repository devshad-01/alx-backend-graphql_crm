from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client
from datetime import datetime

def log_crm_heartbeat():
    with open('/tmp/crm_heartbeat_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - CRM is alive\n")
    print("CRM heartbeat logged!")

def update_low_stock():
    GRAPHQL_ENDPOINT = "http://localhost:8000/graphql"
    transport = RequestsHTTPTransport(url=GRAPHQL_ENDPOINT)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    mutation = gql("""
    mutation {
      updateLowStockProducts {
        products {
          name
          stock
        }
        message
      }
    }
    """)

    response = client.execute(mutation)
    with open('/tmp/low_stock_updates_log.txt', 'a') as log_file:
        for product in response['updateLowStockProducts']['products']:
            log_file.write(f"{datetime.now()} - Product: {product['name']}, New Stock: {product['stock']}\n")
    print("Low stock products updated!")
