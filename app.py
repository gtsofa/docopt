"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    create_room <room_type> <room_name>...
    
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd

from docopt import docopt, DocoptExit
from 


def docopt_dojo(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

@docopt_dojo
def add_person(self, args):
    """"Adds a person"""
    pass

def create_room(self, args):
    """
    Usage: create_room <room_type> <room_name>...
    """
    for room in args['<room_name>']:
    if args['<room_type>'].lower() == 'office' or args['<room_type>'].lower() == 'livingspace':
        # call function to create room
        for room in args['<room_name>']:
            #call the create room fn with args['<room_type>'] as room type and room as room name