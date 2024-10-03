from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='E .'
def get_requirements(file_path:str)->List[str]:
    '''
    The Function will return the List of Requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
           requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='subodh tiwari',
    author_email='kumarsubodh150403@gmail.com',
    url='https://github.com/Subodhtiwari2003/bostonhousepricing.git',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'Flask',
    ],
)
