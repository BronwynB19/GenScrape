import re
import requests

"""
This function takes an accession number, collect the DEFINITION and ORIGIN(assuming origin is the fasta sequence),
and write it to a new file (text or fasta file, still gotta talk to Stormie)
Will probably need to remove all the print statements in the function
"""


def write_from_genbank(accession_number):
    # set genbank_url to the search link
    # origin = sequence; organism = genus species
    global species, voucher, sequence
    genbank_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={accession_number}&rettype=gb"

    # Make the HTTP request
    response = requests.get(genbank_url)

    # Check if the request was successful
    if response.status_code == 200:
        genbank_data = response.text

        # Use regular expressions to extract the DEFINITION section to get the voucher
        definition_match = re.search(r'DEFINITION\s+([\s\S]+?)ACCESSION', genbank_data)
        if definition_match:
            uncleaned_definition = definition_match.group(1)
            # Use regular expressions to clean the definition by removing newlines and sequences of more than 1 space
            definition = re.sub(r'\n {2,}', '', uncleaned_definition)
            voucher = re.sub(r'.*?(ULLZ|HBG|KC|MNHN)(?:\s+)?(\d+).*', r'\1 \2', definition)
            voucher = voucher.replace('\n', '')
            '''
            If the above gives me problems, the regex could be "all text "
            '''

        # Use regular expressions to extract the ORIGIN section to get the sequence
        origin_match = re.search(r'ORIGIN\s+([\s\S]+?)\n//', genbank_data)
        if origin_match:
            uncleaned_origin = origin_match.group(1)
            # Use regular expressions to clean the origin by removing digits, spaces, and newlines
            origin = re.sub(r'[ \n\d]', '', uncleaned_origin)
            sequence = origin

        # Use regular expressions to extract the ORGANISM to get the species name
        species_match = re.search(r'ORGANISM\s+(.*?)\n', genbank_data, re.DOTALL)
        if species_match:
            species = species_match.group(1)
        return species, voucher, sequence
    else:
        print(f"Error: Unable to retrieve data. Status code: {response.status_code}")


# Testing

accession_number_list = ['EU868707.1', 'KP075951.1', 'JX403865.1', 'KP759365']
'''
for i in accession_number_list:
    species, voucher, sequence = write_from_genbank(i)
    print('Accession Number:', i)
    print('>', species, ', ', voucher,  sep='')
    print(sequence)
    print('----------------\n')
'''
