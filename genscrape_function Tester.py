import pandas as pd
import re
import write_from_genbank_function as wfg
import os
import time

"""
This is the file that generates the file for now
Still need to complete and put into the genscrape_function file
Need to pull fasta files by next week (its 11/1 rn)
"""

# Seeing the runtime for curiosity
start = time.time()

# define the file path
file_path = "C:/Users/Owner/Desktop/Shrimp Tree4.xlsx"
# assign the path to something more understandable
Shrimp_Tree = pd.ExcelFile(file_path)

# parameter information
sheet_name = 'CHOW et al., 2021'
gene_name = 'Enol'

# Load the sheet into a dataframe (without 'header=None', it will treat the second row as index 0)
df = Shrimp_Tree.parse(sheet_name, header=None)
row_index = 0  # Row index (0-based) where you want to search (e.g., the first row)
# Find the column index where the search value is located
column_index = df.iloc[row_index].eq(gene_name).idxmax()
# Check if the value was found in the row
if not pd.isna(column_index):
    # Column index (0-based) where the value was found
    print(f'Value "{gene_name}" found at row {row_index + 1}, column {column_index + 1}')
else:
    print(f'Value "{gene_name}" not found in the specified row.')
print(column_index)

# Make a dataframe of the specified column
gene_list = df[column_index]

# Turn NaN values in list into string ('no data')
gene_list = gene_list.fillna('no data')
total_cell_length = len(gene_list)-1  # minus 1 to get rid of the gene name cell, should be same for every gene
print('total cells:', total_cell_length)

# TEST: Remove all entries that say 'no data'
gene_list = [item for item in gene_list if item != 'no data']
non_empty_cells = gene_list
non_empty_cell_length = len(non_empty_cells)-1  # minus 1 to get rid of the gene name cell
print("Removed \'no data\':", non_empty_cells)
print('non empty cells:', non_empty_cell_length, '\n')

# Remove all non-accession numbers
gene_list = [item for item in gene_list if re.match(r'[A-Z][A-Z]\d+(\.1)?$', item)]
cells_with_accession_numbers_length = len(gene_list)
print('gene list clean:', gene_list)
print('cells_with_accession_numbers:', cells_with_accession_numbers_length)

# Define the file path for the FASTA file
fasta_file_path = os.path.join(os.path.expanduser("~/Desktop"), 'Chow Enol.fasta')

# Info for troubleshooting ------
# number of cells that have no info in them
empty_cell_length = total_cell_length - non_empty_cell_length
# Number of cells that have info but not accession numbers (are these new data?)
cells_without_accession_numbers_length = non_empty_cell_length - len(gene_list)

# Open the file in write mode ('w')
with open(fasta_file_path, 'w') as fasta_file:
    for i in gene_list:
        species, voucher, sequence = wfg.write_from_genbank(i)

        # Write the FASTA format to the file
        fasta_file.write(f'>{species}, {voucher}\n')
        fasta_file.write(sequence + '\n')
        fasta_file.write('\n')
    fasta_file.write('Total cells: ' + str(total_cell_length) + '\n')
    fasta_file.write('Empty cells: ' + str(empty_cell_length) + '\n')
    fasta_file.write('Non-empty cells: ' + str(non_empty_cell_length) + '\n')
    fasta_file.write('Cells without accession numbers(new data?): ' + str(cells_without_accession_numbers_length) + '\n')
    fasta_file.write('Cells with accession numbers: ' + str(cells_with_accession_numbers_length) + '\n')
print("FASTA file created successfully.")

end = time.time()
print('Runtime:', end-start)

# ----------------------------------------------------
'''
for i in gene_list:
    species, voucher, sequence = wfg.write_from_genbank(i)
    print('Accession Number:', i)
    print('>', species, ', ', voucher, sep='')
    print(sequence)
    print('----------------\n')
print('END')
'''

# Write the entries of a column to a list given a file and the name of the gene
# Read the first column until it finds the matching gene, then add the values to gene_list
# Used to have file as a parameter, got rid of it since the file is constant. I'd only need to have it as a -
# - parameter if this was being used for multiple files, but this is a very specific solution
# Open file
# Read through row 1/0 until you find 'gene_name'
# Read 'gene_name' column and add each one to gene_list until specified row(note: Z)
# Z: (need to specify a number because there is no set identifier that could stop it)
# Clean gene_list of all non-usable entries
