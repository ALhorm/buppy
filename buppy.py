class Backup:
	def save(filename):
		filedata = open(filename + ".py", "r")
		file = open("backup_" + filename + ".py", "w")
		file.write(filedata.read())
		print("\nThe file " + filename + ".py" + " is backed up and saved to the file backup_" + filename + ".py")
		file.close()
		filedata.close()
