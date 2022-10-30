import os
import logging
from pathlib import Path
#pathlib is used to resolve the issue with / slash like in cmd prompt the path uses \ slash
# in powershell \

logging.basicConfig(
    level = logging.INFO,
    format= '[%(asctime)s: %(levelname)s]: %(message)s'
)

while True:
    project_name = input("enter project name:")
    if project_name != '':
        break
logging.info(f"creating project by name : {project_name}")

#list of files
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py", # to create a robust package
    "init_setup.sh", 
    #help us to create repository,all the basic environment help me to do that(ex:conda env setup)
    "requirements.txt",
    "requirements_dev.txt", #only be use for tesing and also to keep libraries
    "setup.py", #help us do the basic setup
    "pyproject.toml",
    "setup.cfg",
    "tox.ini", # python packages,they need to be tested in various env 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok = True)
        logging.info(f"creating directory at : {filedir} for file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info("creating a new file : {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")
