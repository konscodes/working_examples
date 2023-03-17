import os
from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
#data_file_path = script_parent / 'files' / 'text.txt'

onlyfiles = [f for f in os.listdir(script_parent) if os.path.isfile(os.path.join(script_parent, f))]
print(onlyfiles)

for filename in onlyfiles:
    newfilename = filename.replace(" ", "_")
    print(newfilename)
    oldfilepath = script_parent / filename
    newfilepath = script_parent / newfilename
    os.rename(oldfilepath, newfilepath)