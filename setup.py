from setuptools import find_packages,setup
from typing import List
def get_requirments(file_path:str)->List[str]:
    '''
    this function is used to take the required files from the 
    requirments.txt and import that pakages from there and install.
    '''
    HYPEN_E_DOT='-e .'
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","")for req in requirments]
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)


setup(

name='mlproject',
version='0.0.1',
author='haroshin',
author_email='haroshinkk2002@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirments.txt')
)


