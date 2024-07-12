import logging
from setuptools import find_packages, setup
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HYPER_E_DOT = '-e .'

def get_requirements(filepath: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of requirements,
    excluding the '-e .' entry if it exists.
    
    Parameters:
    filepath (str): Path to the requirements file.
    
    Returns:
    List[str]: A list of requirements.
    '''
    requirements = []

    try:
        with open(filepath, 'r') as fileobj:
            requirements = fileobj.readlines()
            requirements = [req.strip() for req in requirements]  # Use strip() to remove any surrounding whitespace including newlines

            if HYPER_E_DOT in requirements:
                requirements.remove(HYPER_E_DOT)
        
        logger.info("Successfully read and processed the requirements file.")
    except FileNotFoundError:
        logger.error(f"The file at {filepath} was not found.")
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {e}")
           
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ajay Kumar',
    author_email='ajayetw2009@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
