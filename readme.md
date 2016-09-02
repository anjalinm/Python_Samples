These samples parse data from files of a certain format

sample_input.tex:

    tex file which arrives from the Observatory after each observation. 
    Contains observational data in a table format.

txt_to_csv.py: 

    Parses "sample_input.tex".
    Takes data from the table in "sample_input.tex" and writes to a new file "sample_input.csv" for easy future access. 
    Stores each "sample_input.csv" in a directory structure identical to the original, but not in the original, in order to prevent accidental overwriting of files.

sample_input.csv:

    The output of txt_to_csv.py. 
    Contains the data from the table in "sample_input.tex".  

csv_to_sqlcom.py:

    Parses "sample_input.csv" for non-proprietary data. 
    Writes the MySQL commands required to update the radar detection database. 
    All commands are appended to "sqlcmds.txt" to keep record. 
    Has safety nets in place to catch specific errors originated from "sample_input.tex" and to let the user know the path to the problem filee. This prevents inaccurate database updates and allows the user to identify the cause of the errors and to manually update the database instead.

sqlcmds.txt:

    The output of csv_to_sqlcom.py.
    Contains the MySQL commands necessary to update the radar detection table in the main database.
