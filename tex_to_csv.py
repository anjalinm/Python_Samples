#!/usr/bin/env python
import sys, os, traceback, optparse, csv, os.path, fnmatch

def main():
   
    # Creates column headers for the table
    column_headers = ['Col_1', 'Col_2', 'Col_3', 'Col_4', 'Col_5', 'Col_6', 'Col_7', 'Col_8', 'Col_9', 'Col_10', 'Col_11','Col_12']
    table=[column_headers]

    # Opens the file you want to parse
    filename = args[0]
    f = open(filename,'rU')
    filedata=[]
    i=0
    j=0

    # Finds the indexes at which the data start and end
    for data in f:
        i=i+1
        filedata.append(data)     
        if "\startdata" in data:
            j = i
        if "\enddata" in data:
            k = i
    if j==0:
        print "ERROR NO DATA"
        sys.exit()
        f.close()
   
    # Splits each line by the ampersands and adds the rows onto the table
    for each in filedata[j:k-1]:
        by_column = each.rstrip('\\\n\hline').split('&')
        table.append(by_column)

    # Writes the table to the csv file and changes name from ".tex" to ".csv"
    path_name = filename.split('.tex')[0]
    path = path_name.split('/')
    length = len(path)-1
    pure_name = path[length]
    newfile = pure_name + '.csv'
    
    # Saves in mydir as opposed to original_dir (because of write permissions)
    obj = path[length-3]
    year = path[length-2]
    save_path = '/home/anjali/mydir/%s/%s/logs'% (obj, year)
    completeName = os.path.join(save_path, newfile)

    # Writes the table to the csv
    with open(completeName, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(table)

    f.close()
    fp.close()
    sys.exit()
    return


if __name__ == '__main__':
    try:
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        if len(args) < 0:
            parser.error ('missing argument')
        if options.verbose: print '$Id$'
        main()
        sys.exit()
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)