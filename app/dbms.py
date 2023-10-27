
from flask import Flask, request

from supp.dbms_db import db
from supp.config import todo, set_server_config

server = Flask(__name__)

#
# handle request
#

@server.route('/', methods = ['POST'])
def handle_request():

   req = request.get_json()
   print(req, flush=True)

   #
   # set
   #

   if req['operation'] == 'set':

      todo['dbms'].set_record(
         req['key'],
         req['client_id'],
         req['client_counter']
      )
      return db['records'].get(req['key'],{})
     
   #
   # del
   #

   if req['operation'] == 'del':

      todo['dbms'].del_record(
         req['key'],
         req['client_id'],
         req['client_counter']
      )
      return db['records'].get(req['key'],{})
      
   #
   # get
   #

   if req['operation'] == 'get':

      return db['records'].get(req['key'],{})

   #
   # list
   #

   if req['operation'] == 'list':

      return db['records']

   #
   # reset
   #

   if req['operation'] == 'reset':

      db['counter'] = 0
      db['records'].clear()

      return db['records']

#
# start server
#

if __name__ == '__main__':

    set_server_config()
    print(f'**')
    print(f'** DBMS TODO: {todo["folder"]}')
    print(f'**')
    server.run(host='0.0.0.0', port=4000)
