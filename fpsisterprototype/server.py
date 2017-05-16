import os

currdir = os.path.abspath('.')

def listdir():
		for file in os.listdir(currdir):
			print file
def makefile(path):
    with open(path, 'a'):
	    return os.utime(path, None)
def removefile(path):
	return os.remove(path)

def changedirectory(path):
	print path
	currdir = currdir+'/'+path
	return os.chdir(path)

def run():
	while True:
		commands = []
		print currdir+'# ',
		command = raw_input()
		commands.extend(command.split(' '))
		# print commands

		if commands[0] == 'ls':
			listdir()
		elif commands[0] == 'touch':
			makefile(commands[1])
		elif commands[0] == 'rm':
			removefile(currdir+'/'+commands[1])
		elif commands[0] == 'cd':
			changedirectory(currdir+'/'+commands[1])

		else:
			break

if __name__ == "__main__":

	run()