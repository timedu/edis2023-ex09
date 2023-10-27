
from argparse import ArgumentParser
from supp.client_utils import get_client_id

todo = {}


def _get_arguments():

    parser = ArgumentParser(
        description='Assignment 9'
    )
    parser.add_argument(
        '-r', '--review', choices=['0', '1', '2'], default='0',
        help='whose code is being run, default: 0 (your code)'
    ) 
    return vars(parser.parse_args())



def _get_todo_folder(args):

    return 'your_code' if not int(args.get('review')) else f'review_{args["review"]}'     



def set_server_config():

    args = _get_arguments()

    if args['review'] == '1':
         from todos.review_1 import todo_dbms

    elif args['review'] == '2':
         from todos.review_2 import todo_dbms

    else:
         from todos.your_code import todo_dbms
    
    todo['dbms'] = todo_dbms
    todo['folder'] = _get_todo_folder(args)



def set_client_config():

    args = _get_arguments()

    if args['review'] == '1':
         from todos.review_1 import todo_client

    elif args['review'] == '2':
         from todos.review_2 import todo_client

    else:
         from todos.your_code import todo_client
    
    todo['client'] = todo_client  
    todo['prompt'] = f'[{_get_todo_folder(args)} / client-{get_client_id()}] > '
