'''setup.py - building an application as a package:
 setup.py file is a script used in Python projects to define how the project 
should be installed and packaged. It contains information about the project, 
such as its name, version, dependencies (other Python libraries it relies on), 
and any additional files or resources that need to be included.'''

from setuptools import find_packages,setup
from typing import List



# create a constant:
HYPEN_E_DOT='-e .'




def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirements'''
    
    requirements=[]
    # with open('requirments.txt') or alternative using file_path, see below
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # list comprehension:
        requirements=[req.replace("\n", "") for req in requirements]
        # add a condition:
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
        
        





setup(
    name='ML-Project',
    version='0.0.1',
    author='Fernandes',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
     
)

# install_requires=['pandas','numpy','seaborn','matplotlib'] not feasible to list 100 libraries create function instead

'''this list comprehension takes a list called requirements and 
    creates a new list where each element has any newline characters ("\n") removed.'''