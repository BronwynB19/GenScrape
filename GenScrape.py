"""
This will only be filled with code that works based on the outline of the pseudocode.
The plan:
Stormie wants:
    as many files as there are genes (name each file the gene.fasta)
    voucher, species\n sequence
    repeat
Getting the voucher will be the tricky part
"""

import re
import requests  # if run on another system, ig make sure that requests is imported properly

# Accession number you want to retrieve data for (make user input)
accession_number = "KP725762"

# GenBank API endpoint for retrieving data
genbank_api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={accession_number}&rettype=gb"

# Make the API request
response = requests.get(genbank_api_url)

# Check if the request was successful
if response.status_code == 200:
    genbank_data = response.text
    print(response.text)
