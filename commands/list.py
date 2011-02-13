def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('list', 
#                                          aliases=('ls'), #enable in 3.2
                                          help='List todo items.')
    parser_cmd_add.add_argument('search', type=str, nargs='*',
                                help='Search string to list on')
    COMMANDS['list'] = run

def find_match(line, strlist):
    for s in strlist:
        if line.find(s) > -1:
            return True

def run(args):
    toprint = []
    searching = False
    lineno_count = 0
    total_lines = 0
    
    with open(args.todofile, 'r') as tfr:
        todolines = tfr.readlines()
        # test to see if search is important
        if args.search:
            searching = True
        for line in todolines:
            lineno_count += 1
            if searching and find_match(line, args.search): 
                toprint.append((line.strip(), lineno_count))
            else:
                toprint.append((line.strip(), lineno_count))

    toprint.sort()

    lineno_count = len(str(lineno_count))
    for l, n in toprint:
        print "{:0={ww}} {}".format(n, l, ww=lineno_count) 
