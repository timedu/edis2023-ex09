
import json
import traceback

from supp.client_utils import post_request
from supp.config import todo, set_client_config

try:
    import readline
except:
    pass 


def print_json(data):
    print(json.dumps(data, indent=4)) 


def repl():

    while True:

        try:
            user_input = input(todo['prompt'])

        except EOFError:
            print('')
            break        

        if not user_input.strip():
            continue

        input_strings = user_input.split()

        command = input_strings[0].lower()

        try:

            if len(input_strings) == 1:

                if command in ('exit', 'quit'):
                    break

                if command == 'list':

                    result = [
                        post_request(node_id, {'operation': 'list'}) for node_id in [1,2]
                    ] 
                    print_json(result) 
                    continue 

                if command == 'reset':

                    result = [
                        post_request(node_id, {'operation': 'reset'}) for node_id in [1,2]
                    ] 
                    print_json(result) 
                    continue 

            if len(input_strings) == 2:

                assert all(char.isdigit() for char in input_strings[1])
                key = int(input_strings[1])

                if command == 'set1':

                    result = todo['client'].request_write('set', 1, key)
                    print_json(result)
                    continue 

                if command == 'set2':

                    result = todo['client'].request_write('set', 2, key)
                    print_json(result)
                    continue 

                if command == 'del1':

                    result = todo['client'].request_write('del', 1, key)
                    print_json(result)
                    continue

                if command == 'del2':

                    result = todo['client'].request_write('del', 2, key)
                    print_json(result)
                    continue

                if command == 'get':

                    result = todo['client'].request_read(key)
                    print_json(result)
                    continue
                
            raise AssertionError

        except AssertionError:
            print('Usage: { { {set|del}{1|2} | get } <int> | list|reset | exit|quit }')

        except Exception as err:
            print(err)
            traceback.print_exc()

if __name__ == '__main__':

    set_client_config()
    repl()
