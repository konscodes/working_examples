import os

mypath = "C:\\Users\\konstantin.miunts\\OneDrive - BiOS, Inc\\Script\\working examples"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

for filename in onlyfiles:
    newfilename = filename.replace("working_", "")
    #print(newfilename)
    oldfilepath = mypath + "\\" + filename
    newfilepath = mypath + "\\" + newfilename
    os.rename(oldfilepath, newfilepath)