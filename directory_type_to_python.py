#This function assumes all files must be changed to .py files
for file in os.listdir():
    directory = os.getcwd()
    filename= os.path.join(directory, file)
	file_name.split('.')
    new_name = filename[0] + '.py'
    renamed = os.rename(filename,new_name)
