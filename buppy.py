class Backup:
	def getcontent(filename):
		filedata = open(filename, "r")
		file = open("backup.txt", "w")
		file.write(filedata.read())
		print("\nBackup created!")
		file.close()
		filedata.close()
