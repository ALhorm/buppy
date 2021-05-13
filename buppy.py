class Backup:
	def gcff(filename):
		filedata = open(filename, "r")
		file = open("backup_" + filename + ".py", "w")
		file.write(filedata.read())
		print("\nBackup created!")
		file.close()
		filedata.close()
