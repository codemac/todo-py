import datetime

def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('done', 
#                                          aliases=('d'), #enable in 3.2
                                          help='Complete todo item')
    parser_cmd_add.add_argument('number', type=int,
                                help='Line number to complete')
    COMMANDS['done'] = run

def run(args):
    lineno = args.number - 1 # set number to reference array index, not lineno
    with open(args.todofile, 'r') as tfr:
        todolines = tfr.readlines()
        delline = todolines[lineno]
        del todolines[lineno]
        with open(args.donefile, 'a') as tfa:
            nowtime = datetime.datetime.now().strftime('%Y.%m.%d %H:%M')
            tfa.write('[' + nowtime + '] ' + delline)
        with open(args.todofile, 'w') as tfw:
            tfw.writelines(todolines)
