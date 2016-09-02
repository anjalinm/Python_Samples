These samples parse data from files of a certain format

txt_to_csv.py: 
    Parses the logfiles which arrive from the Observatory after each observation. 
    Takes all data observations and writes them to a csv in table form for easy future access. 
    Stores each csv in a file structure identical to the original, but not in the original, in order to prevent accidental overwriting of files.

csv_to_sqlcom.py: 
    Parses the resulting csv files for non-proprietary data. 
    Writes the MySQL commands required to update the radar detection database. 
    All commands are appended to a single file to keep record. 
    Has safety nets in place to catch specific errors originated from the logfiles and to let the user know which logfiles caused the issue. This prevents inaccurate database updates and allows the user to identify the cause of the errors and to manually update the database instead.
