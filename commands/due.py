import todo
import datetime

def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('due',
#                                          aliases=('du'), #enable in 3.2
                                          help='List todo items by due date.')
    parser_cmd_add.add_argument('number', type=int, nargs='*',
                                help='Search string to list on')
    COMMANDS['due'] = due

    parser_cmd_add2 = subparser.add_parser('overdue',
                                           # aliases=('od') #enable in 3.2
                                           help='List todo items that are overdue.')
    parser_cmd_add2.add_argument('search', type=str, nargs='*',
                                 help='Search string to list on')
    COMMANDS['overdue'] = overdue


def due(args):
    toprint = []

    fullp = todo.fullparse_entries(args.todofile)
    
    for n, l, ds, ts, ps, cs in fullp:
        if ds:
            toprint.append((ds[0][2:], l, n))

    # get last line number as line count of file
    lineno_count, w,x,y,z,zz = fullp[-1]
    lineno_count = len(str(lineno_count))
    toprint.sort()
    for d, l, n in toprint:
        print "{:0={ww}} {} {}".format(n, d, l.strip(), ww=lineno_count)

def overdue(args):
    toprint = []

    fullp = todo.fullparse_entries(args.todofile)
    today = datetime.datetime.now()
    
    for n, l, ds, ts, ps, cs in fullp:
        if ds:
            if datetime.datetime.strptime(ds[0][2:], todo.format_date) < datetime.datetime.now():
                toprint.append((ds[0][2:], l, n))

    # get last line number as line count of file
    lineno_count, w,x,y,z,zz = fullp[-1]
    lineno_count = len(str(lineno_count))
    toprint.sort()
    for d, l, n in toprint:
        print "{:0={ww}} {} {}".format(n, d, l.strip(), ww=lineno_count)

