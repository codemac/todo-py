import os
import sys

COMMANDS = {}

def init_commands(subparser):
    plugin_dir = (os.path.dirname(os.path.realpath(__file__)))
    plugin_files = [x[:-3] for x in os.listdir(plugin_dir) if x.endswith(".py")]
    sys.path.insert(0, plugin_dir)
    for plugin in plugin_files:
        mod = __import__(plugin)
        if hasattr(mod, "register"):
            mod.register(COMMANDS, subparser)

def run(command, args):
    if command in COMMANDS:
        COMMANDS[command](args)
    else:
        raise NotImplementedError
