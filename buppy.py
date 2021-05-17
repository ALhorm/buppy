class Backup:
	def save(filename, extension):
		filedata = open(filename + ".py", "r")
		file = open("backup_" + filename + "." + extension, "w")
		file.write(filedata.read())
		print("\nThe file " + filename + ".py" + " is backed up and saved to the file backup_" + filename + "." + extension)
		file.close()
		filedata.close()
