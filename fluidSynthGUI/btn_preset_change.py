import socket
# @brief changes the preset based on offset, note current is a list so it can be modified
# @param {Label} label tkinter label object
# @param {list} soundfonts filepaths to soundfonts
# @param {list} current current index of soundfonts list
# @param {int} offset change in soundfont file
def btn_preset_change(label, soundfonts, current, offset):
	new_sf2_index = (current[0] + offset) % len(soundfonts)
	print(new_sf2_index)
	label.config(text=soundfonts[current[0]].split('/')[-1].split('.')[0].replace('_', ' ').title().center(10))
	current.pop()
	current.append(new_sf2_index)

	# send setting change to port localhost:9800
	client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_connection.connect((socket.gethostname(), 9800))
	command = 'load ' + soundfonts[new_sf2_index] + ' \n'
	client_connection.send(command.encode())
	client.close()
