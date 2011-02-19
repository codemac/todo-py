import todo

def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('add', 
#                                          aliases=('a'), #enable in 3.2
                                          help='Append entry to todo list.')
    parser_cmd_add.add_argument('text', type=str,
                                help='Text of todo to add to list')
    COMMANDS['add'] = run

def run(args):
    todo.validate_entry(args.text)

    with open(args.todofile, 'r+b') as f:
        newlines = [x.strip() for x in f.readlines() if x]
        newlines.append(args.text)
        f.writelines([x + '\n' for x in newlines])
