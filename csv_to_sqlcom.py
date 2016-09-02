#!/usr/bin/env python
import sys, os, traceback, optparse, csv, subprocess

def main():

    # Gets asteroid name from argument
    pwd=args[0]
    asteroid = (pwd.split('/')[4])

    # Checks if asteroid has name of the form "Abc" or "YYYYABC"
    # If the latter is true, adds a space between the YYYY and the ABC
    first2 = asteroid[0:2]
    if first2 == '19' or first2 == '20':
        first4 = asteroid[0:4]
        last = asteroid[4:]
        asteroid = first4 + ' ' + last

    # Gets AB name from ab.csv
    cmd = 'grep \"\\<' + asteroid + '\\>\" /home/anjali/myradar/ab.csv | awk \'{print $1 > \"abname.txt\"}\''
    subprocess.call(cmd, shell=True)
    
    # variable y indicates how many AB names were found
    y = 0
    if os.path.isfile('./abname.txt'):
        txt2 = open("abname.txt")
        with txt2 as f:
            for x, l in enumerate(f):
                pass
        y = x+1

    # Finding multiple AB names fails. Shows user which one failed and the reason
    if y > 1:
        print pwd + ' has ' + str(y) + ' ab names, command not written'
        os.remove("abname.txt")
        sys.exit()

    # One AB name passes. Program continues
    elif y == 1:
        txt2 = open("abname.txt")
        ABb = txt2.read()
        AB = ABb.rstrip('\n').replace(',', '')
        os.remove("abname.txt")

    # Finding no AB names also fails. Shows user which one failed and the reason
    elif y == 0:
        print pwd + ' did not find a match in ab.csv, command not written'
        sys.exit()

    # Opens the csv file you want to parse for Date and Telescope info
    filename = args[0]
    f = open(filename,'rU')

    # Get Telescope and Date
    # If not found, fails. Shows user which one failed and the reason
    reader = csv.reader(f)
    i = 1
    second_row = []
    for i, row in enumerate(reader):
        if i == 1:
            second_row = row
            break
    if len(second_row) < 2:
        print pwd + ' does not have enough data, command not written'
        sys.exit()
    tel = second_row[0]
    date = second_row[1]

    # Breaks up date into year month and day
    year = date[1:5]
    month = date[6:8]
    day = date[9:11]

    # Keeps month and day in format consistent with table display
    if month[0]=='0':
        month = month[1]
    if day[0]=='0':
        day = day[1]

    # Appends to the file sqlcmds.txt
    with open("sqlcmds.txt", "a") as commfile:
        commfile.write("UPDATE anjali.radar_det SET day = %s, WHERE AB = %s, year = %s, month = %s, config = '[A]';\n" % (day, AB, year, month))

    commfile.close()
    f.close()
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