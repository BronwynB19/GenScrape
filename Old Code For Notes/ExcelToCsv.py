'''This is no longer needed but i wanted to keep it for notes/tips'''

import pandas as pd
import os
"""
I figured it would be easier to use the shrimp tree and this file to generate a new file with just the accession 
numbers.
There are a total of 7 possible genes. I'm thinking just write a program that reads 7 by X rows by columns.
I copy/pasted the HBGPredata sheet into an Excel file for ease-of-work
Do files i want to read need to be in the same directory?
"""

# define the file path
file_path = "C:/Users/Owner/Desktop/HBG Predata.xlsx"
# assign the path to something more understandable
HBG_Predata = pd.ExcelFile(file_path)
# define the sheet name
sheet_name = 'HBGPredata'
# define the range
start_row = 0
end_row = 264
start_col = 17
end_col = 23

'''
This line reads the specified range from the Excel file and stores it in a DataFrame (df). 
A DataFrame is a pandas data structure that resembles a table with rows and columns. 
The excel_file.parse function reads the data from the specified sheet (sheet_name), 
selects the columns within the specified range (usecols), and skips the specified number of initial rows (skiprows).
'''
df = HBG_Predata.parse(sheet_name, usecols=range(start_col, end_col + 1), skiprows=range(1, start_row))

# Specify the full path to your desktop
desktop_path = os.path.expanduser("~/Desktop")

# Save the CSV file to your desktop with a default name
output_file_path = os.path.join(desktop_path, 'Predata_Accession_Numbers.csv')

# Save the CSV to your desktop
df.to_csv(output_file_path, index=False)

'''
 Finally, this line writes the data stored in the DataFrame df to a CSV file named 'output.csv'. 
 The index=False argument tells pandas not to write the DataFrame index as a separate column in the CSV file.
'''
# df.to_csv('Predata_Accession_Numbers.csv', index=False)

