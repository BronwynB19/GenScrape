import re
import requests
import write_from_genbank_function as wfg
import pandas as pd
'''
This will be the the hard worker.
This function will read through a list of accession numbers one at a time, and run the 'write_from_genbank' function
on them.
It will then take each output from the function, and format it into a fasta file
    Fasta files are, in fact, plain text, they just have a different file type for naming conventions
Questions for me:
    What should the parameters be, if any? Can it be a void function?
        The parameter might need to be the file that I'm reading the accession numbers from
        If that's the case, try-catch statements are important, and figuring out how to access the specified file
Questions for Stormie:
    How do you want them formatted? Is one long sequence line okay or do you want it broken up into multiple lines
        File name = 'gene_name'.fasta
        >'species', 'voucher'
        'sequence'
    What do you want to name these files? That's probably gonna be the trickiest
        I'm thinking something like 'database_number' 'gene' .fasta
        I can get the DB numbers from the spreadsheet, but not every specimen will have the same DB number
'''
# I should download the shrimp tree file (ask stormie if it will be updated)

# define the file path
file_path = "C:/Users/Owner/Desktop/Shrimp Tree.xlsx"
# assign the path to something more understandable
Shrimp_Tree = pd.ExcelFile(file_path)


# Write the entries of a column to a list given a file and the name of the gene
# Read the first column until it finds the matching gene, then add the values to gene_list
# Used to have file as a parameter, got rid of it since the file is constant. I'd only need to have it as a -
# - parameter if this was being used for multiple files, but this is a very specific solution
def convert_column_to_list(sheet_name, gene_name):
    gene_list = []
    return gene_list


def genscrape(list_of_genes):
    # Open file where accession numbers are stored
    #   Should I use the numbers directly read from the file or write them to a list and use that?
    # Read accession number
    # Write information to .fasta
    # Loop
    return 0

