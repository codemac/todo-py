def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('pri', 
#                                          aliases=('d'), #enable in 3.2
                                          help='Set the priority of a todo item')
    parser_cmd_add.add_argument('number', type=int,
                                help='Line to proritize')
    parser_cmd_add.add_argument('priority', type=str,
                                help='Priority to be set')
    COMMANDS['pri'] = run

def run(args):
    todolines = []
    lineno = args.number - 1
    with open(args.todofile, 'r') as tfr:
        todolines = tfr.readlines()
        priline = todolines[lineno]
        todolines[lineno] = '({}) {}'.format(args.priority,priline)
    with open(args.todofile, 'w') as tfw:
        tfw.writelines(todolines)
