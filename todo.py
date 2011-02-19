#!/usr/bin/env python
# Todo list yay

__author__ = 'Jeff Mickey'
__version__ = '0.1.0'
__version_info__ = (0, 1, 0)
__hex_req_version__ = 0x2070100


import sys

# check version
if sys.hexversion < __hex_req_version__:
    sys.exit("at least python 2.7.1 needed!")

if sys.version_info >= (3, 2, 0):
    sys.exit("Update for command aliases! woot")

import argparse
import re
import datetime
import commands.base

# setup global parser
parser = argparse.ArgumentParser(description='Create, edit, and maintain todo lists')
parser.add_argument('-c', '--config', type=argparse.FileType('r'), dest='configfile',
                    help='Provide configuration file.')
parser.add_argument('-t', '--todo', type=str, dest='todofile',
                    help='Provide todo file.')
parser.add_argument('-d', '--done', type=str, dest='donefile',
                    help='Provide done file.')
subparser = parser.add_subparsers(dest='command_name',
                                  help='Command help')


format_date = "%Y.%m.%d"
format_time = "%H:%M"

# sloppy patterns
date_pat = re.compile('d:\d{4}\D\d{2}\D\d{2}')
time_pat = re.compile('t:\d{2}\D\d{2}')
project_pat = re.compile('[\s^]\+\S+')
context_pat = re.compile('[\s^]@\S+')

#return structure =
#  ( <line number>,
#    <line string (with trailing endline)>,
#    <dates>,
#    <times>,
#    <projects>,
#    <contexts> )
def fullparse_entries(filename):
    line_count = 0
    ret_data = []
    with open(filename, 'r') as tfr:
        todolines = tfr.readlines()
        for line in todolines:
            line_count += 1
            line_dates = date_pat.findall(line)
            line_times = time_pat.findall(line)
            line_projects = [x.strip() for x in project_pat.findall(line)]
            line_contexts = [x.strip() for x in context_pat.findall(line)]
            ret_data.append((line_count, line,
                             line_dates, line_times,
                             line_projects, line_contexts))
    return ret_data


def validate_entry(line):
    '''Raise exception on entries that are not valid.

    This will test dates, times, etc.'''

    line_dates = date_pat.findall(line)
    line_times = time_pat.findall(line)
    line_projects = project_pat.findall(line)
    line_contexts = context_pat.findall(line)
    
    if line_dates:
        for dl in line_dates:
            datetime.datetime.strptime(dl[2:], format_date)

    if line_times:
        for tl in line_times:
            datetime.datetime.strptime(tl[2:], format_time)

commands.base.init_commands(subparser)

def run(args):
    parsed = parser.parse_args(args)
    return commands.base.run(parsed.command_name, parsed)

if __name__ == "__main__":
    out = run(sys.argv[1:])
    if out:
        print out.strip()



