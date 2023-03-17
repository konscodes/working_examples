import os
from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
folder_path = script_parent / 'files' 

onlyfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
print(onlyfolders)

for index, foldername in enumerate(onlyfolders):
    newfoldername = foldername.replace('test', f'{index+1:02d}')
    print(newfoldername)
    oldfilepath = folder_path / foldername
    newfilepath = folder_path / newfoldername[:len(newfoldername)-1]
    os.rename(oldfilepath, newfilepath)