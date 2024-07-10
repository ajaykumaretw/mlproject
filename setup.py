from setuptools import find_packages,setup
from typing import List

HYPER_E_DOT='-e .'

def get_requirements(filepath:str)->List[str]:
    '''
    This function will give requrement
 
    '''
    requirements=[]
    
    with open(filepath) as fileobj:
        requirements=fileobj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPER_E_DOT in requirements :
           requirements.remove(HYPER_E_DOT)
           
    return requirements
        

setup(
    name='mlproject',
    version='0.0.1',
    author='Ajay Kumar',
    author_email='ajayetw2009@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)