import todo

def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('add', 
#                                          aliases=('a'), #enable in 3.2
                                          help='Append entry to todo list.')
    parser_cmd_add.add_argument('text', type=str,
                                help='Text of todo to add to list')
    COMMANDS['add'] = run

def run(args):
    with open(args.todofile, 'a') as f:
        todo.validate_entry(args.text)
        f.write(args.text + '\n')
