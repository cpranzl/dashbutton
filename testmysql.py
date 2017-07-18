#!/usr/bin/env python

__author__ = "Christoph Pranzl"
__copyright__ = "Copyright 2016, Christoph Pranzl"
__credits__ = ["Christoph Pranzl"]
__license__ = "GPL-2.0"
__version__ = "0.0.1"
__maintainer__ = "Christoph Pranzl"
__email__ = "christoph.pranzl@fasolt.net"
__status__ = "prototype"

"""
SYNOPSIS

    testmysql [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    Insert a timestamp in a given MySQL database

EXAMPLES

    testmysql

EXIT STATUS

    TODO: List exit codes

"""

import sys, os, traceback, optparse, time
from datetime import datetime
import MySQLdb

def main():

    global options, args

    if options.verbose: logwrite("VERBOSE")


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], versio$
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
    (options, args) = parser.parse_args()
        if options.verbose: print(datetime.utcnow().isoformat())
        main()
        if options.verbose: print(datetime.utcnow().isoformat())
        if options.verbose: print('TOTAL RUNNING TIME IN MINUTES:'),
        if options.verbose: print((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
     except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
