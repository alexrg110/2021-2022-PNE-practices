import http.client
import json
import termcolor
PORT = 8080
IP = "127.0.0.1"

def request_server(endpoint, params=""):
    conn = http.client.HTTPConnection(IP, PORT)

    try:
        conn.request("GET", endpoint +params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    except UnicodeEncodeError:
        print("ERROR, connction has been lost.")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data2 = json.loads(data1)
    return data2

number = input("Enter limit: ")
dict_list = request_server("/listSpecies?", "&number=" + number + "&json=1")
print(dict_list)


karyotype = input("Enter information: ")
dict_karyotype = request_server("/karyotype?", "karyotype=" + karyotype + "&json=1")
print(dict_karyotype)

chromosome = input("Enter the specie: ")
chromo_number = input("Enter chromosome: ")
dict_length = request_server("/chromosomeLength?", "chromosome=" + chromosome + "&longitude=" + chromo_number + "&json=1")
print(dict_length)

sequence = input("Enter name of the sequence: ")
dict_Seq = request_server("/geneSeq?", "sequence=" + sequence + "&json=1")
print(dict_Seq)

gen = input("Enter name of the sequence: ")
dict_info = request_server("/geneInfo?", "gen=" + gen + "&json=1")
print(dict_info)



gene = input("Enter name of the sequence you need: ")
dict_Calc = request_server("/geneCalc?", "gene=" + gene + "&json=1")
print(dict_Calc)
for k in dict_Calc['base']:
    print(f"{k}: {dict_Calc['bases'][k]}")

chromo = input("Enter chromo number: ")
first = input("Enter start of the gene: ")
last = input("Enter end of the gene: ")
dict_gene_list = request_server("/geneList?", "chromo=" + chromo + "&first=" + first + "&last=" + last + "&json=1")
print(dict_gene_list)