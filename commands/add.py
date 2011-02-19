import todo
import os

def register(COMMANDS, subparser):
    parser_cmd_add = subparser.add_parser('add', 
#                                          aliases=('a'), #enable in 3.2
                                          help='Append entry to todo list.')
    parser_cmd_add.add_argument('text', type=str,
                                help='Text of todo to add to list')
    COMMANDS['add'] = run

def run(args):
    todo.validate_entry(args.text)
    toadd = args.text.strip()
    newlines = []

    with open(args.todofile, 'r+b') as f:
        f.seek(-1, os.SEEK_END) # get the last character
        isline = f.read(1)
        f.seek(0, os.SEEK_END) # go back to the end

        pre = ''
        if isline != '\n':
            pre = '\n'

        f.write(pre + toadd + '\n')
