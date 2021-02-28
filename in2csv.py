import os
cwd = os.getcwd()
os.system("echo Hello {}!".format(cwd))
for root, dirs, files in os.walk(cwd):
    for ind,file in enumerate(files):
        if file.endswith(".xlsx"):
            file = os.path.join(root, file)
            os.system("in2csv \"{}\" > \"{}.csv\"".format(file, file[:-5]))
            #os.system("echo \"{}\"".format(file))
            os.system("echo convert {}/{} ".format(ind+1, len(files)))
            #print(os.path.join(root, file))