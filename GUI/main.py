#!/usr/bin/python3

import PySimpleGUI as sg
import logging
import os
import time

# Add the log message handler to the logger
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# My function that takes a long time to do...
def my_long_operation():
    time.sleep(1)
    return 'My return value'

sg.theme('DarkAmber')   # Add a touch of color
x = 20
y = 5
font = ("Helvetica", 13)
layout = [
	[sg.Text('Enter your Pin: ', size=(40, 1), font=font), sg.Text(size=(40,1), font=font, key='-OUTPUT-')],
	[sg.ReadButton('1', size=(x, y), font=font), sg.ReadButton('2', size=(x, y), font=font), sg.ReadButton('3', size=(x, y), font=font)],
	[sg.ReadButton('4', size=(x, y), font=font), sg.ReadButton('5', size=(x, y), font=font), sg.ReadButton('6', size=(x, y), font=font)],
	[sg.ReadButton('Clear', size=(x, y), font=font), sg.ReadButton('9', size=(x, y), font=font), sg.ReadButton('Enter', size=(x, y), font=font)],
	[sg.Text(size=(40, 1), font=font, key='-ERROR-')],
]
window = sg.Window('Example', layout, no_titlebar=False, size=(800, 480))


# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
		window.closed()
	elif event == 'Clear':
		entry.clear()
		window['-OUTPUT-'].update(entry.get_value())
		window['-ERROR-'].update('')
		window.refresh()
	elif event == 'Enter':
		window.perform_long_operation(my_long_operation, '-DONE-')
		window.refresh()
	elif event  == '-DONE-':
		window['-ERROR-'].update('System Failure')
	else:
		entry.set_value(int(event))
		window['-OUTPUT-'].update(str(entry.get_value()))
		window['-ERROR-'].update('')
		window.refresh()
	print('You entered', event)

window.close()