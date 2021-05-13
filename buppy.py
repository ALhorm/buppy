class Backup:
	def result(filename, expansion):
		filedata = open(filename + ".py", "r")
		file = open("backup_" + filename + "." + expansion, "w")
		file.write(filedata.read())
		print("\nBackup created!")
		file.close()
		filedata.close()
