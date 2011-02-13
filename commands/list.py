import todo

def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('list', 
#                                          aliases=('ls'), #enable in 3.2
                                          help='List todo items.')
    parser_cmd_add.add_argument('search', type=str, nargs='*',
                                help='Search string to list on.')
    COMMANDS['list'] = run
    
    parser_cmd_add2 = subparser.add_parser('projects',
                                           #aliases=('p'), #enable in 3.2
                                           help='List projects.')
    parser_cmd_add2.add_argument('search', type=str, nargs='*',
                                 help='Search string for projects.')

    COMMANDS['projects'] = run_projects

    parser_cmd_add3 = subparser.add_parser('contexts',
                                           #aliases=('c'), #enable in 3.2
                                           help='List contexts.')
    parser_cmd_add3.add_argument('search', type=str, nargs='*',
                                 help='Search string for contexts.')
    COMMANDS['contexts'] = run_contexts

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

def run_projects(args):
    if args.search:
        raise NotImplementedError
    
    projects = {}
    
    fullp = todo.fullparse_entries(args.todofile)

    for n, l, ds, ts, ps, cs in fullp:
        if ps:
            for p in ps:
                if not p in projects:
                    projects[p] = []
                projects[p].append((n,l,ds,ts,ps,cs))

    no_width = len(str(fullp[-1][0]))
    for k, v in projects.items():
        print "{:_^60}".format(k)
        v.sort(lambda x,y: x[1] < y[1])
        for n, l, ds, ts, ps, cs in v:
            print "{:0={ww}} {}".format(n, l.strip(), ww=no_width)
            
def run_contexts(args):
    if args.search:
        raise NotImplementedError
    
    contexts = {}
    
    fullp = todo.fullparse_entries(args.todofile)

    for n, l, ds, ts, ps, cs in fullp:
        if cs:
            for c in cs:
                if not c in contexts:
                    contexts[c] = []
                contexts[c].append((n,l,ds,ts,ps,cs))

    no_width = len(str(fullp[-1][0]))
    for k, v in contexts.items():
        print "{:_^60}".format(k)
        v.sort(lambda x,y: x[1] < y[1])
        for n, l, ds, ts, ps, cs in v:
            print "{:0={ww}} {}".format(n, l.strip(), ww=no_width)
        print
