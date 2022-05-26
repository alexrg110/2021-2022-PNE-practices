import http.client
import json
import termcolor


SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"
genes_dict = {"SRCAP": "ENSG00000080603",
            "FRAT1": "ENSG00000165879",
            "ADA": "ENSG00000196839",
            "FXN": "ENSG00000165060",
            "RNU6_269P": "ENSG00000212379",
            "MIR633": "ENSG00000207552",
            "TTTY4C": "ENSG00000228296",
            "RBMY2YP": "ENSG00000227633",
            "FGFR3": "ENSG00000068078",
            "KDR": "ENSG00000128052",
            "ANK2": "ENSG00000145362"}

gene = "MIR633"
print(f"\nConnecting to server: {SERVER}\n")
id = genes_dict[gene]

conn = http.client.HTTPConnection(SERVER)


try:
    conn.request("GET", ENDPOINT + id + PARAMS) # no need to put the server
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")


data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)

termcolor.cprint("Gene:", "yellow", end='')
print(gene)
termcolor.cprint("Description: ", "yellow", end='')
print(data1['desc'])
termcolor.cprint("Bases: ", "yellow", end='')
print(data1['seq'])
