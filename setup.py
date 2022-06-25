from setuptools import setup
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Dibakar Deb"
DESCRIPTION="This is the first FSDS Nov Batch ML Project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    this function is going to return list of requirments
    mentioned in requirements.txt file
    
    return - This function is going to return a list which contains name 
    of libraries mentioned in requirements file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)

