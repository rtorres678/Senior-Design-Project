import socket

def rev_slider_change(new_val, client_connection):
        message = 'rev_setlevel ' + str(new_val) + ' \n'
        client_connection.send(message.encode())
