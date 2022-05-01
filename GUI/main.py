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
	[sg.ReadButton('', size=(x, y), font=font), sg.ReadButton('Front', size=(x, y), font=font), sg.ReadButton('', size=(x, y), font=font)],
	[sg.ReadButton('Left', size=(x, y), font=font), sg.ReadButton('Stop', size=(x, y), font=font), sg.ReadButton('Right', size=(x, y), font=font)],
	[sg.ReadButton('', size=(x, y), font=font), sg.ReadButton('Back', size=(x, y), font=font), sg.ReadButton('', size=(x, y), font=font)],
	[sg.Slider(range=(0,100))]
	[sg.Text(size=(40, 1), font=font, key='-ERROR-')],
]
window = sg.Window('Example', layout, no_titlebar=False, size=(800, 480))

run = True

# Event Loop to process "events" and get the "values" of the inputs
while run:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel':
		# if user closes window or clicks cancel
		run = False
	elif event == 'Clear':
		window['-ERROR-'].update('')
		window.refresh()
	elif event == 'Enter':
		window.perform_long_operation(my_long_operation, '-DONE-')
		window.refresh()
	elif event  == '-DONE-':
		window['-ERROR-'].update('System Failure')
	else:
		window.refresh()

window.close()