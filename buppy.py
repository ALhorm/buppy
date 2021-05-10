class Backup:
	def create(filename):
		filedata = open(filename, "r")
		filed = open(filename, "r")
		file = open("backup.txt", "w")
		print("\nFile content:\n" + filed.read())
		file.write(filedata.read())
		file.close()
		filedata.close()
