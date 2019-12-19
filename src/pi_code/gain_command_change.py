def gain_command_change(new_val, client_connection):
	message = 'set synth.gain ' + str(new_val) + ' \n'
	client_connection.send(message.encode())
