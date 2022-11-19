from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

GQL_ENDPOINT = 'YOUR_GQL_ENDPOINT_URL'
GQL_API_KEY = 'YOUR_GQL_API_KEY'


# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=GQL_ENDPOINT, headers= {'x-api-key': GQL_API_KEY})

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Define your query, this example is to crete a new tracker instance.
query = gql(
    """
    mutation CreateTracker($input: CreateMyfitrackrv2DBInput!){
        createMyfitrackrv2DB(input: $input){
            id
            count
        }
    }
    """
)

variables = {
    "input": {
        "id": "1",
        "count": 1
    }
}


# Execute the query on the transport
result = client.execute(query,variable_values=variables)
print(result)