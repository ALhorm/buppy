class Backup:
	def result(filename, extension):
		filedata = open(filename + ".py", "r")
		file = open("backup_" + filename + "." + extension, "w")
		file.write(filedata.read())
		print("\nThe backup is created and saved to a file " + "backup_" + filename + "." + extension)
		file.close()
		filedata.close()
