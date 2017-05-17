import os
import Pyro4
from shutil import copyfile

# currdir = os.path.abspath('.')

@Pyro4.expose
class Jebret(object):

	
	def listdir(self, currdir):
		a=[]
		for i, file in enumerate(os.listdir(currdir)):
			a.append(file)
		return a
	#touch
	def makefile(self, path):
	    with open(path, 'a'):
		    return os.utime(path, None)

	#rm
	def removefile(self, path):
		return os.remove(path)

	#cd
	def changedirectory(self, path):
		print path
		os.chdir(path)
		listdir()

	#cp
	def copy(self, src, dst):
		# print src, dst
		copyfile(src, dst)

	#mv
	def move(self, src, dst):
		os.rename(src, dst)

	
	# while True:
	# 	commands = []
	# 	print currdir+'# ',
	# 	command = raw_input()
	# 	commands.extend(command.split(' '))
	# 	# print commands

	# 	if commands[0] == 'ls':
	# 		listdir(currdir)
	# 	elif commands[0] == 'touch':
	# 		makefile(commands[1])
	# 	elif commands[0] == 'rm':
	# 		removefile(currdir+'/'+commands[1])
	# 	elif commands[0] == 'cd':
	# 		print changedirectory(currdir+'/'+commands[1])
	# 	elif commands[0] == 'cp':
	# 		if '/' in commands[2]:
	# 			var1 = commands[2].split('/')[0]
	# 			var2 = commands[2].split('/')[1]
	# 			copy(currdir+'/'+commands[1], currdir+'/'+var1+'/'+var2)
	# 		elif os.path.isdir(commands[2]):
	# 			copy(currdir+'/'+commands[1], currdir+'/'+commands[2]+'/'+commands[1])
	# 		else:
	# 			copy(currdir+'/'+commands[1], currdir+'/'+commands[2])

	# 	elif commands[0] == 'mv':
	# 		if '/' in commands[2]:
	# 			var1 = commands[2].split('/')[0]
	# 			var2 = commands[2].split('/')[1]
	# 			move(currdir+'/'+commands[1], currdir+'/'+var1+'/'+var2)	
	# 		elif os.path.isdir(commands[2]):
	# 			move(currdir+'/'+commands[1], currdir+'/'+commands[2]+'/'+commands[1])
	# 		else:
	# 			move(currdir+'/'+commands[1], currdir+'/'+commands[2])

				
	# 		# removefile(currdir+'/'+commands[1])

	# 	else:
	# 		break

def main():
	Pyro4.Daemon.serveSimple(
        {
            Jebret: "example.jebret"
        },
        ns = True)

if __name__=="__main__":
    main()