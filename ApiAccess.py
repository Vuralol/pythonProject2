import json
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch

def perform_search(search_query):
    print("this is Testfile_2")

    with open('config.json', 'r') as f:
        data = json.load(f)

        api_key = data['API-Key']
        api_insttoken = data['API-Insttoken']

        # Initialize client with API key
        client = ElsClient(api_key)  # Replace 'your_api_key' with your actual API key

        # Set insttoken
        client.inst_token = api_insttoken  # Replace 'your_insttoken' with your actual insttoken

        # Initialize search object and set parameters
        search = ElsSearch(search_query, 'scopus')

        print(search.query)

        print(search.uri)

        search.execute(client)

        filepath = r"C:\Users\Vural Zurnaci\Desktop\Dump of json\dump-dummy.JSON"

        with open(filepath, "w") as file:
            json.dump(search.results, file)

        # Print results
        print("Results found:", search.results)
