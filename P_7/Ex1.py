# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json


SERVER = 'rest.ensembl.org'
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS) # no need to put the server


    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print(f"CONTENT: {type(data1['ping'])}")
    if data1["ping"] == 1:
        print("PING OK!!! The data base is running")
    else:
        print("ERROR data base is not running")
    # -- Print the received data
    print(f"CONTENT: {data1}")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()