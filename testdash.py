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

    testdash [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    Detects ARP probing of an Amazon Dashbutton and logs it

EXAMPLES

    detectdash

EXIT STATUS

    TODO: List exit codes

"""

import sys, os, traceback, optparse, subprocess, time
from datetime import datetime
from scapy.all import *

lastdetection = 0


def arp_display(pkt):

    global lastdetection
    if pkt.haslayer(DHCP):
        if pkt[Ether].src == '44:65:0d:8e:93:48':
            if time.time() - lastdetection > 10:
                lastdetection = time.time()
                print ("Ariel Button pressed")
        else:
            print pkt[Ether].src


def main():

    global options, args

    if options.verbose: logwrite("VERBOSE")

    print "Press Button now ..."
    sniff(prn=arp_display, filter="(udp and (port 67 or 68))", store=0)if __name__ == '__main__':
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
