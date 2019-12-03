import socket

def chorus_slider_change(new_val):
	message = 'cho_set_level ' + str(new_val) + ' \n'
	print(message)
	client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_connection.connect(('127.0.0.1', 9800))
	client_connection.send(message.encode())
	client.close()
