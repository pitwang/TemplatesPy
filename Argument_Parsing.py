#!/usr/bin/python
#!coding=utf-8

import sys,getopt

#print "Number of arguments: ", len(sys.argv), "arguments."
#print "Arguments list: ", str(sys.argv)


#usage: test.py -i <inputfile> -o <outputfile>
def parseOpt(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['help', 'ifile=', 'ofile='])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", '--ifile'):
            inputfile = arg
        elif opt in ("-o", '--ofile'):
            outputfile = arg


#parseOpt(sys.argv[:])

if __name__ == "__main__":
    parseOpt(sys.argv[1:])
