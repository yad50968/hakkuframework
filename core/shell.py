#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Import python modules
import sys

# Import core modules
from core.module_manager import ModuleManager
from core import colors
from core import commandhandler

shellface = "usf"
mm = ModuleManager

def run():
	global shellface
	global mm

	ch = commandhandler.Commandhandler(mm)

	while True:
		try:
			setFace()
			command = input(colors.purple+shellface+colors.end+" > ")
			command = command.split()

			ch.handle(command)
		except KeyboardInterrupt:
			if mm.moduleLoaded == 0:
				print()
				sys.exit(0)
			else:
				print()
				mm.moduleLoaded = 0
				mm.moduleName = ""
				print(colors.green + "ctrl + c detected going back..." + colors.end)

def setFace():
	global shellface
	global mm
	if mm.moduleLoaded == 0:
		shellface = "usf"
	else:
		shellface = "usf:"+mm.moduleName