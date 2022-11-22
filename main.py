import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

GQL_ENDPOINT = os.getenv('GQL_ENDPOINT') # PASS YOUR GRAPHQL ENDPOINT AS AN ENVIRONMENT VARIABLE
GQL_API_KEY = os.getenv('GQL_API_KEY') # PASS YOUR GRAPHQL KEY AS AN ENVIRONMENT VARIABLE

def lambda_handler(event, context):

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
            "id": "4",
            "count": 1
        }
    }


    response = client.execute(query,variable_values=variables)

    return {
        'statusCode': 200,
        'body': response
    }