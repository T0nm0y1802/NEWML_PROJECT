from setuptools import find_packages,setup
from typing import List

HYPHRN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function returns list of functions
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements ]

    if HYPHRN_E_DOT in requirements:
        requirements.remove(HYPHRN_E_DOT)    

    return requirements    


setup(
    name='ML_project',
    version='0.0.1',
    author='Tanmay',
    author_email='tanmaymathur1802@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)