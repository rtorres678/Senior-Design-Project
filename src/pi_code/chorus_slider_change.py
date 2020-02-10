import socket

def chorus_slider_change(new_val, client_connection):
	message = 'cho_set_level ' + str(new_val) + ' \n'
	client_connection.send(message.encode())