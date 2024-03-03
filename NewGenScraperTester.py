from Bio import Entrez
'''
This also works, I didn't realize that the header Stormie is looking for is the DEFINITION, which I can get
with the previous version of my GenScraper code. Would it be more optimal if I continued with this API method?
It *is* harder to understand what does what, so I might just stick with the original version
Essentially, ignore this one for now
'''
# Set your email address (required by NCBI)
Entrez.email = "bbrett23171@gmail.com"

# Specify the accession number you want to retrieve
accession_number = "KP597867.1"

try:
    # Fetch the GenBank record for the specified accession number
    handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="gb", retmode="text")
    record = handle.read()
    handle.close()

    # Print the GenBank record header
    lines = record.split("\n")
    header = []
    for line in lines:
        if line.startswith("LOCUS"):
            header.append(line)
        elif line.startswith("DEFINITION"):
            header.append(line)

    header_text = "\n".join(header)
    print(header_text)

except Exception as e:
    print(f"An error occurred: {e}")
