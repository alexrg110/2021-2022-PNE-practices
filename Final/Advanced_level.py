import http.server
import socketserver
import termcolor
import json
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from seq1 import Seq
import http.client

HTML_FOLDER = "./html/"
SERVER = "rest.ensembl.org"
PARAMS = '?content-type=application/json'
PORT = 8080
dict_genes = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
          "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
           "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
           "ANK2": "ENSG00000145362"}
def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

def make_request_ensembl(endpoint, params=""):
    conn = http.client.HTTPConnection(SERVER)
    parameters = "?content-type=application/json"
    try:
        conn.request("GET", endpoint + parameters +params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data2 = json.loads(data1)
    return data2





# Define the Server's port
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)

        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)
        # Message to send back to the client

        if self.path == "/":
                contents = read_html_file("index.html")\
                    .render(context=
                            {"genes": SERVER + "info/species" + PARAMS})

        elif path == "/listSpecies":
                try:
                    number = int(arguments['number'][0])
                    data_species = make_request_ensembl("/info/species")
                    list1 = data_species['species']
                    empty_list = []
                    if number <= len(list1):
                        for i in range(0, number):
                            empty_list.append(list1[i]['common_name'])

                        if "json" in arguments:
                            contents = {"species": empty_list,
                                "length": len(list1),
                                "number": number}
                        else:
                            contents = read_html_file(path[1:] + ".html") \
                            .render(context={"species": empty_list,
                                "length": len(list1),
                                "number": number})
                    else:
                        contents = read_html_file("error.html").render()
                except ValueError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}
                except KeyError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}

        elif path == "/karyotype":
                try:
                    gene = arguments['karyotype'][0]
                    data_species1 = make_request_ensembl("/info/assembly/" + gene)
                    new_dict = data_species1['karyotype']
                    if "json" in arguments:
                        contents = {"karyotype": new_dict}
                    else:
                        contents = read_html_file(path[1:] + ".html") \
                        .render(context={"karyotype": new_dict})
                except KeyError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}
                except TypeError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}

        elif path == "/chromosomeLength":
                try:
                    chromosome = arguments['chromosome'][0]
                    chromo_number = arguments['longitude'][0]
                    data_species2 = make_request_ensembl("/info/assembly/" + chromosome)
                    dict_1 = data_species2['top_level_region']
                    length = ""
                    for i in dict_1:
                        if i['coord_system'] == "chromosome" and i['name'] == chromo_number:
                            length = str(i['length'])
                    if "json" in arguments:
                        contents = {"length": length}
                    else:
                        contents = read_html_file(path[1:] + ".html") \
                        .render(context={"length": length})
                except KeyError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}

        elif path == "/geneSeq":
                try:
                    gene = arguments['sequence'][0]
                    gene_name = dict_genes[gene]
                    data_seq = make_request_ensembl("/sequence/id/" + gene_name)
                    new_dict = data_seq['seq']
                    if "json" in arguments:
                        contents = {"seq": new_dict}
                    else:
                        contents = read_html_file(path[1:] + ".html") \
                        .render(context={"seq": new_dict})
                except KeyError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}

        elif path == "/geneInfo":
                try:
                    gen = arguments['gen'][0]
                    gene_name = dict_genes[gen]
                    info = make_request_ensembl("/sequence/id/" + gene_name)
                    new_dict1 = info['desc']
                    slice = new_dict1.split(":")
                    start = int(slice[3])
                    end = int(slice[4])
                    length = end - start

                    if "json" in arguments:
                            contents = {"start": start,
                                     "end": end,
                                     "length": length,
                                     "id": gene_name,
                                     "name": gen}
                    else:
                        contents = read_html_file(path[1:] + ".html") \
                            .render(context={"start": start,
                                     "end": end,
                                     "length": length,
                                     "id": gene_name,
                                     "name": gen})
                except KeyError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}

        elif path == "/geneCalc":
                try:
                    gene = arguments['gene'][0]
                    gene_name = dict_genes[gene]
                    calc = make_request_ensembl("/sequence/id/" + gene_name)
                    new_dict2 = calc['seq']
                    seq = Seq(new_dict2)
                    total_length = seq.len()
                    base = seq.count()
                    bases = seq.percentages()
                    if "json" in arguments:
                        contents = {"total_length": total_length,
                                 "base": base,
                                 "bases": bases}
                    else:
                        contents = read_html_file(path[1:] + ".html") \
                        .render(context={"total_length": total_length,
                                 "base": base,
                                 "bases": bases})
                except KeyError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}

        elif path == "/geneList":
                try:
                    chromo = arguments['chromo'][0]
                    first = arguments['first'][0]
                    last = arguments['last'][0]
                    loc_dict = make_request_ensembl("/phenotype/region/homo_sapiens/" + chromo + ":" + first + "-" + last, "")
                    empty = []
                    for i in loc_dict:
                        dict1 = i['phenotype_associations']
                        for b in dict1:
                            if "attributes" in b:
                                if "associated_gene" in b['attributes']:
                                    empty.append(b["attributes"]["associated_gene"])
                    if "json" in arguments:
                        contents = {"empty": empty}
                    else:
                        contents = read_html_file(path[1:] + ".html") \
                        .render(context={"empty": empty})

                except KeyError:
                    if "json" not in arguments:
                        contents = read_html_file("error.html").render()
                    else:
                        contents = {"ERROR during transmission. Try again"}



        else:
                contents = open("html/error.html", "r").read()

            # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        if "json" in arguments:
                contents = json.dumps(contents)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(contents.encode()))
        else:
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(contents.encode()))



        # The header is finished
                self.end_headers()

        # Send the response message
                self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()