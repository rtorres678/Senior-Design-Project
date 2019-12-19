import socket
# @brief changes the preset based on offset, note current is a list so it can be modified
# @param {Label} label tkinter label object
# @param {list} soundfonts filepaths to soundfonts
# @param {list} current current index of soundfonts list
# @param {int} offset change in soundfont file
def btn_preset_change(label, soundfonts, current, offset, client_connection):
	new_sf2_index = (current[0] + offset) % len(soundfonts)
	label.config(text=soundfonts[new_sf2_index].split('/')[-1].split('.')[0].replace('_', ' ').title().center(10))
	current.pop()
	current.append(new_sf2_index)

	command = 'load ' + soundfonts[new_sf2_index] + ' \n'
	client_connection.send(command.encode())
